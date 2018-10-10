import sqlite3
import os


def checkDB():
    user_input = input('輸入y繼續，n退出')
    while user_input != 'n':
        db = sqlite3.connect('test_test.db')
        data_kind = input('1.什麼的帳號： ')
        user_id = input('2.帳號: ')
        user_password = input('3.密碼： ')
        db.execute("CREATE TABLE IF NOT EXISTS USER1 (which_app TEXT, user_id TEXT, password TEXT)")
        db.execute("INSERT INTO USER1 VALUES(?, ?, ?)", (data_kind, user_id, user_password))

        user_input = input('輸入y繼續，n退出')

        cursor = db.cursor()
        cursor.execute('SELECT * FROM USER1')

        for a, b, c in cursor:
            with open('out_put.txt', 'a') as f:
                f.write('\n' + '--' * 16 + '\n' + a + '\n' + b + '\n' + c)
                f.close()

            print(a)
            print(b)
            print(c)
            print('--' * 16)


def cursor():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM test_test')
    for a, b, c in cursor:
        print(a)
        print(b)
        print(c)
        print('--' * 20)
        db.close()


checkDB()

def insertDb(name, passwd):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    checkDB(c)
    c.execute("INSERT INTO passwd (name,password) VALUES ('" + name + "', '" + passwd + "')")
    conn.commit()
    conn.close()


def selectDb(pid, name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    checkDB(c)

    select = "SELECT * from passwd "
    if name:
        select += ('where name LIKE \'%' + name + '%\'')
    if pid:
        select += ('where id = \'' + str(pid) + '\'')
    select += 'ORDER BY id DESC'

    res = list(c.execute(select))
    if len(res) == 0:
        print('Info: record is empty')
    else:
        x = PrettyTable(['id', 'name', 'password', 'time'])
        x.align['name'] = 'l'
        x.padding_width = 1
        for row in res:
            x.add_row(list(row))
        print(x)
    conn.close()


def deleteDb(pid):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    checkDB(c)
    c.execute('DELETE from passwd where id=' + str(pid))
    conn.commit()
    o = conn.total_changes
    if o == 0:
        print('Failure: the password was not found')
    if o == 1:
        print('Success: ID ' + str(pid) + ' password has been deleted')
    conn.close()


checkDB(test_test.db)
print('hello world bye world')
