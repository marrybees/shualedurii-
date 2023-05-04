import sqlite3
conn = sqlite3.connect("students")
cursor = conn.cursor()
r = cursor.execute("SELECT * FROM STUDENTS ")
x = cursor.fetchall()

def funqcia(SocialMedia, age):
    ('SELECT id from students WERE age = 16 and SocialMedi ="instagram"')
x = print
m = cursor.execute('select id from students WERE OnlineClassTime > 2 ')
l = cursor.execut('INSERT INTO students(age) VALUES (16)')
print(m)
print(l)
conn.close()