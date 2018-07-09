import MySQLdb as sql
import datetime

hostname = 'localhost'
username = 'duyhung'
password = 'password'
database = 'employees'

myConnection = sql.connect( host=hostname, user=username, passwd=password, db=database )

cur = myConnection.cursor()
# 1.1
print("1.1")
day1 = '1999-01-01'
day2 = '1999-12-31'

query = "\
SELECT * \
FROM dept_emp, employees\
WHERE dept_emp.emp_no = employees.emp_no \
    AND dept_emp.from_date between '%s'AND '%s' \
LIMIT 10 \
" %(day1, day2)

cur.execute(query)

print("10 Nhan vien lam viec tu %s den %s" %(day1, day2))
for data in cur.fetchall():
    print(data[0], data[2], data[3], data[5], data[6], data[7], data[8], data[9], data[11])
# Lấy 10 giá trị với fetchmany
# res = cur.fetchmany(10) 

myConnection.close()