class doctors:
    drInfo = []
    def __init__(self, ID, Name, Specialization, WorkingTime, Qualification, RoomNumber):
        self.ID = ID
        self.Name = Name
        self.Specialization = Specialization
        self.workingTime = WorkingTime
        self.Qualification = Qualification
        self.RoomNumber = RoomNumber
    
    def formatDrInfo(self):
        ## makes new enterys on the txt file look like the pre existing ones
        self.joined = self.ID + "_Dr. " + self.Name + "_" + self.workingTime + "_" + self.Specialization + "_" + self.Qualification + "_" + self.RoomNumber
        
        return self.joined
        
    def enterDrInfo(self):
        ## process for entering in a new dr
        self.ID = input("Enter doctor's ID: ")
        self.Name = input("Enter doctor's name: ")
        self.Specialization = input("Enter specialization: ")
        self.Qualification = input("Enter qualification: ")
        self.workingTime = input("Enter working hours: (7am to 10pm) ")
        self.RoomNumber = input("Enter room number: ")
        
            
    def addDrToFile(self):
        ## once done enter dr info, it will add it with this
        with open("Project Data/files\doctors.txt", "a") as f:
            f.write('\n')
        with open("Project Data/files\doctors.txt", "a") as f:
            f.write(self.joined)

    def readDoctorsFile(self):
        ## reads the dr info and fills it out by a list
        self.drFile = open("Project Data/files\doctors.txt").read().splitlines()
        
        return self.drFile
        
    def searchDoctorById(self):
        ## checks if the dr exists and reads the text file and outputs the given dr in one line by id
        search = input("search ID:")
        for x in self.drFile:
            if search in x[:4]:
                self.result = x
                return self.result

    def searchDoctorByName(self):
        ## checks if the dr exists and reads the text file and outputs the given dr in one line by name
        search = input("Search Name:")
        for x in self.drFile:
            if search in x:
                self.result = x
                return self.result
            

    def displayDoctorInfo(self):
        ## input id of dr and it will put out all the dr's information on separate lines
        txt = "{id:<10}{name:20}{time:15}{spec:20}{qual:20}{room:10}"
        y = self.drFile[0]
        z = y.split("_")
        self.IDh = z[0]
        self.Nameh = z[1]
        self.workingTimeh = z[2]  
        self.Specializationh = z[3]  
        self.Qualificationh = z[4]  
        self.RoomNumberh = z[5]
        print(txt.format(id=self.IDh,name=self.Nameh,time=self.workingTimeh,spec=self.Specializationh,qual=self.Qualificationh,room=self.RoomNumberh))
        for x in self.drFile:
            if x == self.result:
                y = x.split("_")
                self.ID = y[0]
                self.Name = y[1]
                self.workingTime = y[2]  
                self.Specialization = y[3]  
                self.Qualification = y[4]  
                self.RoomNumber = y[5]  
                print(txt.format(id=self.ID,name=self.Name,time=self.workingTime,spec=self.Specialization,qual=self.Qualification,room=self.RoomNumber))
        
    def editDoctorInfo(self):
        ## edits dr's info of the one they input their id as
        self.ID = input("Enter new ID: ")
        self.drInfo.append(self.ID)
        self.Name = input("Enter new name: ")
        self.drInfo.append(self.Name)
        self.Specialization = input("Entert new specialization: ")
        self.drInfo.append(self.Specialization)
        self.Qualification = input("Enter new qualifcation: ")
        self.drInfo.append(self.Qualification)
        self.workingTime = input("Enter new working hours: (7am to 10pm) ")
        self.drInfo.append(self.workingTime)
        self.RoomNumber = input("Enter new room number:")
        self.drInfo.append(self.RoomNumber)

        for x in self.drFile:
            if self.result == x:
                self.drFile.remove(x)

            
        return self.drInfo

    def displayDoctorList(self):
        ## genaral list of all the text 
        txt = "{id:<10}{name:20}{time:15}{spec:20}{qual:20}{room:10}"
        for x in self.drFile:
            y = x.split("_")
            self.ID = y[0]
            self.Name = y[1]
            self.workingTime = y[2]  
            self.Specialization = y[3]  
            self.Qualification = y[4]  
            self.RoomNumber = y[5]  
            print(txt.format(id=self.ID,name=self.Name,time=self.workingTime,spec=self.Specialization,qual=self.Qualification,room=self.RoomNumber))

    def writeListOfDoctorsToFile(self):
        ## rewrites the whole list
        self.drFile.append(self.joined)
        with open("Project Data/files\doctors.txt", "w") as f:
            f.write('\n'.join(self.drFile))

