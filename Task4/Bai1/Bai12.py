# 1.2
print("1.2")
gender = 'F'
day1 = '1950-01-01'
day2 = '1960-01-01'

query = "SELECT COUNT(*)\
FROM dept_emp, employees \
WHERE dept_emp.emp_no = employees.emp_no \
    AND employees.gender = '%s' \
    AND employees.birth_date between '%s' AND '%s' \
" %(gender, day1, day2)

cur.execute(query)
res = cur.fetchall()
print("Số nhân viên nữ có ngày sinh từ %s đến %s la %s"%(day1, day2, res[0][0]))