print("**************************")
print("*       FILE HANDLING      *")
print("***************************")
import os
while True:
  def f():
    print("1.create the file")
    print("2.read the file")
    print("3.list the file")
    print("4.edit the file")
    print("5.delete the file")
    print("6.stop the program")
  a=input("enter the choice")
  match a:
    case"1":
        print("creating a file")
        name=input("enter the file name:")
        name=name+".txt"
        file=open(name,"w")
        file.write("welcome")
        print("__________________")
        print("file created succesfully")
        print("____________________")
    case"2":
        print("reading a file")
        name=input("enter the file name:")
        name=name+".txt"
        file=open(name,"r")
        print("__________________________")
        print(file.read())
        print("__________________________")
        f()
    case"3":
        print("listing a file")
        print("____________________")
        path="D:\MONISHA PYTHON"
        file=os.listdir(path)
        for file in file:
          print(file)
        print("_______________________")
        f()
    case"4":
        print("editing a file")
        name=input("enter the file name:")
        name=name+".txt"
        file=open(name,"a")
        print(file.write("gowdthi"))
        print("____________________")
        print("edited the file")
        print("________________")
    case"5":
        print("deleting a file")
        name=input("enter the file name:")
        name=name+".txt"
        os.remove(name)
        print("file",name,"deleted succesfully")
        print("_______________________")
    case"6":
        print("stop the program")
print("end")

        
