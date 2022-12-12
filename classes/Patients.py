class patient:
    drInfo = []
    def __init__(self, pid, Name, disease, gender, age):
        self.pid = pid
        self.Name = Name
        self.disease = disease
        self.gender = gender
        self.age = age
        
    
    def formatPatientInfo(self):
        ## makes new enterys on the txt file look like the pre existing ones
        self.joined = self.pid + "_" + self.Name + "_" + self.disease + "_" + self.gender + "_" + self.age
        
        return self.joined
        
    def enterPatientInfo(self):
        ## process for entering in a new dr
        self.pid = input("Enter patient's ID: ")
        self.Name = input("Enter patient's name: ")
        self.disease = input("Enter patient's disease: ")
        self.gender = input("Enter patient's gender: ")
        self.age = input("Enter patient's age: ")
        
        
            
    def addPatientToFile(self):
        ## once done enter dr info, it will add it with this
        with open("Project Data/files\patients.txt", "a") as f:
            f.write('\n')
        with open("Project Data/files\patients.txt", "a") as f:
            f.write(self.joined)

    def readPatientsFile(self):
        ## reads the dr info and fills it out by a list
        self.patFile = open("Project Data/files\patients.txt").read().splitlines()
        
        return self.patFile
        
    def searchPatientById(self):
        ## checks if the dr exists and reads the text file and outputs the given dr in one line by id
        search = input("search ID:")
        for x in self.patFile:
            if search in x[:4]:
                self.result = x
                return self.result

    def searchPatientByName(self):
        ## checks if the dr exists and reads the text file and outputs the given dr in one line by name
        search = input("Search Name:")
        for x in self.patFile:
            if search in x:
                self.result = x
                return self.result
            

    def displayPatientInfo(self):
        ## input id of dr and it will put out all the dr's information on separate lines
        txt = "{pid:<10}{name:20}{disease:15}{gender:20}{age:20}"
        y = self.patFile[0]
        z = y.split("_")
        self.pid = z[0]
        self.Name = z[1]
        self.disease = z[2]  
        self.gender = z[3]  
        self.age = z[4]  
        print(txt.format(pid=self.pid,name=self.Name,disease=self.disease,gender=self.gender,age=self.age))
        for x in self.patFile:
            if x == self.result:
                y = x.split("_")
                self.pid = y[0]
                self.Name = y[1]
                self.disease = y[2]  
                self.gender = y[3]  
                self.age = y[4]  
                print(txt.format(pid=self.pid,name=self.Name,disease=self.disease,gender=self.gender,age=self.age))
        
    def editPatientInfo(self):
        ## edits dr's info of the one they input their id as
        self.pid = input("Enter new ID: ")
        self.Name = input("Enter new name: ")
        self.disease = input("Enter new disease: ")
        self.gender = input("Enter new gender: ")
        self.age = input("Enter new age: ")


        for x in self.patFile:
            if self.result == x:
                self.patFile.remove(x)

    def displayPatientList(self):
        ## genaral list of all the text 
        txt = "{pid:<10}{name:20}{disease:15}{gender:20}{age:20}"
        for x in self.patFile:
            y = x.split("_")
            self.pid = y[0]
            self.Name = y[1]
            self.disease = y[2]  
            self.gender = y[3]  
            self.age = y[4]  
            print(txt.format(pid=self.pid,name=self.Name,disease=self.disease,gender=self.gender,age=self.age))

    def writeListOfPatientsToFile(self):
        ## rewrites the whole list
        self.patFile.append(self.joined)
        with open("Project Data/files\patients.txt", "w") as f:
            f.write('\n'.join(self.patFile))

test = patient(22, "Keegan", "Diabeties", "Male", 19)
inp = 1
while int(inp) < 6:
    print("Patient menu \n 1 - Display patient list \n 2 - Search for patient by ID \n 3 - Search for patient by name \n 4 - Add patient \n 5 - Edit patient info \n 6 - Back to the Main Menu")
    inp = input()
    if int(inp) == 1:
        test.readPatientsFile()
        test.displayPatientList()
    elif int(inp) == 2:
        test.readPatientsFile()
        test.searchPatientById()
        test.displayPatientInfo()
    elif int(inp) == 3:
        test.readPatientsFile()
        test.searchPatientByName()
        test.displayPatientInfo()
    elif int(inp) == 4:
        test.enterPatientInfo()
        test.formatPatientInfo()
        test.addPatientToFile()
    elif int(inp) == 5:
        test.readPatientsFile()
        test.searchPatientById()
        test.editPatientInfo()
        test.formatPatientInfo()
        test.writeListOfPatientsToFile()