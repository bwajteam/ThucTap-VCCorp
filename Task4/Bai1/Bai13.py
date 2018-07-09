# 1.3
print("1.3")
idEmp = 10005
vt = 'Staff'
query = "SELECT first_name, last_name, hire_date, SUM(salaries.salary) \
FROM employees, salaries, titles \
WHERE employees.emp_no = '%d' \
    AND employees.emp_no = salaries.emp_no \
    AND salaries.emp_no = titles.emp_no \
    AND salaries.from_date >= titles.from_date \
    AND salaries.to_date <= titles.to_date \
    AND titles.title = '%s'\
    " %(idEmp, vt)

cur.execute(query)
res = cur.fetchall()
print("first_name, last_name, hire_date, salary_total cua nhan vien emp_id = %d"%(idEmp))
print("%s, %s, %s, %s" %(res[0][0], res[0][1], res[0][2], res[0][3]))