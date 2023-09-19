import mysql.connector

#  program emulates any select command(w/out args...             yet)

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database='hr_manager',
    user='root',
    password='cr1ng3',
    autocommit=True
)



def selct(column_name, table_name):
    sql = "SELECT "+ column_name +" FROM " + table_name + ""
#    sql += " WHERE first_name ='" + first_name + "'"
#    sql += " AND employees.job_id = jobs.job_id; "
    print(sql)

    cur = connection.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    if cur.rowcount > 0:
        for i in result:
            print(i[0])
    return

select, table = input("select>  "), input("from> ")
selct(select, table)
