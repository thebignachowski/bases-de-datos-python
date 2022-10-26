from calendar import c
import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

cursor = database.cursor()



cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

#Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")
coches = [
    ('Seat', 'Alhambra', 13850),
    ('Renaul', 'Clio', 8500),
    ('Citroen', 'Saxo', 4550),
    ('Mercedes', 'Clase C', 35800)
]

cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
database.commit()

cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()

for coche in result:
    print(coche)


cursor.execute("DELETE FROM vehiculos WHERE marca = 'Renaul'")
database.commit()

