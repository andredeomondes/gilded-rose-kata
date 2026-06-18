# -*- coding: utf-8 -*-
"""Pacote de estrategias de atualizacao diaria de quality/sell_in.

Cada regra de item vive em seu proprio modulo (SRP); este __init__
reexporta a API publica para quem so precisa de
"from src.domain.updaters import X" em vez de importar de cada
submodulo individualmente.
"""
from src.domain.updaters.base import ItemUpdater
from src.domain.updaters.normal import NormalItemUpdater
from src.domain.updaters.aged_brie import AgedBrieUpdater
from src.domain.updaters.sulfuras import SulfurasUpdater
from src.domain.updaters.backstage_passes import BackstagePassesUpdater
from src.domain.updaters.conjured import ConjuredItemUpdater
from src.domain.updaters.registry import UpdaterRegistry, build_default_registry

__all__ = [
    "ItemUpdater",
    "NormalItemUpdater",
    "AgedBrieUpdater",
    "SulfurasUpdater",
    "BackstagePassesUpdater",
    "ConjuredItemUpdater",
    "UpdaterRegistry",
    "build_default_registry",
]
