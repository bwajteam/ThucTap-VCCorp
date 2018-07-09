# 2.2
print("2.2")
dept = 'Production'
# Lay dept_no theo dept_name
q1 = "SELECT dept_no FROM departments WHERE dept_name = '%s'" %(dept)
cur.execute(q1)
res = cur.fetchall()

# Xoa toan bo thong tin cua nhan vien va quan ly trong cac bang lien quan
q2 = "\
DELETE a, b, c, d, e \
FROM dept_emp a, employees b , salaries c , titles d, dept_manager e \
WHERE a.dept_no = 'd004' \
AND a.emp_no = b.emp_no \
AND a.emp_no = c.emp_no \
AND a.emp_no = d.emp_no \
AND e.emp_no = b.emp_no \
AND e.emp_no = c.emp_no \
AND e.emp_no = d.emp_no \
" %(res[0][0])

# Xoa bang departments
q4 = "DELETE FROM departments WHERE dept_no = '%s'" %(res[0][0])