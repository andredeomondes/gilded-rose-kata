# -*- coding: utf-8 -*-
# Copia exata da classe Item do legado (legacy/gilded_rose.py).
# Restricao obrigatoria do trabalho: esta classe nao pode ser alterada.


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
