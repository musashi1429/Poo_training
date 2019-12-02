from main import *

#create class for def town and number town.
class City :
#Construct.
    def __init__(self, ville, departement):
        self.ville = ville
        self.departement = departement
#Method for see where we are.
    def showlocation(self):
        print("la ville est {}".format(self.ville),"et le departement est {}".format(self.departement))
#Method for change our location .
    def changelocation(self,ville,departement):
        self.ville = ville
        self.departement = departement
