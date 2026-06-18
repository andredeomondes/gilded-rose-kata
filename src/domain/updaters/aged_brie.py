# -*- coding: utf-8 -*-
"""Regra do item "Aged Brie"."""
from src.domain.item import Item
from src.domain.updaters.base import ItemUpdater, MAX_QUALITY


class AgedBrieUpdater(ItemUpdater):
    """Aged Brie.

    Ganha 1 de quality por dia, e o dobro apos o vencimento
    (``sell_in < 0``). Quality nunca passa de MAX_QUALITY.
    """

    def update(self, item: Item) -> None:
        """Atualiza um item Aged Brie.

        Args:
            item: Item Aged Brie a ser atualizado in-place.
        """
        item.quality = min(MAX_QUALITY, item.quality + 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = min(MAX_QUALITY, item.quality + 1)
