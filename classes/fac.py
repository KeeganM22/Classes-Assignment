class facilities:
    def __init__(self, facilityName):
        self.facilityName = facilityName

    def addFacility(self):
        self.facilityName = input("what is the name of this new facility?")

        return self.facilityName

    def writeListOffacilitiesToFile(self):
        with open("Project Data/files/facilities.txt", "a") as f:
            f.write("\n")
        with open("Project Data/files/facilities.txt", "a") as f:
            f.write(self.facilityName)
            

    def displayFacilities(self):
        facilitiesList = open("Project Data/files/facilities.txt").read().splitlines()
        for x in facilitiesList:
            print(x)

test = facilities("test")
inp = 1
while int(inp) < 6:
    print("facilities menu \n 1 - Display facilities list \n 2 - add facility \n 3 - back to main menu")
    inp = input()
    if int(inp) == 1:
        test.displayFacilities()
    elif int(inp) == 2:
        test.addFacility()
        test.writeListOffacilitiesToFile()
