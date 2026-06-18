# -*- coding: utf-8 -*-
"""Abstracao da estrategia de atualizacao diaria (Strategy pattern).

GildedRose depende somente da interface ItemUpdater (DIP), nunca das
implementacoes concretas em normal.py, aged_brie.py etc. Isso permite
adicionar novas regras de item sem alterar quem consome o updater.
"""
from src.domain.item import Item

MIN_QUALITY: int = 0
"""Menor valor de quality permitido para qualquer item (exceto Sulfuras)."""

MAX_QUALITY: int = 50
"""Maior valor de quality permitido para qualquer item (exceto Sulfuras)."""


class ItemUpdater:
    """Estrategia de atualizacao diaria de um Item.

    Cada subclasse encapsula a regra de negocio de uma familia de itens
    (item comum, Aged Brie, Sulfuras, Backstage passes, Conjured...).
    """

    def update(self, item: Item) -> None:
        """Aplica a passagem de um dia em um item.

        Muta ``item.quality`` e ``item.sell_in`` in-place, de acordo com
        a regra de negocio da subclasse.

        Args:
            item: Item a ser atualizado.

        Raises:
            NotImplementedError: Se a subclasse nao implementar a regra.
        """
        raise NotImplementedError
