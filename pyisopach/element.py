import json
import numpy as np
from .periodic_table import get_periodic_table

class Element(object):

    def __init__(self, symbol, count):
        self.symbol = symbol
        self._periodic_table = get_periodic_table()[symbol]
        self.count = count

    @property
    def molecular_weight(self):
        return self.atomic_weight * float(self.count)

    @property
    def isotopic_ratios(self):
        return self._periodic_table["isotopic_ratio"]

    @property
    def atomic_charge(self):
        return self._periodic_table["atomic_charge"]

    @property
    def atomic_weight(self):
        isotopic_weight = self.isotopic_weight
        ratios = self._periodic_table["isotopic_ratio"]
        return float(np.matrix(ratios) * np.transpose(np.matrix(isotopic_weight)))

    @property
    def isotopic_weight(self):
        return self._periodic_table["isotopic_weight"]
