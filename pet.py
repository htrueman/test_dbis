from animal import Animal


class Pet(Animal):
    def __init__(self, name, species):
        Animal.__init__(self, species)
        self.name = name

    def __str__(self):
        return "%s is a %s" % (self.get_name(), self.get_species())

    def get_name(self):
        return self.name


def create_pet(name, species):
    return Pet(name, species)
