# 1.5
print("1.5")
day1 = '1988-06-25'
day2 = '1989-06-25'
#  tinh luong nhan vien
query = "\
SELECT departments.dept_name, SUM(salaries.salary) \
FROM salaries, dept_emp, departments \
WHERE salaries.from_date >= '%s' \
AND salaries.to_date <= '%s' \
AND salaries.emp_no = dept_emp.emp_no \
AND departments.dept_no = dept_emp.dept_no \
GROUP BY departments.dept_name \
" % (day1, day2)
cur.execute(query)
res = cur.fetchall()

salaries = []
for data in res:
    salaries[data[0] = data[0][0]

# Tinh luong manager neu manager chua tung la nhan vien

query = "\
SELECT departments.dept_name, salaries.salary, dept_manager.emp_no, salaries.from_date\
FROM salaries, dept_manager, departments\
WHERE salaries.from_date >= '%s'\
AND salaries.to_date <= '%s'\
AND dept_manager.emp_no = salaries.emp_no\
AND departments.dept_no = dept_manager.dept_no\
AND dept_manager.dept_no NOT IN (SELECT dept_emp.emp_no FROM dept_emp)\
" %(day1, day2)

cur.execute(query)
res = cur.fetchall()

for data in res:
    salaries[data[0] += data[0][0]

print("Tổng lương phải trả của mỗi phòng ban trong khoản thời gian from_date = %s và to_date %s" %(day1, day2))
for data in salaries:
    print("Phong ban: %s tra %d" % (data[0], data[1]))