
loop = 1

while int(loop) > 0:
    print("Welcome to Alberta Hospital (AH) Managment system \n Select from the following options, or select 0 to stop: \n 1 - Doctors \n 2 - Facilities \n 3 - Laboratories \n 4 - Patients ")
    loop = input()
    if int(loop) == 1:
        from Doctors import doctors
        doc = doctors(12, "mclean", "EMT", "1 to 1", "PHD", 12)
        docs = 1
        while int(docs) < 6:
            print("doctors menu \n 1 - Display Doctors list \n 2 - Search for doctor by ID \n 3 - Search for doctor by name \n 4 - Add doctor \n 5 - Edit doctor info \n 6 - Back to the Main Menu")
            docs = input()
            if int(docs) == 1:
                doc.readDoctorsFile()
                doc.displayDoctorList()
            elif int(docs) == 2:
                doc.readDoctorsFile()
                doc.searchDoctorById()
                doc.displayDoctorInfo()
            elif int(docs) == 3:
                doc.readDoctorsFile()
                doc.searchDoctorByName()
                doc.displayDoctorInfo()
            elif int(docs) == 4:
                doc.enterDrInfo()
                doc.formatDrInfo()
                doc.addDrToFile()
            elif int(docs) == 5:
                doc.readDoctorsFile()
                doc.searchDoctorById()
                doc.editDoctorInfo()
                doc.formatDrInfo()
                doc.writeListOfDoctorsToFile()
    if int(loop) == 2:
        from Facilities import facilities
        fac = facilities("pat")
        faci = 1
        while int(faci) < 3:
            print("facilities menu \n 1 - Display facilities list \n 2 - add facility \n 3 - back to main menu")
            faci = input()
            if int(faci) == 1:
                fac.displayFacilities()
            elif int(faci) == 2:
                fac.addFacility()
                fac.writeListOffacilitiesToFile()
    if int(loop) == 3:
        from Labs import labs
        lab = labs(1, 1)
        labi = 1
        while labi < 3:
            print("Labs menu \n 1 - Display labs list \n 2 - add lab \n 3 - back to main menu")
            labi = int(input())
            if labi == 1:
                lab.readLabFile()
                lab.displayLabs()
            elif labi == 2:
                lab.enterLabInfo()
                lab.formatLabInfo()
                lab.addLabToFile()
            elif labi == 3:
                pass
    if int(loop) == 4:
        from Patients import patient
        pat = patient(22, "Keegan", "Diabeties", "Male", 19)
        pati = 1
        while int(pati) < 6:
            print("Patient menu \n 1 - Display patient list \n 2 - Search for patient by ID \n 3 - Search for patient by name \n 4 - Add patient \n 5 - Edit patient info \n 6 - Back to the Main Menu")
            pati = input()
            if int(pati) == 1:
                pat.readPatientsFile()
                pat.displayPatientList()
            elif int(pati) == 2:
                pat.readPatientsFile()
                pat.searchPatientById()
                pat.displayPatientInfo()
            elif int(pati) == 3:
                pat.readPatientsFile()
                pat.searchPatientByName()
                pat.displayPatientInfo()
            elif int(pati) == 4:
                pat.enterPatientInfo()
                pat.formatPatientInfo()
                pat.addPatientToFile()
            elif int(pati) == 5:
                pat.readPatientsFile()
                pat.searchPatientById()
                pat.editPatientInfo()
                pat.formatPatientInfo()
                pat.writeListOfPatientsToFile()