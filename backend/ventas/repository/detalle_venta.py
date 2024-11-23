from database.database import DatabaseConnection

def obtener_detalles_venta():
    with DatabaseConnection() as db:
        db.cursor.execute("SELECT * FROM detalles_venta")
        return db.cursor.fetchall()

def obtener_detalle_venta_por_id(id: int):
    with DatabaseConnection() as db:
        db.cursor.execute("SELECT * FROM detalles_venta WHERE id = %s", (id,))
        return db.cursor.fetchone()

def crear_detalle_venta(detalle):
    with DatabaseConnection() as db:
        db.cursor.execute("""
            INSERT INTO detalles_venta (id_venta, id_producto, nombre_producto, precio_unitario, cantidad, subtotal)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (detalle.id_venta, detalle.id_producto, detalle.nombre_producto, detalle.precio_unitario, detalle.cantidad, detalle.subtotal))
        db.cursor.execute("SELECT LAST_INSERT_ID()")
        return db.cursor.fetchone()["LAST_INSERT_ID()"]

def eliminar_detalle_venta(id: int):
    with DatabaseConnection() as db:
        db.cursor.execute("DELETE FROM detalles_venta WHERE id = %s", (id,))
