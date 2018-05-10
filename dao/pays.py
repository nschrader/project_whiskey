from overrides import overrides

from extensions import mongo
from .entity import Entity

class Pays(Entity):

    def __init__(self, **entries):
        self.nom = None
        self.continent = None
        self.climat = None
        self.culture = None
        self.vie_pratique = None
        self.tourisme = None
        self.universites = None
        Entity.__init__(self, **entries)

    @classmethod
    @overrides
    def get_collection(cls):
        return mongo.pays
