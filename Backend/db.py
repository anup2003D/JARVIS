import csv
import sqlite3

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)
query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)
query = "CREATE TABLE IF NOT EXISTS contacts(id integer primary key, name VARCHAR(200), email VARCHAR(255), phone VARCHAR(255) NULL)"
cursor.execute(query)

'''query = "INSERT INTO sys_command VALUES(null,'Whatsapp', 'C:\\Users\\Anup0\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\WhatsApp Web.lnk')"
cursor.execute(query)
conn.commit()'''
'''query = "INSERT INTO web_command VALUES(null,'whatsapp', 'C:\\Users\\Anup0\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\WhatsApp Web.lnk')"
cursor.execute(query)
conn.commit()'''
'''query = "INSERT INTO web_command VALUES(null,'instagram', 'https://www.instagram.com/')"
cursor.execute(query)
conn.commit()'''

desired_columns_indices=[0,19]

with open('contacts.csv','r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        selected_data=[row[i] for i in desired_columns_indices]
        cursor.execute('''INSERT INTO contacts(id, 'name', 'phone') VALUES(null, ?,?);''', tuple(selected_data))

conn.commit()
conn.close()

print("Database and tables created successfully.")