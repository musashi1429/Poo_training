from cities import *
class Ville:
    def __init__(self,data_dic):
        self.name = None
        self.department = None
        self.country = None
        self.population = None
        self.mayor = None
        self.captital = None
        self.hydrate(data_dic)

    def hydrate(self,data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def show_information(self):
        text = "------------------\n \
        name: {}\n \
        department: {}\n \
        country: {}\n \
        population: {}\n \
        mayor: {}\n \
        captital: {}\n"
        print(text.format(self.name, self.department, self.country, self.population, self.mayor, self.captital,))





for city in cities:
    city = Ville(city)
    city.show_information()
