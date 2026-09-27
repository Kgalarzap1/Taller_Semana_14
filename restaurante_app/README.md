# Restaurante App - Semana 14

## Descripción

Proyecto correspondiente a la Semana 14 de la asignatura
Programación Orientada a Objetos.

Esta actividad continúa la evolución de Restaurante App iniciada
en la Semana 13.

En esta semana se aplican componentes y contenedores de Tkinter
para organizar mejor la interfaz gráfica e incorporar operaciones
de gestión sobre los productos.

La aplicación mantiene una arquitectura modular separando
modelos, servicios, persistencia e interfaz gráfica.

## Estructura

restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
└── main.py

## Componentes y contenedores utilizados

La interfaz utiliza diferentes componentes de Tkinter y ttk.

### Frame

Se utiliza para dividir la aplicación en áreas principales,
como el menú lateral y el área de contenido.

### LabelFrame

Se utiliza para agrupar visualmente el formulario de productos,
el resumen y las tablas.

### Label

Permite presentar títulos, nombres de campos e información
al usuario.

### Entry

Permite ingresar los datos de los productos:

- Código
- Nombre
- Categoría
- Precio
- Stock

### ttk.Button

Permite solicitar las diferentes acciones de la aplicación.

### ttk.Treeview

Se utiliza para mostrar productos y usuarios mediante filas
y columnas.

### ttk.Scrollbar

Permite desplazarse verticalmente cuando la cantidad de
registros supera el espacio disponible.

### messagebox

Se utiliza para presentar mensajes de confirmación y error.

## Gestión de productos

La sección Productos permite realizar las siguientes operaciones:

- Registrar un producto.
- Cargar o consultar un producto mediante su código.
- Actualizar los datos de un producto.
- Eliminar un producto.
- Limpiar el formulario.
- Visualizar los productos registrados.

## Persistencia

Los productos se almacenan en:

datos/productos.json

Las operaciones de registro, actualización y eliminación
modifican la colección del sistema y posteriormente guardan
los cambios en el archivo JSON.

ArchivoServicio es responsable de leer y escribir archivos JSON.

RestauranteServicio contiene la lógica de gestión de productos.

MainView únicamente obtiene los datos del formulario, solicita
las operaciones al servicio y actualiza la presentación.

## Usuarios

La sección Usuarios se mantiene como una vista de consulta.

Los usuarios son cargados desde:

datos/usuarios.json

## Flujo

1. Se ejecuta main.py.
2. Se crea una única ventana principal de Tkinter.
3. Se cargan productos y usuarios desde archivos JSON.
4. Se muestra LoginView.
5. El usuario ingresa sus credenciales.
6. RestauranteServicio valida el acceso.
7. Se muestra MainView.
8. El usuario puede consultar usuarios o gestionar productos.
9. Después de una operación de productos se actualiza la tabla.
10. Los cambios se conservan en productos.json.
11. Cerrar sesión regresa al LoginView utilizando la misma ventana.

## Credenciales de prueba

Usuario: admin
Contraseña: 1234

Usuario: empleado
Contraseña: abcd

## Ejecución

Ubicarse dentro de la carpeta restaurante_app y ejecutar:

python main.py