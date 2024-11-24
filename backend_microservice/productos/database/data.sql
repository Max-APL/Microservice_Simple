
INSERT INTO categoria (nombre) VALUES ('Celulares'), ('Laptops'), ('Accesorios');

INSERT INTO marca (nombre) VALUES ('Samsung'), ('Apple'), ('HP');

INSERT INTO producto (nombre, descripcion, precio, id_categoria, id_marca)
VALUES
('iPhone 13', 'Celular de alta gama', 999.99, 1, 2),
('Galaxy S21', 'Celular con Android', 799.99, 1, 1),
('HP Pavilion', 'Laptop para trabajo', 1200.00, 2, 3),
('AirPods', 'Accesorio de Apple', 199.99, 3, 2);