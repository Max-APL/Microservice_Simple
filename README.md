# Sistema de Gestión de Productos y Ventas

Este proyecto consiste en un sistema basado en **microservicios** para la gestión de productos y ventas. Está diseñado para demostrar una arquitectura moderna y escalable, utilizando **FastAPI** como framework para los microservicios, **RabbitMQ** para la comunicación asincrónica entre ellos y **MySQL** como base de datos para persistencia.

---

## 🚀 **Arquitectura del Sistema**

El sistema está compuesto por dos microservicios principales:

### **1. Microservicio de Gestión de Productos**
Este microservicio maneja las operaciones relacionadas con los productos, incluyendo:
- **CRUD de Productos**: Crear, leer, actualizar y eliminar productos.
- **Gestión de Marcas**: CRUD para marcas asociadas a los productos.
- **Gestión de Categorías**: CRUD para categorías de productos.
- **Cola RabbitMQ**: Escucha solicitudes para obtener detalles de un producto.

Endpoints principales:
- `/gestion_productos/productos`: Endpoints para CRUD de productos.
- `/gestion_productos/marcas`: Endpoints para CRUD de marcas.
- `/gestion_productos/categorias`: Endpoints para CRUD de categorías.

### **2. Microservicio de Ventas**
Este microservicio se encarga de las operaciones relacionadas con las ventas, incluyendo:
- **Registro de Ventas**: Crear una venta con detalles asociados.
- **Detalles de Venta**: Registro y consulta de los productos vendidos.
- **Comunicación con Productos**: Solicita datos del producto al microservicio de Gestión de Productos a través de RabbitMQ.

Endpoints principales:
- `/ventas/venta`: Endpoints para CRUD de ventas.
- `/ventas/detalle`: Endpoints para gestionar detalles de venta.

---

## 📡 **Comunicación entre Microservicios**

La comunicación entre los microservicios utiliza **RabbitMQ** para el intercambio de mensajes asincrónicos:
1. **Microservicio de Ventas** envía una solicitud a la cola `productos_request` para obtener los detalles de un producto.
2. **Microservicio de Gestión de Productos** escucha esa cola, busca el producto en la base de datos y publica una respuesta en la cola `productos_response`.
3. **Microservicio de Ventas** consume la respuesta y la utiliza para completar la operación.

---

## 🛠️ **Tecnologías Utilizadas**

- **Backend**:
  - [FastAPI](https://fastapi.tiangolo.com/): Framework para construir los microservicios.
  - [MySQL](https://www.mysql.com/): Base de datos relacional para persistencia de datos.
  - [RabbitMQ](https://www.rabbitmq.com/): Broker de mensajes para comunicación entre microservicios.
  - [Pika](https://pika.readthedocs.io/): Cliente Python para RabbitMQ.

- **Frontend** (en desarrollo):
  - [Vue.js](https://vuejs.org/): Framework progresivo para construir interfaces de usuario.

---

## 🛠️ **Configuración del Proyecto**

### **1. Requisitos Previos**
Asegúrate de tener instalados:
- [Python 3.10 o superior](https://www.python.org/downloads/)
- [RabbitMQ](https://www.rabbitmq.com/download.html)
- [MySQL](https://dev.mysql.com/downloads/installer/)

### **2. Clonar el Repositorio**
Clona este repositorio en tu máquina local:
```bash
git clone https://github.com/tu-usuario/nombre-del-repositorio.git
cd nombre-del-repositorio
