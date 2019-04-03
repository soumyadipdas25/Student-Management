# -*- coding: utf-8 -*-
"""
PYTHON PROJECT ON STUDENT MANAGEMENT SYSYTEM
                    BY
Name:-SOUMYADIP DAS
Roll:-1605236
Class:-CS-3
Batch-PYTHON & PROGRAMMING
"""
list1 = []
def write_to_file(lists):
    f  = open('STUDENT.txt', 'a')
    for i in lists:
        f.write(i)
    f.close()

def details():
    name=input("Enter the first name: ")+" "
    name1=input("Enter the last name: ")+" "
    roll=input("Enter the roll number: ")+" "
    hostel=input("Enter the hostel name: ")+" "
    branch=input("Enter the branch in capital: ")+" "
    cgpa=input("Enter the CGPA: ")+" "
    ph=input("Enter the phone number: ")+"\n"
    return [roll, name, name1, hostel, branch, cgpa, ph]
def display():
    y=1
    st1=input("Enter the roll number")
    f=open("STUDENT.txt",mode="r",encoding="utf-8")
    with open("STUDENT.txt") as infile:
        for lineno,lines in enumerate(infile,1):
            list1 = lines.split()
            if list1[0] == st1:
                print("NAME:-",list1[1],list1[2])
                print("Hostel:-",list1[len(list1)-4])
                print("BRANCH:-",list1[len(list1)-3])
                print("CGPA:-",list1[len(list1)-2])
                print("Phone number:-",list1[len(list1)-1])
                y=y+1
        if y==1:
            print("NO ROLL NUMBER FOUND")
        f.close()
    
def chnum():  
     import os
     st1=input("Enter the roll number of the student whose number is to be changed:")
     f=open("STUDENT.txt", "r")
     f1=open("STUDENT1.txt","a")
     #f1=open("STUDENT1.txt",mode="w",encoding="utf-8")
     with open("STUDENT.txt") as infile:
         for lineno,lines in enumerate(infile,1):
             list1 = lines.split()
             if list1[0] == st1:
                 ph=input("Enter new phone number:")
                 list1[len(list1)-1]=ph
                 s = ""
                 for i in list1:
                     s += i + " "
                 s=s+"\n"
                 f1.write(s)
             else:
                 s = ""
                 for i in list1:
                     s += i + " "
                 s=s+"\n"
                 f1.write(s)
                 
                 
     f.close()
     f1.close()
     os.remove("STUDENT.txt")
     os.rename("STUDENT1.txt","STUDENT.txt")
     
    

def brchange():
     import os
     st1=input("Enter the roll number of the student whose branch is to be changed:")
     f1=open("STUDENT1.txt","a")
     with open("STUDENT.txt") as infile:
         for lineno,lines in enumerate(infile,1):
             list1 = lines.split()
             if st1==list1[0]:
                 if list1[len(list1)-2]>='9':
                     print("BRANCH CAN BE UPDATED")
                     br=input("Enter the new branch")
                     list1[len(list1)-3]=br
                     s = ""
                     for i in list1:
                         s += i + " "
                     s=s+"\n"
                     f1.write(s)
                 else:
                     print("CGPA less than 9 so cannot update")
                     s = ""
                     for i in list1:
                         s += i + " "
                     s=s+"\n"
                     f1.write(s)
             else:
                 s = ""
                 for i in list1:
                     s += i + " "
                 s=s+"\n"
                 f1.write(s)
     f1.close()
     os.remove("STUDENT.txt")
     os.rename("STUDENT1.txt","STUDENT.txt")
                 
def delrecord():
    import os
    st1=input("Enter the roll number of the student whose record is to be deleted:")
    f1=open("STUDENT1.txt","a")
    with open("STUDENT.txt") as infile:
        for lineno,lines in enumerate(infile,1):
            list1 = lines.split()
            if st1!=list1[0]:
                s = ""
                for i in list1:
                    s += i + " "
                s=s+"\n"
                f1.write(s)
            else:
                print("NO SUCH ROLL NUMBER FOUND")
    f1.close()
    os.remove("STUDENT.txt")
    os.rename("STUDENT1.txt","STUDENT.txt")             
    
    
           
while True:
    print("Press 1 to input details of student")
    print("Press 2 to show the details of a student via roll number")
    print("Press 3 to change phone number")
    print("Press 4 to change branch")
    print("Press 5 to delete the record of a student")
    print("Press 6 to exit")
    x=int(input("Enter your choice: "))
    if x==6:
        break          
    elif x==1:
        write_to_file(details())
    elif x==2:
        display()
    elif x==3:
        chnum()
    elif x==4:
        brchange()
    elif x==5:
        delrecord()
    else:
        print("INVALID ENTRY\n")
        
             
        