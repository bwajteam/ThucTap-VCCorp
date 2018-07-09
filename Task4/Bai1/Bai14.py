# 1.4
print("1.4")
lastName = 'Markovitch'
firstName = 'Margareta'

querry  = "SELECT * FROM employees, dept_manager WHERE employees.emp_no = dept_manager.emp_no AND employees.last_name = '%s' AND employees.first_name = '%s'" % (lastName, firstName)

cur.execute(query)
res = cur.fetchall()

if res != None:
    query = "\
    SELECT * \
    FROM  dept_manager, employees, titles \
        WHERE dept_manager.emp_no = employees.emp_no \
        AND dept_manager.emp_no = titles.emp_no \
        AND employees.last_name = '%s' \
        AND employees.first_name = '%s'\
        AND titles.title = 'Manager' \
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