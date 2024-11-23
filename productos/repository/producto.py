from database.database import DatabaseConnection

def obtener_productos():
    with DatabaseConnection() as db:
        db.cursor.execute("SELECT * FROM producto")
        return db.cursor.fetchall()

def obtener_producto_por_id(id_producto: int):
    with DatabaseConnection() as db:
        db.cursor.execute("SELECT * FROM producto WHERE id_producto = %s", (id_producto,))
        return db.cursor.fetchone()

def crear_producto(producto):
    with DatabaseConnection() as db:
        db.cursor.execute("""
            INSERT INTO producto (nombre, descripcion, precio, id_categoria, id_marca)
            VALUES (%s, %s, %s, %s, %s)
        """, (producto.nombre, producto.descripcion, producto.precio, producto.id_categoria, producto.id_marca))
        # Obtener el ID del producto recién creado
        db.cursor.execute("SELECT LAST_INSERT_ID()")
        return db.cursor.fetchone()["LAST_INSERT_ID()"]

def actualizar_producto(id_producto: int, producto):
    with DatabaseConnection() as db:
        db.cursor.execute("""
            UPDATE producto
            SET nombre = %s, descripcion = %s, precio = %s, id_categoria = %s, id_marca = %s
            WHERE id_producto = %s
        """, (producto.nombre, producto.descripcion, producto.precio, producto.id_categoria, producto.id_marca, id_producto))

def eliminar_producto(id_producto: int):
    with DatabaseConnection() as db:
        db.cursor.execute("DELETE FROM producto WHERE id_producto = %s", (id_producto,))

def buscar_producto_por_id(id_producto):
    """Consulta un producto por ID en la base de datos."""
    with DatabaseConnection() as db:
        db.cursor.execute("SELECT * FROM producto WHERE id_producto = %s", (id_producto,))
        return db.cursor.fetchone()