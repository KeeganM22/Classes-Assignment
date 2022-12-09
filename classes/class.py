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
        self.joined = '_'.join(self.drInfo)
        
        return self.joined
        
    def enterDrInfo(self):
        ## process for entering in a new dr
        self.ID = input("Enter doctor's ID:")
        self.drInfo.append(self.ID)
        self.Name = input("Enter doctor's name:")
        self.drInfo.append(self.Name)
        self.Specialization = input("Enter specialization:")
        self.drInfo.append(self.Specialization)
        self.Qualification = input("Enter qualification:")
        self.drInfo.append(self.Qualification)
        self.workingTime = input("Enter working hours: (7am to 10pm)")
        self.drInfo.append(self.workingTime)
        self.RoomNumber = input("Enter room number:")
        self.drInfo.append(self.RoomNumber)
        
        return self.drInfo
            
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
        for x in [0]:
            head = self.drFile[x]
            print(head.replace("_", " "))
        print(self.result.replace("_", " "))
        
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
        split = (x.replace("_", " ") for x in self.drFile)
        for x in split:
            print(x)

    def writeListOfDoctorsToFile(self):
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


