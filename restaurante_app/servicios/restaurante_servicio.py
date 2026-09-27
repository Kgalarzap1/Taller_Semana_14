from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(
        self,
        archivo_servicio: ArchivoServicio
    ) -> None:

        self.archivo_servicio = (
            archivo_servicio
        )

        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []

        self._indice_productos: dict[
            str, Producto
        ] = {}

        self._indice_usuarios: dict[
            str, Usuario
        ] = {}

        self._indice_acceso: dict[
            str, Usuario
        ] = {}

        self.cargar_datos()

    def cargar_datos(self) -> None:

        datos_productos = (
            self.archivo_servicio.leer_json(
                "productos.json"
            )
        )

        datos_usuarios = (
            self.archivo_servicio.leer_json(
                "usuarios.json"
            )
        )

        self._productos = [
            Producto(
                dato["codigo"],
                dato["nombre"],
                dato["categoria"],
                float(dato["precio"]),
                int(dato["stock"])
            )
            for dato in datos_productos
        ]

        self._usuarios = [
            Usuario(
                dato["identificacion"],
                dato["nombre"],
                dato["correo"],
                dato["usuario"],
                dato["contrasena"]
            )
            for dato in datos_usuarios
        ]

        self._reconstruir_indices()

    def _reconstruir_indices(self) -> None:

        self._indice_productos = {
            producto.codigo: producto
            for producto in self._productos
        }

        self._indice_usuarios = {
            usuario.identificacion: usuario
            for usuario in self._usuarios
        }

        self._indice_acceso = {
            usuario.usuario: usuario
            for usuario in self._usuarios
        }

    # -------------------------------------------------
    # LOGIN
    # -------------------------------------------------

    def validar_acceso(
        self,
        nombre_usuario: str,
        contrasena: str
    ) -> Usuario | None:

        usuario = self._indice_acceso.get(
            nombre_usuario
        )

        if usuario is None:
            return None

        if usuario.contrasena != contrasena:
            return None

        return usuario

    # -------------------------------------------------
    # CONSULTAS GENERALES
    # -------------------------------------------------

    def listar_productos(
        self
    ) -> list[Producto]:

        return list(self._productos)

    def listar_usuarios(
        self
    ) -> list[Usuario]:

        return list(self._usuarios)

    def cantidad_productos(self) -> int:

        return len(self._productos)

    def cantidad_usuarios(self) -> int:

        return len(self._usuarios)

    # -------------------------------------------------
    # PERSISTENCIA DE PRODUCTOS
    # -------------------------------------------------

    def guardar_productos(self) -> None:

        datos = [
            producto.a_diccionario()
            for producto in self._productos
        ]

        self.archivo_servicio.escribir_json(
            "productos.json",
            datos
        )

    # -------------------------------------------------
    # BUSCAR PRODUCTO
    # -------------------------------------------------

    def buscar_producto_por_codigo(
        self,
        codigo: str
    ) -> Producto | None:

        codigo = codigo.strip()

        if not codigo:
            raise ValueError(
                "Ingrese el código del producto."
            )

        return self._indice_productos.get(
            codigo
        )

    # -------------------------------------------------
    # REGISTRAR
    # -------------------------------------------------

    def registrar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio,
        stock
    ) -> Producto:

        codigo = codigo.strip()

        if codigo in self._indice_productos:

            raise ValueError(
                "Ya existe un producto "
                "con ese código."
            )

        try:
            precio = float(precio)
        except (ValueError, TypeError):
            raise ValueError(
                "El precio debe ser un número válido."
            )

        try:
            stock = int(stock)
        except (ValueError, TypeError):
            raise ValueError(
                "El stock debe ser un número entero."
            )

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        self._productos.append(
            producto
        )

        self._reconstruir_indices()
        self.guardar_productos()

        return producto

    # -------------------------------------------------
    # ACTUALIZAR
    # -------------------------------------------------

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio,
        stock
    ) -> Producto:

        codigo = codigo.strip()

        producto_existente = (
            self._indice_productos.get(
                codigo
            )
        )

        if producto_existente is None:

            raise ValueError(
                "No existe un producto "
                "con ese código."
            )

        try:
            precio = float(precio)
        except (ValueError, TypeError):
            raise ValueError(
                "El precio debe ser un número válido."
            )

        try:
            stock = int(stock)
        except (ValueError, TypeError):
            raise ValueError(
                "El stock debe ser un número entero."
            )

        producto_actualizado = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        posicion = self._productos.index(
            producto_existente
        )

        self._productos[posicion] = (
            producto_actualizado
        )

        self._reconstruir_indices()
        self.guardar_productos()

        return producto_actualizado

    # -------------------------------------------------
    # ELIMINAR
    # -------------------------------------------------

    def eliminar_producto(
        self,
        codigo: str
    ) -> None:

        codigo = codigo.strip()

        producto = (
            self._indice_productos.get(
                codigo
            )
        )

        if producto is None:

            raise ValueError(
                "No existe un producto "
                "con ese código."
            )

        self._productos.remove(
            producto
        )

        self._reconstruir_indices()
        self.guardar_productos()