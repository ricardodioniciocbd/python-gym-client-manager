# Zona Fit - Sistema de Gestión de Clientes de Gimnasio

Una aplicación de consola desarrollada en Python para gestionar clientes de gimnasio utilizando el patrón de diseño DAO (Data Access Object) y MySQL como base de datos.

## Características

- **CRUD completo**: Crear, leer, actualizar y eliminar clientes
- **Patrón DAO**: Separación clara entre lógica de negocio y acceso a datos
- **Connection Pooling**: Gestión eficiente de conexiones MySQL
- **Interfaz de consola**: Menú interactivo fácil de usar
- **Manejo de errores**: Gestión robusta de excepciones

## Tecnologías

- **Python 3.12**
- **MySQL** - Base de datos
- **mysql-connector-python** - Conector de base de datos
- **Patrón DAO** - Arquitectura de acceso a datos

## Funcionalidades

1. **Listar clientes** - Visualizar todos los clientes registrados
2. **Agregar cliente** - Registrar nuevos clientes
3. **Modificar cliente** - Actualizar información existente
4. **Eliminar cliente** - Remover clientes del sistema
5. **Gestión de membresías** - Control de números únicos de membresía

## Estructura del Proyecto
python-gym-client-manager/ 
├── cliente.py # Clase entidad Cliente
├── conexion.py # Gestión de conexiones MySQL 
├── cliente_dao.py # Patrón DAO para operaciones CRUD
├── zona_fit_app.py # Interfaz de usuario (capa de presentación) 
└── README.md