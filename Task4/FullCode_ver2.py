import MySQLdb as sql
import datetime

hostname = 'localhost'
username = 'root'
password = '123456'
database = 'employees'

myConnection = sql.connect( host=hostname, user=username, passwd=password, db=database )

cur = myConnection.cursor()
# 1.1
print("1.1")
day1 = '1999-01-01'
day2 = '1999-12-31'

query = "\
SELECT * \
FROM dept_emp, employees, departments \
WHERE dept_emp.emp_no = employees.emp_no \
    AND dept_emp.dept_no = departments.dept_no \
    AND dept_emp.from_date between '%s'AND '%s' \
LIMIT 10 \
" %(day1, day2)

cur.execute(query)

print("10 Nhan vien lam viec tu %s den %s" %(day1, day2))
for data in cur.fetchall():
    print(data[0], data[2], data[3], data[5], data[6], data[7], data[8], data[9], data[11])
# Lấy 10 giá trị với fetchmany
# res = cur.fetchmany(10) 

# 1.2
print("1.2")
gt = 'F'
day1 = '1950-01-01'
day2 = '1960-01-01'

query = "SELECT COUNT(*)\
FROM dept_emp, employees \
WHERE dept_emp.emp_no = employees.emp_no \
    AND employees.gender = '%s' \
    AND employees.birth_date between '%s' AND '%s' \
" %(gt, day1, day2)

cur.execute(query)
res = cur.fetchall()
print("Số nhân viên nữ có ngày sinh từ %s đến %s la %s"%(day1, day2, res[0][0]))

# 1.3
print("1.3")
idEmp = 10005
vt = 'Staff'
query = "SELECT first_name, last_name, hire_date, SUM(salaries.salary) \
FROM employees, salaries, titles \
WHERE employees.emp_no = '%d' \
    AND employees.emp_no = salaries.emp_no \
    AND salaries.emp_no = titles.emp_no \
    AND salaries.from_date > titles.from_date \
    AND salaries.to_date < titles.to_date \
    AND titles.title = '%s'\
    " %(idEmp, vt)

cur.execute(query)
res = cur.fetchall()
print("first_name, last_name, hire_date, salary_total cua nhan vien emp_id = %d"%(idEmp))
print("%s, %s, %s, %s" %(res[0][0], res[0][1], res[0][2], res[0][3]))

# 1.4
print("1.4")
lastName = 'Markovitch'
firstName = 'Margareta'

querry  = "SELECT * FROM employees WHERE last_name = '%s' AND first_name = '%s'" % (lastName, firstName)

cur.execute(query)
res = cur.fetchall()

if res != None:
    query = "\
    SELECT * \
    FROM  dept_manager, employees \
        WHERE dept_manager.emp_no = employees.emp_no \
        AND employees.last_name = '%s' \
        AND employees.first_name = '%s'\
    " % (lastName, firstName)
    try:
    # Thuc thi lenh SQL
        cur.execute(query)
    # Commit cac thay doi vao trong Database
        myConnection.commit()
    except:
    # Rollback trong tinh huong co bat ky error nao
        myConnection.rollback()

    res = cur.fetchall()
    deptNo = res[0][0]

    # Them dieu kien AND dept_emp.to_date = '9999-01-01' de loai cac nhan vien da len lam quan ly
    query = "\
    SELECT COUNT(*) \
    FROM dept_emp \
    WHERE dept_emp.dept_no = '%s'\
        AND dept_emp.to_date = '9999-01-01' \
    " %(deptNo)
    cur.execute(query)
    res = cur.fetchall()
    print("So nhan vien ma Margareta Markovitch quan ly: %s"%(res[0][0])) 
# 1.5
print("1.5")
day1 = '1988-06-25'
day2 = '1989-06-25'

