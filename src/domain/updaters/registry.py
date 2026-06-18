# -*- coding: utf-8 -*-
"""Registro de estrategias, injetavel em GildedRose (DIP).

Diferente do antigo resolve_updater() fixo no modulo, este registro pode
ser estendido em tempo de execucao via register()/register_by_predicate()
sem editar este arquivo -- quem monta o registro (build_default_registry,
um teste, outro cliente) decide o que cadastrar (OCP).
"""
from typing import Callable, Dict, List, Tuple

from src.domain.item_names import AGED_BRIE, SULFURAS, BACKSTAGE_PASSES, is_conjured
from src.domain.updaters.base import ItemUpdater
from src.domain.updaters.normal import NormalItemUpdater
from src.domain.updaters.aged_brie import AgedBrieUpdater
from src.domain.updaters.sulfuras import SulfurasUpdater
from src.domain.updaters.backstage_passes import BackstagePassesUpdater
from src.domain.updaters.conjured import ConjuredItemUpdater

NamePredicate = Callable[[str], bool]
"""Predicado usado para casar um item pelo nome (ex.: prefixo "Conjured")."""


class UpdaterRegistry:
    """Mapeia nome de item para ItemUpdater.

    A resolucao tem fallback para correspondencia por predicado e, por
    fim, para um updater default. A ordem de resolucao em ``resolve`` e:

        1. Correspondencia exata por nome (``register``).
        2. Primeiro predicado que casar (``register_by_predicate``, na
           ordem em que foram registrados).
        3. ``default_updater``.

    Attributes:
        _default_updater: Estrategia usada quando nada mais casar.
        _updaters_by_name: Mapa de nome exato de item para updater.
        _predicate_updaters: Lista de pares (predicado, updater), na
            ordem de prioridade de avaliacao.
    """

    def __init__(self, default_updater: ItemUpdater) -> None:
        """Inicializa um registry vazio com um updater default.

        Args:
            default_updater: Estrategia usada quando nenhum nome ou
                predicado registrado corresponde ao item.
        """
        self._default_updater: ItemUpdater = default_updater
        self._updaters_by_name: Dict[str, ItemUpdater] = {}
        self._predicate_updaters: List[Tuple[NamePredicate, ItemUpdater]] = []

    def register(self, item_name: str, updater: ItemUpdater) -> "UpdaterRegistry":
        """Associa um nome exato de item a um updater.

        Args:
            item_name: Nome exato do item (ex. "Aged Brie").
            updater: Estrategia a ser usada para esse item.

        Returns:
            A propria instancia, para permitir encadeamento de chamadas.
        """
        self._updaters_by_name[item_name] = updater
        return self

    def register_by_predicate(
        self, predicate: NamePredicate, updater: ItemUpdater
    ) -> "UpdaterRegistry":
        """Associa um predicado sobre o nome do item a um updater.

        Util para familias de itens identificadas por padrao (ex.
        prefixo "Conjured") em vez de nome exato.

        Args:
            predicate: Funcao que recebe o nome do item e retorna True
                se ele pertence a familia tratada por ``updater``.
            updater: Estrategia a ser usada quando ``predicate`` for
                verdadeiro.

        Returns:
            A propria instancia, para permitir encadeamento de chamadas.
        """
        self._predicate_updaters.append((predicate, updater))
        return self

    def resolve(self, item_name: str) -> ItemUpdater:
        """Resolve a estrategia adequada para um nome de item.

        Args:
            item_name: Nome do item a resolver.

        Returns:
            O ItemUpdater correspondente, ou o updater default se
            nenhum nome ou predicado casar.
        """
        if item_name in self._updaters_by_name:
            return self._updaters_by_name[item_name]
        for predicate, updater in self._predicate_updaters:
            if predicate(item_name):
                return updater
        return self._default_updater


def build_default_registry() -> UpdaterRegistry:
    """Constroi o registry padrao da aplicacao.

    Inclui as regras conhecidas do kata (Aged Brie, Sulfuras, Backstage
    passes, Conjured) e NormalItemUpdater como default.

    Returns:
        Registry pronto para uso, podendo ainda ser estendido pelo
        chamador via ``UpdaterRegistry.register`` antes de injetar em
        GildedRose.
    """
    registry = UpdaterRegistry(default_updater=NormalItemUpdater())
    registry.register(AGED_BRIE, AgedBrieUpdater())
    registry.register(SULFURAS, SulfurasUpdater())
    registry.register(BACKSTAGE_PASSES, BackstagePassesUpdater())
    registry.register_by_predicate(is_conjured, ConjuredItemUpdater())
    return registry
