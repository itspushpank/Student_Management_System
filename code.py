data={}

def rollValidation():
    while True:
        roll=input("Enter the roll number :").strip()
        if roll not in data.keys():
            return roll
        else:
            print("\nThe Roll number already exist!\nEnter another Roll no!\n")

def rollValidation2():
    while True:
        roll=input("Enter the roll number :").strip()
        if roll in data.keys():
            return roll
        else:
            print("\nRoll no does not exist!\nPlease enter a valid roll number!\n")

def updater(roll):
    lst=list(data[roll]["marks"].values())
    lst = [x if x is not None else 0.0 for x in lst] 
    data[roll]["average"]=sum(lst)/len(lst)
    grade="A+" if 100>=data[roll]["average"]>=90 else "A" if 90>data[roll]["average"]>=80 else "B+" if 80>data[roll]["average"]>=70 else "B" if 70>data[roll]["average"]>=60 else "C" if 60>data[roll]["average"]>=50 else "D" if 50>data[roll]["average"]>=40 else "F"
    data[roll]["grade"]=grade

def marksValidation(roll):
    
    pass

def addStudent(roll):
    # roll=int(input("Enter the Roll Number: "))
    data[roll]={}
    data[roll]["name"]=input("\nEnter Name: ").strip()
    data[roll]["branch"]=input("Enter Branch: ").strip()
    data[roll]["semester"]=input("Enter Semester: ").strip()
    listo=input("Enter courses (comma-separated): ").split(",")
    # data[roll]["courses"]=input("Enter courses (comma-separated): ").split(",")
    data[roll]["courses"]=[x.strip() for x in listo]
    # print(data[roll]["courses"])
    data[roll]["grade"]=None
    data[roll]["average"]=None
    print("\nStudent added successfully!")
    print("\n")

def recordMarks(roll):
    # roll=input("Enter the Roll Number: ")
    print(f"\nStudent: {data[roll]["name"]}\n")

    data[roll]["marks"]={}
    some=list(data[roll]["courses"])
    lst=[]
    while True:
        try:           
            for i in data[roll]["courses"]:
                x=True
                while x:
                    j=int(input(f"Enter marks for {i}:"))
                    if 0<=j<=100:
                        lst.append(j)
                        x=False
                    else:
                        print("Enter a Number Between (0-100)")
            data[roll]["marks"]=dict(zip(data[roll]["courses"],lst))
            data[roll]["average"]=sum(lst)/len(lst)
            # print(data[roll]["courses"])
            break
        except:
            print("Invalid Input!\n Please enter an Integer marks between (0-100)")
    grade="A+" if 100>=data[roll]["average"]>=90 else "A" if 90>data[roll]["average"]>=80 else "B+" if 80>data[roll]["average"]>=70 else "B" if 70>data[roll]["average"]>=60 else "C" if 60>data[roll]["average"]>=50 else "D" if 50>data[roll]["average"]>=40 else "F"
    data[roll]["grade"]=grade
    print("\nMarks recorded successfully!\n")
    print(f"Average: {data[roll]["average"]:.2f}%")
    print(f"Grade: {grade}")
    print("\n")
            

    

def displayAllStudent():
    
    print("-"*87)
    print(f"| {'Roll No.':<12}| {'Name':<25}| {'Branch':<25}|{'Average':^9}|{'Grade':^7}|")
    print("-"*87)
    for i in data.keys():
        # test=str(round(data[i]["average"],2)) +"%"
        if data[i]["average"]==None and data[i]["grade"]==None:
            print(f"| {i:<12}| {data[i]["name"]:<25}| {data[i]["branch"]:<25}|{"----":^9}|{"----":^7}|")
        else:
            print(f"| {i:<12}| {data[i]["name"]:<25}| {data[i]["branch"]:<25}|{data[i]["average"]:^9}|{data[i]["grade"]:^7}|")
        print("-"*87)
    print("\n")

def displayIndividualStudent(roll):
    print("\n===== Student Details =====")
    print(f"Roll Number: {roll}")
    print(f"Name: {data[roll]["name"]}")
    print(f"Branch: {data[roll]["branch"]}")
    print(f"Semester: {data[roll]["semester"]}\n")
    print("Enrolled Courses and Marks:")
    for k,v in data[roll]["marks"].items():
        print(f"{k} : {v}")

    print(f"Average: {data[roll]["average"]:.2f}%")
    print(f"Grade: {data[roll]["grade"]}")
    print("\n")
    

