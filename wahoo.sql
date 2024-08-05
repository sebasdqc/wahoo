CREATE database elwahoo;
show databases;
use elwahoo;

-- Crear tabla de facturas
CREATE TABLE invoices (
    id_factura INT PRIMARY KEY AUTO_INCREMENT,
    fecha_factura DATE,
    monto INT
);

-- Crear tabla de elementos de facturas con su respectiva Foreign Key de la tabla invoices
CREATE TABLE items_factura (
    id_elemento INT PRIMARY KEY AUTO_INCREMENT,
    id_factura INT,
    descripcion VARCHAR(100),
    monto INT,
    FOREIGN KEY (id_factura) REFERENCES invoices(id_factura)
);

-- Insertar datos de ejemplo en la tabla invoices
INSERT INTO invoices (fecha_factura, monto) VALUES
('2020-12-24', 100),
('2020-12-12', 200),
('2020-11-20', 300);

-- Insertar datos de ejemplo en la tabla items_facturas
INSERT INTO items_factura (id_factura, descripcion, monto) VALUES
(1, 'carnes', 50),
(1, 'cereales', 25),
(1, 'sal', 25),
(2, 'bebidas', 150),
(2, 'carnes', 50),
(3, 'cereales', 10),
(3, 'carnes', 100),
(3, 'cefe', 100),
(3, 'frutas', 90);

-- Creamos la vista considerando los criterios requeridos
CREATE VIEW view_facturas AS
SELECT 
    invoices.id_factura,
    SUM(ef.monto) AS monto_total,
    SUM(CASE WHEN ef.descripcion = 'carnes' THEN ef.monto ELSE 0 END) AS carnes,
    SUM(CASE WHEN ef.descripcion = 'cereales' THEN ef.monto ELSE 0 END) AS cereales,
    SUM(CASE WHEN ef.descripcion NOT IN ('carnes', 'cereales') THEN ef.monto ELSE 0 END) AS otros
FROM 
    invoices
JOIN 
    items_factura ef ON invoices.id_factura = ef.id_factura
GROUP BY 
    invoices.id_factura;

-- Visualizamos la factura para comprobar 
SELECT * FROM view_facturas;