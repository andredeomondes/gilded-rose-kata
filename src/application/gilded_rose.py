# -*- coding: utf-8 -*-
"""Camada de aplicacao: orquestra a atualizacao diaria de um inventario
de itens, delegando a regra de cada item ao seu ItemUpdater (Strategy).
"""
from typing import List, Optional

from src.domain.item import Item
from src.domain.updaters import UpdaterRegistry, build_default_registry


class GildedRose(object):
    """Inventario da loja.

    Atualiza ``quality``/``sell_in`` de todos os itens uma vez por dia.
    Depende apenas da abstracao UpdaterRegistry (DIP) -- nunca decide
    diretamente a regra de nenhum item.

    O registry pode ser injetado via construtor (ex. em testes, para
    registrar regras customizadas sem alterar nenhum arquivo de
    producao); quando omitido, usa build_default_registry().

    Attributes:
        items: Itens do inventario, mutados in-place a cada chamada de
            update_quality.
    """

    def __init__(
        self,
        items: List[Item],
        updater_registry: Optional[UpdaterRegistry] = None,
    ) -> None:
        """Inicializa o inventario.

        Args:
            items: Itens do inventario, mutados in-place a cada chamada
                de update_quality.
            updater_registry: Registry de estrategias a usar. Se None,
                usa o registry default do dominio.
        """
        self.items: List[Item] = items
        self._updater_registry: UpdaterRegistry = (
            updater_registry or build_default_registry()
        )

    def update_quality(self) -> None:
        """Avanca um dia para todos os itens do inventario.

        Para cada item, resolve seu ItemUpdater no registry e aplica a
        atualizacao de quality/sell_in correspondente.
        """
        for item in self.items:
            updater = self._updater_registry.resolve(item.name)
            updater.update(item)
