

INSERT INTO clientes (nombre, correo)
VALUES
('Juan Pérez', 'juan.perez@example.com'),
('Ana García', 'ana.garcia@example.com'),
('Carlos Sánchez', 'carlos.sanchez@example.com');


INSERT INTO ventas (id_cliente, fecha, total)
VALUES
(1, '2024-11-22', 1799.98),
(2, '2024-11-21', 199.99),
(3, '2024-11-20', 1200.00);


INSERT INTO detalles_venta (id_venta, id_producto, nombre_producto, precio_unitario, cantidad, subtotal)
VALUES
(1, 1, 'iPhone 13', 999.99, 1, 999.99),
(1, 2, 'Galaxy S21', 799.99, 1, 799.99),
(2, 4, 'AirPods', 199.99, 1, 199.99),
(3, 3, 'HP Pavilion', 1200.00, 1, 1200.00);

