"""
Hospital Records Keeper

1.Add Patient
2.View All Patient
3.Search Patient by ID
4.Search Patient by Name
5.Update Patient
6.Delete Patient
7.Count Total Patients
8.Search Patient by Disease
9.Sort Patient by Name
10.Delete All Records
0.Exit
"""
import pickle
import os

def AddPatient():
    file=open("Hospital.Records",'ab')
    ID=input("Enter Patient ID: ")
    Name=input("Enter Patient Name: ")
    Address=input("Enter Address: ")
    Age=input("Enter Age: ")
    Phone=input("Enter Phone Number: ")
    Disease=input("Enter Disease: ")
    DOJ=input("Enter Date of Joining: ")

    Record=[ID,Name,Address,Age,Phone,Disease,DOJ]
    pickle.dump(Record,file)

    print("\n\t Patient Added Successfully")
    file.close()
    input("\n\t Press Enter to Continue...")

def ViewAllPatient():
    try:
        file=open("Hospital.Records",'rb')
        print("\t Here is your all patient details")

        while True:
            Record=pickle.load(file)

            print("\n\t Patient ID        :",Record[0])
            print("\t Patient Name      :",Record[1])
            print("\t Patient Address   :",Record[2])
            print("\t Patient Age       :",Record[3])
            print("\t Patient Phone     :",Record[4])
            print("\t Patient Disease   :",Record[5])
            print("\t Patient DOJ       :",Record[6])
            print("\t---------------------------")

    except:
        print("\t End of records")

        file.close()
        input("\n\t Press Enter to continue...")

def SearchPatientByID():
    ID = input("Enter Patient ID to search: ")

    try:
            file= open("Hospital.Records", 'rb')
            while True:
                Record = pickle.load(file)
                if Record[0] == ID:
                    print(f"""
ID        : {Record[0]}
Name      : {Record[1]}
Address   : {Record[2]}
Age       : {Record[3]}
Phone     : {Record[4]}
Disease   : {Record[5]}
DOJ       : {Record[6]}
-------------------------
""")
                    
                    print("Patient Record Found")
                    break

    except :
        print("Enter Correct Patient ID")
        
    file.close()
    input("\n\t Press Enter to Continue...")

def SearchPatientByName():
    Name=input("Enter Patient Name to search: ")

    try:
        file=open("Hospital.Records",'rb')
        while True:
            Record=pickle.load(file)
            if Record[1].lower()==Name.lower():
                print(f"""
ID        : {Record[0]}
Name      : {Record[1]}
Address   : {Record[2]}
Age       : {Record[3]}
Phone     : {Record[4]}
Disease   : {Record[5]}
DOJ       : {Record[6]}
-------------------------
""")
                print("Patient Record Found")
                break
    except :
        print("Enter Correct Patient Name")

    file.close()
    input("\n\t Press Enter to Continue...")
    

def UpdatePatient():
    ID = input("Enter Patient ID to update: ")
    found = False
    
    file = open("Hospital.Records", 'rb')
    temp = open("temp.dat", 'wb')

    try:
        while True:
            Record = pickle.load(file)
            if Record[0] == ID:
                print("Old Record:", Record)
                Record[1] = input("Enter New Name: ")
                Record[2] = input("Enter New Address: ")
                Record[3] = input("Enter New Age: ")
                Record[4] = input("Enter New Phone Number: ")
                Record[5] = input("Enter New Diseases: ")
                Record[6] = input("Enter New DOJ: ")

                found=True
            pickle.dump(Record, temp)

    except  :
        file.close()
        temp.close()

    if found :
        os.remove("Hospital.Records")
        os.rename("temp.dat", "Hospital.Records")
        print("\n\t Patient Updated Successfully")
    else:
        os.remove("temp.dat")
        print("\n\t Patient Not Found")
    
    print("\n\t Press Enter to Continue...")

def DeletePatient():
    ID = input("Enter Patient ID to delete: ")
    found = False
    file = open("Hospital.Records", 'rb')
    temp = open("temp.dat", 'wb')

    try:
        while True:
            Record = pickle.load(file)
            if Record[0]!= ID:
                pickle.dump(Record, temp)
            else:
                found = True

    except :
        file.close()
        temp.close()

    os.remove("Hospital.Records")
    os.rename("temp.dat","Hospital.Records")

    if found:
        print("Patient Deleted")
    else:
        print("Patient Not Found")
def CountTotalPatient():

    count = 0
    file=open("Hospital.Records",'rb')

    try:
        while True:
            pickle.load(file)
            count=count + 1
    except:
        pass

    print("Total Patient:",count)

def SearchPatientByDisease():
    Disease=input("Enter Disease: ")
    found=False
    file=open("Hospital.Records",'rb')

    try:
        while True:
            Record=pickle.load(file)
            if Record[5].lower()==Disease.lower():
                print(f"""
ID        : {Record[0]}
Name      : {Record[1]}
Address   : {Record[2]}
Age       : {Record[3]}
Phone     : {Record[4]}
Disease   : {Record[5]}
DOJ       : {Record[6]}
-------------------------
""")
                found=True
            
    except :
        print("Here Are All Patient Records")
    
    if not found:
        print("No Patient Found With This Diesease")

    file.close()
    input("\n\t Press Enter to Continue...")
        
def SortPatientByName():
    data=[]

    file=open("Hospital.Records",'rb')

    try:
       while True:
           data.append(pickle.load(file))

    except:
        pass

    data.sort(key=lambda x:x[1])

    for record in data:
        print(record)

def DeleteAllRecords():
    confirm=input("Are you sure?(Yes/No):")

    if confirm.lower()=="yes":
        open("Hospital.Records",'wb').close()
        print("All Records Deleted")
    else:
        print("Operation Cancelled")
#Dashboard
while True:
    
    print("\n\t ***** Hospital Records Keeper")
    print('''
    1.Add Patient
    2.View All Patient
    3.Search Patient by ID
    4.Search Patient by Name
    5.Update Patient
    6.Delete Patient
    7.Count Total Patients
    8.Search Patient by Disease
    9.Sort Patient by Name
    10.Delete All Records
    0.Exit'''
    )
    ch=int(input("Enter your choice: "))
    if ch==0:
        print("\n\t\t Exit!")
        break
    elif ch==1:
        AddPatient()
    elif ch==2:
        ViewAllPatient()
    elif ch==3:
        SearchPatientByID()
    elif ch==4:
        SearchPatientByName()
    elif ch==5:
        UpdatePatient()
    elif ch==6:
        DeletePatient()
    elif ch==7:
        CountTotalPatient()
    elif ch==8:
        SearchPatientByDisease()
    elif ch==9:
        SortPatientByName()
    elif ch==10:
        DeleteAllRecords()
    else:
        print("\n\t Wrong Entered\n\t Try Again!") 
    

