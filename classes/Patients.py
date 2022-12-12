class patient:
    drInfo = []
    def __init__(self, pid, Name, disease, gender, age):
        self.pid = pid
        self.Name = Name
        self.disease = disease
        self.gender = gender
        self.age = age
        
    
    def formatPatientInfo(self):
        self.joined = self.pid + "_" + self.Name + "_" + self.disease + "_" + self.gender + "_" + self.age
        
        return self.joined
        
    def enterPatientInfo(self):
        self.pid = input("Enter patient's ID: ")
        self.Name = input("Enter patient's name: ")
        self.disease = input("Enter patient's disease: ")
        self.gender = input("Enter patient's gender: ")
        self.age = input("Enter patient's age: ")
        
        
            
    def addPatientToFile(self):
        with open("classes/Project Data/files\patients.txt", "a") as f:
            f.write('\n')
        with open("classes/Project Data/files\patients.txt", "a") as f:
            f.write(self.joined)

    def readPatientsFile(self):
        self.patFile = open("classes/Project Data/files\patients.txt").read().splitlines()
        
        return self.patFile
        
    def searchPatientById(self):
        search = input("search ID:")
        for x in self.patFile:
            if search in x[:4]:
                self.result = x
                return self.result

    def searchPatientByName(self):
        search = input("Search Name:")
        for x in self.patFile:
            if search in x:
                self.result = x
                return self.result
            

    def displayPatientInfo(self):
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
        self.pid = input("Enter new ID: ")
        self.Name = input("Enter new name: ")
        self.disease = input("Enter new disease: ")
        self.gender = input("Enter new gender: ")
        self.age = input("Enter new age: ")


        for x in self.patFile:
            if self.result == x:
                self.patFile.remove(x)

    def displayPatientList(self):
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
        self.patFile.append(self.joined)
        with open("classes/Project Data/files\patients.txt", "w") as f:
            f.write('\n'.join(self.patFile))

