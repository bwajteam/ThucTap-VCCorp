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