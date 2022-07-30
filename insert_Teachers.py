from creator import schoolname,username,password
import insert_Subjects
import mysql
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user=username,
  passwd=password,
  database=schoolname)

mycursor = mydb.cursor()

ans="y"
count=1
print("Enter all teachers details: ")
while ans=="Y" or ans=="y":
    print("Record",count, ":")
    tid=input("Enter teacher id: ")
    name=input("Enter teacher name: ")
    subid=input("Enter sub id: ")
    sql = "INSERT INTO teachers (t_id, t_name, sub_id) VALUES (%s, %s, %s)"
    val = (tid, name, subid)
    mycursor.execute(sql, val)
    count+=1

    mydb.commit()

    print(mycursor.rowcount, "Record inserted.")
    
    ans=input("Do you wish to contiue?\n")

mycursor.execute("SELECT * FROM teachers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)