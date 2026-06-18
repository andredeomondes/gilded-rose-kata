# -*- coding: utf-8 -*-
"""Regra do item legendario "Sulfuras, Hand of Ragnaros"."""
from src.domain.item import Item
from src.domain.updaters.base import ItemUpdater


class SulfurasUpdater(ItemUpdater):
    """Sulfuras: item legendario, nunca vendido e nunca perde quality.

    ``quality`` e ``sell_in`` permanecem inalterados em qualquer cenario.
    """

    def update(self, item: Item) -> None:
        """No-op: Sulfuras nunca muda.

        Args:
            item: Ignorado.
        """
        pass
