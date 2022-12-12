class labs:
    def __init__(self, labName, cost):
        self.labName = labName
        self.cost = cost

    def enterLabInfo(self):
        self.labname = input("enter lab name: ")
        self.cost = input("enter cost: ")

        
    def formatLabInfo(self):
        self.formated = str(self.labname) + "_" + str(self.cost)
        return self.formated
        
    def readLabFile(self):
        self.labFile = open("Project Data/files\laboratories.txt").read().splitlines()
        return self.labFile
    def addLabToFile(self):
        with open("Project Data/files\laboratories.txt", "a") as f:
            f.write("\n")
        with open("Project Data/files\laboratories.txt", "a") as f:
            f.write(self.formated)

    def writeListOflabsToFile(self):
        with open("Project Data/files\laboratories.txt", "w") as f:
            f.write(self.labFile)
            

    def displayLabs(self):
        
        text = "{name:<30}{cost:30}"
        for x in self.labFile:
            split = x.split("_")
            self.labName = split[0]
            self.cost = split[1]
            print(text.format(name=self.labName,cost=self.cost))
        

lab = labs(1, 1)

user = 1
while user <3:
    print("Labs menu \n 1 - Display labs list \n 2 - add lab \n 3 - back to main menu")
    user = int(input())
    if user == 1:
        lab.readLabFile()
        lab.displayLabs()
    elif user == 2:
        lab.enterLabInfo()
        lab.formatLabInfo()
        lab.addLabToFile()