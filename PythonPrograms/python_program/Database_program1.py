# database python code in mysql with python ...??


from pymysql import *
def add():	
	con=connect(db="vaibhav",user="root",password="root",host="localhost")
	cur=con.cursor()
	id=int(input("Enter the Id of student : "))
	name=input("Enter name :  ")
	clas=input("Enter class : ")
	age=int(input("Enter Age : "))
	address=input("Enter YOur add : ")
	contact=int(input("Enter Your Contact Number : "))
	cur.execute("insert into data values('%d','%s','%s','%d','%s','%d')"%(id,name,clas,age,address,contact))
	con.commit()
	print("Record Inserted")
	con.close()
def display():
	con=connect(db="vaibhav",user="root",password="root",host="localhost")
	cur=con.cursor()
	cur.execute("Select * from data")
	result=cur.fetchall()
	print("Id\tName\tClaas\tAge\tAddress\tContact")
	for x in result:
		print("%d\t%s\t%s\t%d\t%s\t%d"%(x[0],x[1],x[2],x[3],x[4],x[5]))
	con.close()
	con.commit()	
display()	