## first open the main menu for other classes
## enters loop to re run this class over and over
## when in dr displays options to chose from
##  -- 1 display doctor list
##  ---- first for each line in the txt file
##  ------ uses readDoctorsFile to read from the text file and turn it into a list
##  ------ use displayDoctorList, this takes each of the created lists and prints them with the writelines function
##  -- 2 search for dr ID
##  ---- uses searchDoctorById to find if the dr exists
##  ------ uses readDoctorsFile to read from the text file and turn it into a list
##  ------ uses DisplayDoctorInfo to display the list from readDoctorsFile into a print
##  -- 3 search for dr Name
##  ---- uses searchDoctorByName to find if the dr exists
##  ------ uses readDoctorsFile to read from the text file and turn it into a list
##  ------ uses DisplayDoctorInfo to display the list from readDoctorsFile into a print
##  -- 4 Add doctor
##  ---- uses enterDrInfo to process all the new information and add it to a list
##  ------ uses formatDrInfo to make it look like other entries in the txt file
##  ------ uses addDrToFile to add the new formatted information onto the file on a new line
##  -- 5 edit dr info 
##  ---- uses findDrById to find the dr to edit
##  ------ uses editDrInfo to process all of the new edits
##  -------- uses formatDrInfo to make it look like other entries in the txt file
##  -------- uses writeListOfDoctorsToFile to edit the list
##  -- 6 back to main menu
##  ---- passes the loop to exit the classes 


test = doctors(12, "mclean", "EMT", "1 to 1", "PHD", 12)

## testing editing, remove comment to run 
##test.readDoctorsFile()
##test.searchDoctorById()
##test.editDoctorInfo()
##test.formatDrInfo()
##test.writeListOfDoctorsToFile()

## testing adding, remove comment to run
##test.enterDrInfo()
##test.formatDrInfo()
##test.addDrToFile()

## testing print list remove comment to run
##test.readDoctorsFile()
##test.displayDoctorList()

## testing search for id, remove comment to run
##test.readDoctorsFile()
##test.searchDoctorById()
##test.displayDoctorInfo()

## testing search for name, remove comment to run
##test.readDoctorsFile()
##test.searchDoctorByName()
##test.displayDoctorInfo()

inp = 1
while int(inp) < 6:
    print("doctors menu \n 1 - Display Doctors list \n 2 - Search for doctor by ID \n 3 - Search for doctor by name \n 4 - Add doctor \n 5 - Edit doctor info \n 6 - Back to the Main Menu")
    inp = input()
    if int(inp) == 1:
        test.readDoctorsFile()
        test.displayDoctorList()
    elif int(inp) == 2:
        test.readDoctorsFile()
        test.searchDoctorById()
        test.displayDoctorInfo()
    elif int(inp) == 3:
        test.readDoctorsFile()
        test.searchDoctorByName()
        test.displayDoctorInfo()
    elif int(inp) == 4:
        test.enterDrInfo()
        test.formatDrInfo()
        test.addDrToFile()
    elif int(inp) == 5:
        test.readDoctorsFile()
        test.searchDoctorById()
        test.editDoctorInfo()
        test.formatDrInfo()
        test.writeListOfDoctorsToFile()

