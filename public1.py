import sqlite3
connect = sqlite3.connect("mani_database.db")
cursor = connect.cursor()
result = cursor.execute("SELECT * FROM shopinfo WHERE 1")
row = list(result.fetchone())
shopname = row[0]
shopaddress = row[1]
shoptel = row[2]
shoptype = row[3]
shop_money_unit = row[4]
