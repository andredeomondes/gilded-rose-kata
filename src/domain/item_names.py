# -*- coding: utf-8 -*-
# Nomes de item centralizados aqui em vez de repetidos como string literal
# em varios pontos do codigo (ver docs/diagnostico_tecnico.md, item 2).

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
CONJURED_PREFIX = "Conjured"


def is_conjured(item_name):
    return item_name.startswith(CONJURED_PREFIX)
