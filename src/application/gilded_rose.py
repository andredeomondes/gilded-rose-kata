# -*- coding: utf-8 -*-
from src.domain.item_updaters import resolve_updater


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            resolve_updater(item.name).update(item)
