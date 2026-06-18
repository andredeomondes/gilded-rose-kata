# -*- coding: utf-8 -*-
"""Nomes de item centralizados.

Evita repetir a mesma string literal em varios pontos do codigo (ver
docs/diagnostico_tecnico.md, item 2).
"""

AGED_BRIE: str = "Aged Brie"
"""Nome exato do item que ganha quality com o tempo."""

SULFURAS: str = "Sulfuras, Hand of Ragnaros"
"""Nome exato do item lendario que nunca muda de quality/sell_in."""

BACKSTAGE_PASSES: str = "Backstage passes to a TAFKAL80ETC concert"
"""Nome exato do item cujo bonus de quality depende do sell_in."""

CONJURED_PREFIX: str = "Conjured"
"""Prefixo que identifica qualquer item "Conjured *" (familia de itens,
nao um nome exato)."""


def is_conjured(item_name: str) -> bool:
    """Indica se um item pertence a familia de itens Conjured.

    Args:
        item_name: Nome do item, por exemplo "Conjured Mana Cake".

    Returns:
        True se o nome comecar com CONJURED_PREFIX, False caso contrario.
    """
    return item_name.startswith(CONJURED_PREFIX)
