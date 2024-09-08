class MyCar:
    def __init__(self, year, model):
        self.year= year
        self.model = model
    def NewYear(self,year):
        self.year = int(year)
    def getYear(self):
        return self.year

MyNewCAr= MyCar(2023, "Maybach")
print(MyNewCAr.getYear())

