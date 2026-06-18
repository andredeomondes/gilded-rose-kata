# -*- coding: utf-8 -*-
"""Testes de caracterizacao: capturam o comportamento ATUAL do sistema legado.
Servem de rede de seguranca para a refatoracao (Passo 6/7) -- devem continuar
passando depois que a logica for movida para src/, sem nenhuma alteracao.
"""
import pytest

from gilded_rose import Item, GildedRose

SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"


def update(name, sell_in, quality, days=1):
    items = [Item(name, sell_in, quality)]
    rose = GildedRose(items)
    for _ in range(days):
        rose.update_quality()
    return items[0]


class TestItemComum:
    def test_perde_1_de_quality_por_dia_antes_do_vencimento(self):
        item = update("item comum", sell_in=10, quality=20)
        assert item.quality == 19
        assert item.sell_in == 9

    def test_perde_2_de_quality_por_dia_apos_vencimento(self):
        item = update("item comum", sell_in=0, quality=20)
        assert item.quality == 18
        assert item.sell_in == -1

    def test_quality_nunca_fica_negativa(self):
        item = update("item comum", sell_in=5, quality=0)
        assert item.quality == 0


class TestAgedBrie:
    def test_ganha_1_de_quality_por_dia_antes_do_vencimento(self):
        item = update(AGED_BRIE, sell_in=10, quality=20)
        assert item.quality == 21

    def test_ganha_2_de_quality_por_dia_apos_vencimento(self):
        item = update(AGED_BRIE, sell_in=0, quality=20)
        assert item.quality == 22

    def test_quality_nunca_passa_de_50(self):
        item = update(AGED_BRIE, sell_in=10, quality=50)
        assert item.quality == 50


class TestSulfuras:
    def test_quality_nunca_muda(self):
        item = update(SULFURAS, sell_in=5, quality=80)
        assert item.quality == 80

    def test_sell_in_nunca_muda(self):
        item = update(SULFURAS, sell_in=0, quality=80)
        assert item.sell_in == 0


class TestBackstagePasses:
    def test_ganha_1_de_quality_quando_sell_in_maior_que_10(self):
        item = update(BACKSTAGE, sell_in=15, quality=20)
        assert item.quality == 21

    def test_ganha_2_de_quality_quando_sell_in_entre_6_e_10(self):
        item = update(BACKSTAGE, sell_in=10, quality=20)
        assert item.quality == 22

    def test_ganha_3_de_quality_quando_sell_in_entre_0_e_5(self):
        item = update(BACKSTAGE, sell_in=5, quality=20)
        assert item.quality == 23

    def test_quality_zera_apos_o_show(self):
        item = update(BACKSTAGE, sell_in=0, quality=20)
        assert item.quality == 0

    def test_quality_nunca_passa_de_50_mesmo_com_bonus(self):
        item = update(BACKSTAGE, sell_in=5, quality=49)
        assert item.quality == 50


class TestComportamentoAtualConjured:
    """Documenta o comportamento ATUAL (com bug) do item Conjured no legado.
    Confirma o diagnostico (docs/diagnostico_tecnico.md item 7): hoje ele
    degrada como item comum, 1/dia, em vez de 2/dia. Este teste sera
    substituido pelo comportamento correto na branch feat/conjured.
    """
    def test_hoje_degrada_como_item_comum_1_por_dia(self):
        item = update("Conjured Mana Cake", sell_in=10, quality=20)
        assert item.quality == 19
