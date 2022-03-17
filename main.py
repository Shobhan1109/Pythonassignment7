import sqlite3

conn = sqlite3.connect('Employee3.db')

conn.execute('''CREATE TABLE Employee_info_
                (ID INT PRIMARY KEY NOT NULL,
                 Fname TEXT NOT NULL,
                 Lname TEXT NOT NULL,
                 salary INT);''')

print("table created successfully")

conn.execute('''insert into Employee_info_(ID,Fname,Lname,salary)
                values(1,'Sharath','kumar',12000)''')
conn.execute('''insert into Employee_info_(ID,Fname,Lname,salary)
                values(2,'Rithick','B',10000)''')
conn.execute('''insert into Employee_info_(ID,Fname,Lname,salary)
                values(3,'Rishi','H',18000)''')
conn.execute('''insert into Employee_info_(ID,Fname,Lname,salary)
                values(4,'Krisha','A',19000)''')
conn.execute('''insert into Employee_info_(ID,Fname,Lname,salary)
                values(5,'Shoban','raj',20000)''')

print("record is inserted:")

conn.commit()

print("all records")

res=conn.execute('''select * from Employee_info_;''')
for row in res:
 print(row[0], " ", row[1], " ", row[2], " ", row[3])
print("QUERY")

res1=conn.execute('''select * from Employee_info_ order by Fname asc;''')
for row in res1:
 print(row[0], " ", row[1], " ", row[2], " ", row[3])
conn.close()