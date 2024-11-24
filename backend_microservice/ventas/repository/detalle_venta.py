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


def eliminar_detalle_venta_db(id_detalle: int):
    """Elimina un detalle de venta de la base de datos y retorna el id_venta relacionado."""
    with DatabaseConnection() as db:
        # Obtener el id_venta antes de eliminar el detalle
        db.cursor.execute("SELECT id_venta FROM detalles_venta WHERE id = %s", (id_detalle,))
        detalle = db.cursor.fetchone()
        if not detalle:
            raise ValueError(f"El detalle con ID {id_detalle} no existe.")

        id_venta = detalle["id_venta"]

        # Eliminar el detalle
        db.cursor.execute("DELETE FROM detalles_venta WHERE id = %s", (id_detalle,))
        db.connection.commit()

        return id_venta

def actualizar_detalle_venta_db(id_detalle: int, detalle_data):
    """Actualiza un detalle de venta en la base de datos y retorna el registro actualizado."""
    with DatabaseConnection() as db:
        updates = []
        params = []

        if detalle_data.id_producto:
            updates.append("id_producto = %s")
            params.append(detalle_data.id_producto)
        if detalle_data.nombre_producto:
            updates.append("nombre_producto = %s")
            params.append(detalle_data.nombre_producto)
        if detalle_data.cantidad:
            updates.append("cantidad = %s")
            params.append(detalle_data.cantidad)
        if detalle_data.precio_unitario is not None:
            updates.append("precio_unitario = %s")
            params.append(detalle_data.precio_unitario)
        if detalle_data.subtotal is not None:
            updates.append("subtotal = %s")
            params.append(detalle_data.subtotal)

        if not updates:
            raise ValueError("No hay datos para actualizar.")

        # Actualizar el detalle de venta
        query = f"UPDATE detalles_venta SET {', '.join(updates)} WHERE id = %s"
        params.append(id_detalle)
        db.cursor.execute(query, tuple(params))
        db.connection.commit()

        # Recuperar y retornar el detalle actualizado
        db.cursor.execute("SELECT * FROM detalles_venta WHERE id = %s", (id_detalle,))
        return db.cursor.fetchone()

def obtener_detalles_por_venta(id_venta: int):
    """Obtiene todos los detalles de venta relacionados con un ID de venta."""
    with DatabaseConnection() as db:
        db.cursor.execute("SELECT * FROM detalles_venta WHERE id_venta = %s", (id_venta,))
        return db.cursor.fetchall()

def calcular_total_venta(id_venta: int):
    """Calcula el nuevo total de la venta sumando los subtotales de los detalles."""
    with DatabaseConnection() as db:
        db.cursor.execute("SELECT SUM(subtotal) FROM detalles_venta WHERE id_venta = %s", (id_venta,))
        total = db.cursor.fetchone()["SUM(subtotal)"]
        return total or 0.0

def actualizar_total_venta(id_venta: int, nuevo_total: float):
    """Actualiza el campo total en la tabla ventas."""
    with DatabaseConnection() as db:
        db.cursor.execute("UPDATE ventas SET total = %s WHERE id_venta = %s", (nuevo_total, id_venta))
        db.connection.commit()
