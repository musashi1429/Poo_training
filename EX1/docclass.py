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
        self.departement =



villeactuelle = City("Paris",75)
villeactuelle.showlocation()

villeactuelle = City("Roubaix",59)
villeactuelle.showlocation()

villeactuelle = City("lyon",69)
villeactuelle.showlocation()

villeactuelle = City("Marseille",13)
villeactuelle.showlocation()

villeactuelle = City("rouen",86)
villeactuelle.showlocation()

villeactuelle.changelocation("Marseille",13)
villeactuelle.showlocation()