query = "\
SELECT departments.dept_name, SUM(salaries.salary) \
FROM departments, dept_emp, dept_manager, salaries \
WHERE dept_emp.dept_no = departments.dept_no \
    AND dept_manager.dept_no = departments.dept_no \
    AND dept_emp.emp_no = salaries.emp_no \
    AND dept_manager.emp_no = salaries.emp_no \
    AND salaries.from_date between '%s' AND '%s' \
    AND salaries.to_date between '%s' AND '%s' \
    AND dept_manager.emp_no NOT IN dept_emp.emp_no \
GROUP BY departments.dept_no \
" % (day1, day2, day1, day2)
cur.execute(query)
res = cur.fetchall()
print("Tổng lương phải trả của mỗi phòng ban trong khoản thời gian from_date = %s và to_date %s" %(day1, day2))
for data in res:
    print("Phong ban: %s tra %d" % (data[0], data[1]))

# 2.1
print("2.1")
# Lay ngay thuc hien cap nhat lam moc thoi gian to_date, start_date
toDay = datetime.datetime.now().strftime('%Y-%m-%d')

idEmp = 10002

query = "\
UPDATE titles \
SET to_date = '%s' \
WHERE emp_no = '%d'\
AND start_date = (SELECT MAX(Start_date) FROM titles) \
" % (toDay, idEmp)

try:
   cur.execute(query)
   myConnection.commit()
except:
   myConnection.rollback()

vt = 'Senior Staff'
query = "\
INSERT INTO titles \
VALUES ('%d', '%s', '%s', '9999-01-01')\
" % (idEmp, vt, toDay)
try:
   cur.execute(query)
   myConnection.commit()
except:
   myConnection.rollback()

print("Thăng chức cho nhân viên 10002 từ “Staff” lên “Senior Staff”")
print("Kiem tra: ")

query = "SELECT * FROM titles WHERE emp_no = '%s' " % (idEmp)

cur.execute(query)
res = cur.fetchall()
for data in res:
    print(data)
# 2.2
print("2.2")
dept = 'Production'
# Lay dept_no theo dept_name
q1 = "SELECT dept_no FROM departments WHERE dept_name = '%s'" %(dept)
cur.execute(q1)
res = cur.fetchall()

# Xoa toan bo thong tin cua nhan vien trong cac bang lien quan
q2 = "\
DELETE * FROM dept-emp, employees, salariees, titles \
WHERE dept_emp.dept_no = '%s' \
AND dept_emp.emp_no = employees.emp_no \
AND dept_emp.emp_no = salariees.emp_no \
AND dept_emp.emp_no = titles.emp_no \
" %(res[0][0])

# # Xoa toan bo thong tin quan ly trong cac bang lien quan
q3 = "\
DELETE * FROM dept_manager, employees, salariees, titles \
WHERE dept_manager.dept_no = '%s' \
AND dept_manager.emp_no = employees.emp_no \
AND dept_manager.emp_no = salariees.emp_no \
AND dept_manager.emp_no = titles.emp_no \
" %(res[0][0])

# Xoa bang departments
q4 = "DELETE FROM departments WHERE dept_no = '%s'" %(res[0][0])

# 2.3
print("2.3")
idEmp = 29005
dept_name = 'Bigdata & ML'
dept_no = 'd010'


# Them phong moi

query = "\
INSERT INTO departments \
VALUES ('%s' ,'%s') \
"%(dept_no, dept_name)

try:
   cur.execute(query)
   myConnection.commit()
except:
   myConnection.rollback()

# Xoa emp_id trong bang dept_emp
query = " \
DELETE \
FROM dept_emp \
WHERE emp_no = '%s' \
" %(idEmp)
# Them emp_id trong bang dept_manager
# Lay ngay thuc hien cap nhat lam moc thoi gian to_date, start_date
toDay = datetime.datetime.now().strftime('%Y-%m-%d')

query ="\
INSERT INTO dept_manager\
VALUES ('%s','%d','%s', '9999-01-01' )\
" %(dept_no, idEmp, toDay)




print("Kiem tra: ")
query = "SELECT * FROM dept_manager WHERE emp_no = '%s' " % (idEmp)

