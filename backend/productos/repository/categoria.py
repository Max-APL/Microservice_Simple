from database.database import DatabaseConnection

def obtener_categorias():
    with DatabaseConnection() as db:
        db.cursor.execute("SELECT * FROM categoria")
        return db.cursor.fetchall()

def obtener_categoria_por_id(id_categoria: int):
    with DatabaseConnection() as db:
        db.cursor.execute("SELECT * FROM categoria WHERE id_categoria = %s", (id_categoria,))
        return db.cursor.fetchone()

def crear_categoria(categoria):
    with DatabaseConnection() as db:
        db.cursor.execute("""
            INSERT INTO categoria (nombre)
            VALUES (%s)
        """, (categoria.nombre,))
        # Obtener el ID de la categoría recién creada
        db.cursor.execute("SELECT LAST_INSERT_ID()")
        return db.cursor.fetchone()["LAST_INSERT_ID()"]

def actualizar_categoria(id_categoria: int, categoria):
    with DatabaseConnection() as db:
        db.cursor.execute("""
            UPDATE categoria
            SET nombre = %s
            WHERE id_categoria = %s
        """, (categoria.nombre, id_categoria))

def eliminar_categoria(id_categoria: int):
    with DatabaseConnection() as db:
        db.cursor.execute("DELETE FROM categoria WHERE id_categoria = %s", (id_categoria,))
