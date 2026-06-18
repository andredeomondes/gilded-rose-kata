# -*- coding: utf-8 -*-
"""Prova que GildedRose aceita um UpdaterRegistry por injecao (DIP) e que
e possivel estender o comportamento (OCP) sem alterar nenhum arquivo de
producao -- so registrando a nova regra no registry injetado.
"""
from src.domain.item import Item
from src.application.gilded_rose import GildedRose
from src.domain.updaters import ItemUpdater, build_default_registry


class DoublesQualityUpdater(ItemUpdater):
    def update(self, item):
        item.quality *= 2
        item.sell_in -= 1


def test_gilded_rose_usa_registry_default_quando_nao_recebe_nenhum():
    items = [Item("item comum", sell_in=10, quality=20)]
    GildedRose(items).update_quality()
    assert (items[0].sell_in, items[0].quality) == (9, 19)


def test_gilded_rose_aceita_registry_customizado_via_injecao():
    custom_registry = build_default_registry()
    custom_registry.register("Item Especial", DoublesQualityUpdater())

    items = [Item("Item Especial", sell_in=5, quality=10)]
    GildedRose(items, updater_registry=custom_registry).update_quality()

    assert (items[0].sell_in, items[0].quality) == (4, 20)
