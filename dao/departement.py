from overrides import overrides

from extensions import mongo
from .enumeration import Enumeration

class Departement(Enumeration):

    @classmethod
    @overrides
    def get_collection(cls):
        return mongo.departements
