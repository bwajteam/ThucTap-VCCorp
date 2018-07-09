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