from app.modules.level_1.class_user import *

class Centre():

    def __init__(self, centreID, abn, name, _type, phone, location):
        self.centreID = centreID
        self.abn = abn
        self.name = name.capitalize()
        self._type = _type
        self.phone = phone
        self.location = location

    def set_abn(self, abn):
        self.abn = abn

    def set_name(self, name):
        self.name = name.capitalize()

    def set_type(self, _type):
        self.location = location

    def get_rating(self):
        system = System
        list_ratings = system.get_ratings()
        my_ratings = []
        if not list_ratings:
            return []
        for r in list_ratings:
            if r.entityID == self.centreID:
                my_ratings.append(r.rating)
        if not my_ratings:
            return []
        return "{0:.2f}".format(statistics.mean(my_ratings))

    def get_providers(self):
        system = System
        dict_users = system.get_users()
        list_employment = system.get_employment()
        c_providers = []
        for r in list_employment:
            if r.centre.centreID == self.centreID:
                c_providers.append(r.provider)
        return c_providers
        
    def __str__(self):
        return str(self.name + ", centreID: " + self.centreID)