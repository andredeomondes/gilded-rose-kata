# -*- coding: utf-8 -*-
"""Regra dos itens da familia "Conjured *" (RF11, docs/requisitos.md)."""
from src.domain.item import Item
from src.domain.updaters.base import ItemUpdater, MIN_QUALITY


class ConjuredItemUpdater(ItemUpdater):
    """Item Conjured.

    Degrada 2x mais rapido que um item comum: perde 2 de quality por
    dia, e o dobro (4) apos o vencimento (``sell_in < 0``). Quality
    nunca fica negativa.

    Corrige o bug do legado, que tratava Conjured como item comum
    (1 de quality por dia).
    """

    def update(self, item: Item) -> None:
        """Atualiza um item Conjured.

        Args:
            item: Item Conjured a ser atualizado in-place.
        """
        item.quality = max(MIN_QUALITY, item.quality - 2)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = max(MIN_QUALITY, item.quality - 2)
