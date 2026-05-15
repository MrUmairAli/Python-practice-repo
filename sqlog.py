import mysql.connector

# Connect
d = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="user_system"
)

cursor = d.cursor()
cursor.execute("INSERT INTO users VALUES (%s, %s, %s)", (6, 'ale', 'alice12hgjh3'))
d.commit()   
cursor.execute("SELECT * FROM users")
c=[]
for x in cursor:
    c.append(x)
print(c)

    