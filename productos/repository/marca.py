from database.database import DatabaseConnection

def obtener_marcas():
    with DatabaseConnection() as db:
        db.cursor.execute("SELECT * FROM marca")
        return db.cursor.fetchall()

def obtener_marca_por_id(id_marca: int):
    with DatabaseConnection() as db:
        db.cursor.execute("SELECT * FROM marca WHERE id_marca = %s", (id_marca,))
        return db.cursor.fetchone()

def crear_marca(marca):
    with DatabaseConnection() as db:
        db.cursor.execute("""
            INSERT INTO marca (nombre)
            VALUES (%s)
        """, (marca.nombre,))
        # Obtener el ID de la marca recién creada
        db.cursor.execute("SELECT LAST_INSERT_ID()")
        return db.cursor.fetchone()["LAST_INSERT_ID()"]

def actualizar_marca(id_marca: int, marca):
    with DatabaseConnection() as db:
        db.cursor.execute("""
            UPDATE marca
            SET nombre = %s
            WHERE id_marca = %s
        """, (marca.nombre, id_marca))

def eliminar_marca(id_marca: int):
    with DatabaseConnection() as db:
        db.cursor.execute("DELETE FROM marca WHERE id_marca = %s", (id_marca,))