cur.execute(query)
res = cur.fetchall()
for data in res:
    print(data)

# 3.1
print("3.1")

firstName = 'Chirstian' 

query = "\
DELIMITER $$\
DROP PROCEDURE IF EXISTS getDataEmp $$ \
CREATE PROCEDURE getDataEmp(IN firstName varchar(20))\
BEGIN\
   SELECT employees.emp_no, employees.first_name, employees.last_name, employees.gender, titles.title, departments.dept_name\
   FROM employees, titles, departments, dept_emp\
   WHERE dept_emp.dept_no = departments.dept_no\
   AND dept_emp.emp_no = employees.emp_no\
   AND employees.emp_no = titles.emp_no\
   AND employees.first_name = firstName;\
END; $$\
DELIMITER ;\
"
try:
   cur.execute(query)
   myConnection.commit()
except:
   myConnection.rollback()

query = "\
CALL getDataEmp('%s');\
" %(firstName)

cur.execute(query)
res = cur.fetchall()
for data in res:
    print(data)

# 3.2
print("3.2")
firstName = 'Mari'
query = "\
DELIMITER $$\
DROP PROCEDURE IF EXISTS getSalariesByName $$ \
CREATE PROCEDURE getSalariesByName(IN firstName varchar(20))\
BEGIN\
   SELECT employees.emp_no, employees.first_name, employees.last_name, SUM(salaries.salary)\
   FROM employees, salaries\
   WHERE salaries.emp_no = employees.emp_no\
   AND employees.first_name = firstName\
   GROUP BY employees.emp_no;\
END; $$\
DELIMITER ;\
"

try:
   cur.execute(query)
   myConnection.commit()
except:
   myConnection.rollback()

query = "\
CALL getSalariesByName('%s');\
" %(firstName)

cur.execute(query)
res = cur.fetchall()
for data in res:
    print(data)


# 4.1
print("4.1")

idEmp = 10001
idDept = 'd010'
newTitle = 'Senior Engineer'
toDay = datetime.datetime.now().strftime('%Y-%m-%d')

# Kiem tra nhan vien co la quan ly hay khong
query = "\
SELECT emp_id \
FROM dept_emp \
WHERE to_date > '%s' \
" %(toDay)
cur.execute(query)
res = cur.fetchall()

if res != None:
    query ="\
    DELIMITER $$\
    DROP PROCEDURE IF EXISTS changeDept $$ \
    CREATE PROCEDURE changeDept(IN idEmp INT(5), IN idDept varchar(5), IN newTitle varchar (50), IN toDay varchar (20))\
    BEGIN\
        UPDATE dept_emp\
        SET dept_no = idDept\
        WHERE emp_no = idEmp;\
    \
        UPDATE titles\
        SET to_date = toDay\
        WHERE emp_no = idEmp;\
    \
        INSERT INTO titles\
        VALUES (idEmp, newTitle, toDay, '9999-01-01');\
    \
        SELECT employees.emp_no, employees.first_name, employees.last_name, employees.gender, titles.title, departments.dept_name\
            FROM employees, departments, dept_emp, titles\
            WHERE employees.emp_no = dept_emp.emp_no\
            AND employees.emp_no = titles.emp_no\
            AND dept_emp.dept_no = departments.dept_no\
            AND employees.emp_no = idEmp;\
    END; $$\
    DELIMITER ;\
    "
    # Them dieu kien update voi ngay max nhung bi loi, y 2.1 tuong tu ko bi loi
    # UPDATE titles\
    # SET to_date = toDay\
    # WHERE emp_no = idEmp;\
    # AND from_date = (SELECT MAX(from_date) FROM titles);\

    try:
        cur.execute(query)
        myConnection.commit()
    except:
        myConnection.rollback()

    query = "\
    CALL changeDept('%s', '%s', '%s', '%s');\
    " %(idEmp, idDept, newTitle, toDay)

    cur.execute(query)
    res = cur.fetchall()
    for data in res:
        print(data)

myConnection.close()