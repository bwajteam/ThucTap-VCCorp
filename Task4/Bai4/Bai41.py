# 4.1
print("4.1")

idEmp = 10001
idDept = 'd010'
newTitle = 'Senior Engineer'
toDay = datetime.datetime.now().strftime('%Y-%m-%d')




query ="\
DELIMITER $$\
    DROP PROCEDURE IF EXISTS changeDept $$ \
    CREATE PROCEDURE changeDept(IN idEmp INT(5), IN idDept varchar(5), IN newTitle varchar (50), IN toDay varchar (20))\
    BEGIN\
        IF newTitle != 'Manager' THEN \
\
            UPDATE dept_emp\
            SET to_date = toDay\
            WHERE emp_no = idEmp\
            AND to_date = '9999-01-01';\
            \
            INSERT INTO dept_emp \
            VALUES (idEmp, idDept, toDay, '9999-01-01'); \
            \           
            UPDATE titles \
            SET to_date = toDay\
            WHERE emp_no = idEmp\
            AND to_date = '9999-01-01';\
\    
            INSERT INTO titles\
            VALUES (idEmp, newTitle, toDay, '9999-01-01');\
    \
            SELECT employees.emp_no, employees.first_name, employees.last_name, employees.gender, titles.title, departments.dept_name \
            FROM employees, departments, dept_emp, titles\
            WHERE employees.emp_no = dept_emp.emp_no\
            AND employees.emp_no = titles.emp_no\
            AND dept_emp.dept_no = departments.dept_no\
            AND employees.emp_no = idEmp\
            AND titles.from_date < dept_emp.to_date\
            AND titles.to_date > dept_emp.from_date;\
        END IF ;\
    END; $$\
    DELIMITER ;\
    "


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