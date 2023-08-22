import mysql.connector  as ms

cnx = ms.connect(
    user="root", password= "root",
    host ="127.0.0.1",
    database = "grocery_store"
)