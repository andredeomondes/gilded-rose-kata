# -*- coding: utf-8 -*-
"""Testes unitarios das estrategias isoladas (sem instanciar GildedRose).
Prova o atendimento ao RNF04 (docs/requisitos.md): cada regra pode ser
testada isoladamente.
"""
from src.domain.item import Item
from src.domain.item_updaters import (
    NormalItemUpdater,
    AgedBrieUpdater,
    SulfurasUpdater,
    BackstagePassesUpdater,
    resolve_updater,
)
from src.domain.item_names import AGED_BRIE, SULFURAS, BACKSTAGE_PASSES


def test_normal_item_updater_perde_1_por_dia():
    item = Item("item comum", sell_in=10, quality=20)
    NormalItemUpdater().update(item)
    assert (item.sell_in, item.quality) == (9, 19)


def test_normal_item_updater_clampa_em_zero():
    item = Item("item comum", sell_in=10, quality=0)
    NormalItemUpdater().update(item)
    assert item.quality == 0


def test_aged_brie_updater_ganha_1_por_dia():
    item = Item(AGED_BRIE, sell_in=10, quality=20)
    AgedBrieUpdater().update(item)
    assert item.quality == 21


def test_sulfuras_updater_nao_altera_nada():
    item = Item(SULFURAS, sell_in=5, quality=80)
    SulfurasUpdater().update(item)
    assert (item.sell_in, item.quality) == (5, 80)


def test_backstage_updater_zera_apos_show():
    item = Item(BACKSTAGE_PASSES, sell_in=0, quality=20)
    BackstagePassesUpdater().update(item)
    assert item.quality == 0


def test_resolve_updater_retorna_estrategia_correta_por_nome():
    assert isinstance(resolve_updater(AGED_BRIE), AgedBrieUpdater)
    assert isinstance(resolve_updater(SULFURAS), SulfurasUpdater)
    assert isinstance(resolve_updater(BACKSTAGE_PASSES), BackstagePassesUpdater)
    assert isinstance(resolve_updater("item qualquer"), NormalItemUpdater)
