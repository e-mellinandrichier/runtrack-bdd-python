import mysql.connector

# Connexion à la base de données
my_database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pipicaca",
    database="LaPlateforme"
)

cursor = my_database.cursor()

cursor.execute("SELECT * FROM etudiants")

etudiants = cursor.fetchall()

for etudiant in etudiants:
    print(etudiant)

cursor.close()
my_database.close()
