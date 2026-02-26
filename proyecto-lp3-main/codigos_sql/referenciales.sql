
DROP TABLE IF EXISTS venta CASCADE;
DROP TABLE IF EXISTS disponibilidad_horaria CASCADE;
DROP TABLE IF EXISTS libro CASCADE;
DROP TABLE IF EXISTS cliente CASCADE;
DROP TABLE IF EXISTS usuario CASCADE;
DROP TABLE IF EXISTS turno CASCADE;
DROP TABLE IF EXISTS dia CASCADE;
DROP TABLE IF EXISTS persona CASCADE;
DROP TABLE IF EXISTS genero CASCADE;
DROP TABLE IF EXISTS categoria CASCADE;
DROP TABLE IF EXISTS autor CASCADE;
DROP TABLE IF EXISTS ciudad CASCADE;


CREATE TABLE ciudad(
    id_ciudad SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) UNIQUE
);

CREATE TABLE genero(
    id_genero SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) UNIQUE
);

CREATE TABLE categoria(
    id_categoria SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) UNIQUE
);

CREATE TABLE autor(
    id_autor SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE dia(
    id_dia SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) UNIQUE
);

CREATE TABLE turno(
    id_turno SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) UNIQUE
);

CREATE TABLE usuario(
    id_usuario SERIAL PRIMARY KEY,
    nickname VARCHAR(60) NOT NULL,
    clave VARCHAR(255) NOT NULL,
    estado BOOLEAN DEFAULT TRUE
);


CREATE TABLE persona(
    id_persona SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    documento VARCHAR(20),
    telefono VARCHAR(20),
    email VARCHAR(100),
    id_genero INTEGER NOT NULL,
    id_ciudad INTEGER NOT NULL,
    FOREIGN KEY(id_genero) REFERENCES genero(id_genero)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(id_ciudad) REFERENCES ciudad(id_ciudad)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE cliente(
    id_cliente SERIAL PRIMARY KEY,
    id_persona INTEGER NOT NULL,
    FOREIGN KEY(id_persona) REFERENCES persona(id_persona)
        ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE libro(
    id_libro SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    id_autor INTEGER NOT NULL,
    id_categoria INTEGER NOT NULL,
    precio NUMERIC(10,2) NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY(id_autor) REFERENCES autor(id_autor)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(id_categoria) REFERENCES categoria(id_categoria)
        ON DELETE RESTRICT ON UPDATE CASCADE
);


CREATE TABLE disponibilidad_horaria(
    id_disponibilidad SERIAL PRIMARY KEY,
    id_dia INTEGER NOT NULL,
    id_turno INTEGER NOT NULL,
    disponible BOOLEAN DEFAULT TRUE,
    observacion VARCHAR(200),
    FOREIGN KEY(id_dia) REFERENCES dia(id_dia)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(id_turno) REFERENCES turno(id_turno)
        ON DELETE RESTRICT ON UPDATE CASCADE
);


CREATE TABLE venta(
    id_venta SERIAL PRIMARY KEY,
    id_cliente INTEGER NOT NULL,
    id_libro INTEGER NOT NULL,
    cantidad INTEGER DEFAULT 1,
    precio NUMERIC(10,2) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(id_libro) REFERENCES libro(id_libro)
        ON DELETE RESTRICT ON UPDATE CASCADE
);


INSERT INTO dia (descripcion) VALUES
('Lunes'),
('Martes'),
('Miércoles'),
('Jueves'),
('Viernes'),
('Sábado'),
('Domingo');

INSERT INTO turno (descripcion) VALUES
('Mañana'),
('Tarde');

INSERT INTO categoria (descripcion) VALUES
('Novela'),
('Ciencia'),
('Historia'),
('Tecnología'),
('Infantil');

INSERT INTO genero (descripcion) VALUES
('Ficción'),
('No Ficción'),
('Educativo');
