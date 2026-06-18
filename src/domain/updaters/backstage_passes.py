# -*- coding: utf-8 -*-
"""Regra do item "Backstage passes to a TAFKAL80ETC concert"."""
from src.domain.item import Item
from src.domain.updaters.base import ItemUpdater, MAX_QUALITY


class BackstagePassesUpdater(ItemUpdater):
    """Backstage passes.

    Quality sobe conforme o show se aproxima e despenca a zero apos o
    show acontecer (``sell_in < 0``).

    Regras de incremento por dia, antes do decremento de ``sell_in``:
        * +1 sempre.
        * +1 extra (total +2) quando ``sell_in < 11``.
        * +1 extra (total +3) quando ``sell_in < 6``.

    Quality nunca passa de MAX_QUALITY e e zerada apos o show.
    """

    def update(self, item: Item) -> None:
        """Atualiza um item Backstage passes.

        Args:
            item: Item Backstage passes a ser atualizado in-place.
        """
        item.quality = min(MAX_QUALITY, item.quality + 1)
        if item.sell_in < 11:
            item.quality = min(MAX_QUALITY, item.quality + 1)
        if item.sell_in < 6:
            item.quality = min(MAX_QUALITY, item.quality + 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
