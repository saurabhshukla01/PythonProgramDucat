str=input("Enter File Name : ")
f=open(str+".txt","r")
print("Is file is closed   : ",f.closed)
print("Mode of file is     : ",f.mode)
print("Opened file name is : ",f.name)
f.close()
print("Is file is closed   : ",f.closed)