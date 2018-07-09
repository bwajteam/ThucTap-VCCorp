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

newTitle = 'Senior Staff'
query = "\
INSERT INTO titles \
VALUES ('%d', '%s', '%s', '9999-01-01')\
" % (idEmp, newTitle, toDay)
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