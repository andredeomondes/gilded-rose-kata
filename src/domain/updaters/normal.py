# -*- coding: utf-8 -*-
"""Regra do item comum (default): nenhuma das familias especiais."""
from src.domain.item import Item
from src.domain.updaters.base import ItemUpdater, MIN_QUALITY


class NormalItemUpdater(ItemUpdater):
    """Item generico.

    Perde 1 de quality por dia, e o dobro apos o vencimento
    (``sell_in < 0``). Quality nunca fica negativa.
    """

    def update(self, item: Item) -> None:
        """Atualiza um item comum.

        Args:
            item: Item comum a ser atualizado in-place.
        """
        item.quality = max(MIN_QUALITY, item.quality - 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = max(MIN_QUALITY, item.quality - 1)
