from database.database import DatabaseConnection

def obtener_ventas():
    with DatabaseConnection() as db:
        db.cursor.execute("SELECT * FROM ventas")
        return db.cursor.fetchall()  # La conversión se maneja en el esquema

def obtener_venta_por_id(id_venta: int):
    with DatabaseConnection() as db:
        db.cursor.execute("SELECT * FROM ventas WHERE id_venta = %s", (id_venta,))
        return db.cursor.fetchone()

def crear_venta(venta):
    with DatabaseConnection() as db:
        db.cursor.execute("""
            INSERT INTO ventas (id_cliente, fecha, total)
            VALUES (%s, %s, %s)
        """, (venta.id_cliente, venta.fecha, venta.total))
        db.cursor.execute("SELECT LAST_INSERT_ID()")
        return db.cursor.fetchone()["LAST_INSERT_ID()"]

def actualizar_venta(id_venta: int, venta):
    with DatabaseConnection() as db:
        db.cursor.execute("""
            UPDATE ventas
            SET id_cliente = %s, fecha = %s, total = %s
            WHERE id_venta = %s
        """, (venta.id_cliente, venta.fecha, venta.total, id_venta))

def eliminar_venta(id_venta: int):
    with DatabaseConnection() as db:
        db.cursor.execute("DELETE FROM ventas WHERE id_venta = %s", (id_venta,))
