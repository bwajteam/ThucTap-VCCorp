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