def updateStudent(roll):
    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Branch")
    print("3. Semester")
    print("4. Add Course")
    print("5. Remove Course")
    print("6. Update Marks\n")
    choice=input("Enter choice: \n")
    match choice:
        case '1':
            data[roll]["name"]=input("Enter new name: ")
            print("Updated Successfully!")
        case '2':
            data[roll]["branch"]=input("Enter new branch: ")
            print("Updated Successfully!")
        case '3':
            data[roll]["semester"]=input("Enter new semester: ")
            print("Updated Successfully!")
        case '4':
            x=input("Enter new course to be added: ")
            data[roll]["courses"].append(x)
            data[roll]["marks"][x]=None
            print("Updated Successfully!")
        case '5':
            print("What course do you want to remove?")
            count=0
            for i in data[roll]["courses"]:
                count+=1
                print(f"{count}. {i}")
            r=int(input("\nEnter the position of the course that you want to remove : "))
            z=data[roll]["courses"].pop(r-1)
            data[roll]["marks"].pop(z)
            print("Updated Successfully!")
            updater(roll)
        case '6':
            print("Select to course of which you want to Update marks.\n")
            c=0
            for ky,vl in data[roll]["marks"].items():
                c+=1
                print(f"{c}. {ky:<10} : {vl}")
            upsub=input("Enter the name of course of which you want to Update marks  :").strip()
            # print(data[roll]["courses"])
            # if upsub in list(data[roll]["marks"].keys()):
            if upsub in data[roll]["courses"]:
                x=True
                while x:
                    try:        
                        while x:
                            j=int(input(f"Enter marks for {upsub}:"))
                            if 0<=j<=100:
                                data[roll]["marks"][upsub]=j
                                x=False
                            else:
                                print("Enter a Number Between (0-100)")
                    except:
                        print("Invalid Input!\n Please enter an Integer marks between (0-100)")
            else:
                print("The Course does not exist!\nEnter a Course that is Opt by the Student!!!")
            # for k in data[roll]["marks"].keys():
            #     x=True
            #     while x:
            #         try:        
            #             while x:
            #                 j=int(input(f"Enter marks for {k}:"))
            #                 if 0<=j<=100:
            #                     data[roll]["marks"][k]=j
            #                     x=False
            #                 else:
            #                     print("Enter a Number Between (0-100)")
            #         except:
            #             print("Invalid Input!\n Please enter an Integer marks between (0-100)")
            print("Updated Successfully!")
            updater(roll)
        case _:
            print("Invalid Choice ")
            print("Update Not Successful!")

def deleteStudent(roll):
    print(f"Student: {data[roll]["name"]}")
    choice=input("Are you sure you want to delete?  (yes/no) :")
    if choice=="yes":
        data.pop(roll)
        print("Student deleted successfully!")
    else:
        print("Cancelled!!!")
    

def searchBYbranch():
    branch=input("Enter Branch: ")
    print("-"*60)
    print(f"| {'Roll No.':<12}| {'Name':<25}|{'Average':^9}|{'Grade':^7}|")
    print("-"*60)
    count=0
    for i in data.keys():
        if data[i]["branch"]==branch:
            if data[i]["average"]==None and data[i]["grade"]==None:
                print(f"| {i:<12}| {data[i]["name"]:<25}|{"----":^9}|{"----":^7}|")
            else:
                print(f"| {i:<12}| {data[i]["name"]:<25}|{data[i]["average"]:^9}|{data[i]["grade"]:^7}|")
            print("-"*60)
            count+=1
    print(f"\nTotal students in {branch}: {count}")



while True:
    print("\n\n===== Student Management System =====")
    print("1. Add New Student")
    print("2. Record Marks")
    print("3. Display All Students")
    print("4. Display Individual Student")
    print("5. Update Student Information")
    print("6. Delete Student Record")
    print("7. Search by Branch")
    print("8. Exit")
    print()
    

    choice=input("Enter your choice (1-8):")
    
    match choice:
        case '1':
            addStudent(rollValidation())
        case '2':
            recordMarks(rollValidation2())
        case '3':
            displayAllStudent()
        case '4':
            displayIndividualStudent(rollValidation2())
        case '5':
            updateStudent(rollValidation2())
        case '6':
            deleteStudent(rollValidation2())
        case '7':
            searchBYbranch()
        case '8':
            print("====Thanks for using Student management System====")
            break
        case _:
            print("====Invalid choice====\n====Please enter a valid Choice (1-8)====\n")








