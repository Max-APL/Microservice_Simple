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

def actualizar_detalle_venta_db(id_detalle: int, detalle_data):
    """Actualiza un detalle de venta en la base de datos."""
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

        query = f"UPDATE detalles_venta SET {', '.join(updates)} WHERE id = %s"
        params.append(id_detalle)

        db.cursor.execute(query, tuple(params))
        db.connection.commit()
