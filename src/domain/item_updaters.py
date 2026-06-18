# -*- coding: utf-8 -*-
"""Estrategias de atualizacao diaria de quality/sell_in, uma por tipo de
item. Substitui o metodo monolitico update_quality (ver
docs/diagnostico_tecnico.md) por classes pequenas, cada uma testavel
isoladamente (RNF04/RNF05/RNF06 em docs/requisitos.md).
"""
from src.domain.item_names import AGED_BRIE, SULFURAS, BACKSTAGE_PASSES

MIN_QUALITY = 0
MAX_QUALITY = 50


class ItemUpdater:
    def update(self, item):
        raise NotImplementedError


class NormalItemUpdater(ItemUpdater):
    def update(self, item):
        item.quality = max(MIN_QUALITY, item.quality - 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = max(MIN_QUALITY, item.quality - 1)


class AgedBrieUpdater(ItemUpdater):
    def update(self, item):
        item.quality = min(MAX_QUALITY, item.quality + 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = min(MAX_QUALITY, item.quality + 1)


class SulfurasUpdater(ItemUpdater):
    def update(self, item):
        pass


class BackstagePassesUpdater(ItemUpdater):
    def update(self, item):
        item.quality = min(MAX_QUALITY, item.quality + 1)
        if item.sell_in < 11:
            item.quality = min(MAX_QUALITY, item.quality + 1)
        if item.sell_in < 6:
            item.quality = min(MAX_QUALITY, item.quality + 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0


_UPDATERS_BY_NAME = {
    AGED_BRIE: AgedBrieUpdater(),
    SULFURAS: SulfurasUpdater(),
    BACKSTAGE_PASSES: BackstagePassesUpdater(),
}

_DEFAULT_UPDATER = NormalItemUpdater()


def resolve_updater(item_name):
    return _UPDATERS_BY_NAME.get(item_name, _DEFAULT_UPDATER)
