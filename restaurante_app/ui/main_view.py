import tkinter as tk
from tkinter import ttk, messagebox


class MainView(tk.Frame):

    def __init__(
        self,
        master,
        restaurante_servicio,
        usuario_actual,
        al_cerrar_sesion
    ) -> None:

        super().__init__(
            master,
            bg="#f5f5f5"
        )

        self.restaurante_servicio = (
            restaurante_servicio
        )

        self.usuario_actual = (
            usuario_actual
        )

        self.al_cerrar_sesion = (
            al_cerrar_sesion
        )

        self.frame_contenido = None

        self.producto_codigo_entry = None
        self.producto_nombre_entry = None
        self.producto_categoria_entry = None
        self.producto_precio_entry = None
        self.producto_stock_entry = None

        self.tabla_productos = None
        self.tabla_usuarios = None

        self.construir_interfaz()

    # =================================================
    # ESTRUCTURA GENERAL
    # =================================================

    def construir_interfaz(self) -> None:

        frame_sidebar = tk.Frame(
            self,
            bg="#263238",
            width=190,
            padx=16,
            pady=18
        )

        frame_sidebar.pack(
            side="left",
            fill="y"
        )

        frame_sidebar.pack_propagate(
            False
        )

        tk.Label(
            frame_sidebar,
            text="RESTAURANTE\nAPP",
            bg="#263238",
            fg="white",
            font=("Arial", 17, "bold"),
            justify="left"
        ).pack(
            anchor="w",
            pady=(0, 8)
        )

        tk.Label(
            frame_sidebar,
            text=(
                f"Usuario:\n"
                f"{self.usuario_actual.nombre}"
            ),
            bg="#263238",
            fg="white",
            font=("Arial", 10),
            justify="left"
        ).pack(
            anchor="w",
            pady=(0, 25)
        )

        ttk.Button(
            frame_sidebar,
            text="Inicio",
            command=self.mostrar_inicio
        ).pack(
            fill="x",
            pady=4
        )

        ttk.Button(
            frame_sidebar,
            text="Productos",
            command=self.mostrar_productos
        ).pack(
            fill="x",
            pady=4
        )

        ttk.Button(
            frame_sidebar,
            text="Usuarios",
            command=self.mostrar_usuarios
        ).pack(
            fill="x",
            pady=4
        )

        ttk.Separator(
            frame_sidebar,
            orient="horizontal"
        ).pack(
            fill="x",
            pady=15
        )

        ttk.Button(
            frame_sidebar,
            text="Cerrar sesión",
            command=self.cerrar_sesion
        ).pack(
            fill="x",
            pady=4
        )

        self.frame_contenido = tk.Frame(
            self,
            bg="#f5f5f5",
            padx=25,
            pady=20
        )

        self.frame_contenido.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.mostrar_inicio()

    def limpiar_contenido(self) -> None:

        for widget in (
            self.frame_contenido.winfo_children()
        ):
            widget.destroy()

    # =================================================
    # INICIO
    # =================================================

    def mostrar_inicio(self) -> None:

        self.limpiar_contenido()

        tk.Label(
            self.frame_contenido,
            text="Panel principal",
            bg="#f5f5f5",
            font=("Arial", 22, "bold")
        ).pack(
            anchor="w"
        )

        tk.Label(
            self.frame_contenido,
            text=(
                "Resumen general del sistema"
            ),
            bg="#f5f5f5",
            font=("Arial", 11)
        ).pack(
            anchor="w",
            pady=(5, 25)
        )

        resumen = tk.LabelFrame(
            self.frame_contenido,
            text="Resumen",
            bg="#f5f5f5",
            padx=20,
            pady=20
        )

        resumen.pack(
            fill="x"
        )

        tk.Label(
            resumen,
            text=(
                "Productos registrados: "
                f"{self.restaurante_servicio.cantidad_productos()}"
            ),
            bg="#f5f5f5",
            font=("Arial", 12)
        ).pack(
            anchor="w",
            pady=5
        )

        tk.Label(
            resumen,
            text=(
                "Usuarios registrados: "
                f"{self.restaurante_servicio.cantidad_usuarios()}"
            ),
            bg="#f5f5f5",
            font=("Arial", 12)
        ).pack(
            anchor="w",
            pady=5
        )

    # =================================================
    # PRODUCTOS
    # =================================================

    def mostrar_productos(self) -> None:

        self.limpiar_contenido()

        tk.Label(
            self.frame_contenido,
            text="Gestión de productos",
            bg="#f5f5f5",
            font=("Arial", 21, "bold")
        ).pack(
            anchor="w",
            pady=(0, 15)
        )

        formulario = tk.LabelFrame(
            self.frame_contenido,
            text="Datos del producto",
            bg="#f5f5f5",
            padx=15,
            pady=12
        )

        formulario.pack(
            fill="x",
            pady=(0, 12)
        )

        formulario.columnconfigure(
            1,
            weight=1
        )

        # Código
        tk.Label(
            formulario,
            text="Código",
            bg="#f5f5f5"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.producto_codigo_entry = (
            tk.Entry(formulario)
        )

        self.producto_codigo_entry.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        # Nombre
        tk.Label(
            formulario,
            text="Nombre",
            bg="#f5f5f5"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.producto_nombre_entry = (
            tk.Entry(formulario)
        )

        self.producto_nombre_entry.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        # Categoría
        tk.Label(
            formulario,
            text="Categoría",
            bg="#f5f5f5"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.producto_categoria_entry = (
            tk.Entry(formulario)
        )

        self.producto_categoria_entry.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        # Precio
        tk.Label(
            formulario,
            text="Precio",
            bg="#f5f5f5"
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.producto_precio_entry = (
            tk.Entry(formulario)
        )

        self.producto_precio_entry.grid(
            row=3,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        # Stock
        tk.Label(
            formulario,
            text="Stock",
            bg="#f5f5f5"
        ).grid(
            row=4,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.producto_stock_entry = (
            tk.Entry(formulario)
        )

        self.producto_stock_entry.grid(
            row=4,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        # Botones
        acciones = tk.Frame(
            formulario,
            bg="#f5f5f5"
        )

        acciones.grid(
            row=5,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(12, 0)
        )

        ttk.Button(
            acciones,
            text="Registrar",
            command=self.registrar_producto
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            acciones,
            text="Cargar / Consultar",
            command=self.cargar_producto_en_formulario
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            acciones,
            text="Actualizar",
            command=self.actualizar_producto
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            acciones,
            text="Eliminar",
            command=self.eliminar_producto
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            acciones,
            text="Limpiar",
            command=self.limpiar_formulario_producto
        ).pack(
            side="left",
            padx=4
        )

        # ---------------------------------------------
        # TABLA
        # ---------------------------------------------

        contenedor_tabla = tk.LabelFrame(
            self.frame_contenido,
            text="Productos registrados",
            padx=10,
            pady=10
        )

        contenedor_tabla.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "codigo",
            "nombre",
            "categoria",
            "precio",
            "stock"
        )

        self.tabla_productos = ttk.Treeview(
            contenedor_tabla,
            columns=columnas,
            show="headings"
        )

        self.tabla_productos.heading(
            "codigo",
            text="Código"
        )

        self.tabla_productos.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_productos.heading(
            "categoria",
            text="Categoría"
        )

        self.tabla_productos.heading(
            "precio",
            text="Precio"
        )

        self.tabla_productos.heading(
            "stock",
            text="Stock"
        )

        self.tabla_productos.column(
            "codigo",
            width=80,
            anchor="center"
        )

        self.tabla_productos.column(
            "nombre",
            width=180
        )

        self.tabla_productos.column(
            "categoria",
            width=140
        )

        self.tabla_productos.column(
            "precio",
            width=90,
            anchor="center"
        )

        self.tabla_productos.column(
            "stock",
            width=80,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            contenedor_tabla,
            orient="vertical",
            command=self.tabla_productos.yview
        )

        self.tabla_productos.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tabla_productos.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.refrescar_productos()

    def obtener_datos_producto(self):

        return (
            self.producto_codigo_entry.get().strip(),
            self.producto_nombre_entry.get().strip(),
            self.producto_categoria_entry.get().strip(),
            self.producto_precio_entry.get().strip(),
            self.producto_stock_entry.get().strip()
        )

    def registrar_producto(self) -> None:

        try:

            self.restaurante_servicio.registrar_producto(
                *self.obtener_datos_producto()
            )

            self.refrescar_productos()
            self.limpiar_formulario_producto()

            messagebox.showinfo(
                "Productos",
                "Producto registrado correctamente."
            )

        except ValueError as error:

            messagebox.showerror(
                "Productos",
                str(error)
            )

    def cargar_producto_en_formulario(
        self
    ) -> None:

        try:

            codigo = (
                self.producto_codigo_entry
                .get()
                .strip()
            )

            producto = (
                self.restaurante_servicio
                .buscar_producto_por_codigo(
                    codigo
                )
            )

            if producto is None:

                raise ValueError(
                    "No existe un producto "
                    "con ese código."
                )

            self.limpiar_formulario_producto()

            self.producto_codigo_entry.insert(
                0,
                producto.codigo
            )

            self.producto_nombre_entry.insert(
                0,
                producto.nombre
            )

            self.producto_categoria_entry.insert(
                0,
                producto.categoria
            )

            self.producto_precio_entry.insert(
                0,
                str(producto.precio)
            )

            self.producto_stock_entry.insert(
                0,
                str(producto.stock)
            )

        except ValueError as error:

            messagebox.showerror(
                "Productos",
                str(error)
            )

    def actualizar_producto(self) -> None:

        try:

            self.restaurante_servicio.actualizar_producto(
                *self.obtener_datos_producto()
            )

            self.refrescar_productos()
            self.limpiar_formulario_producto()

            messagebox.showinfo(
                "Productos",
                "Producto actualizado correctamente."
            )

        except ValueError as error:

            messagebox.showerror(
                "Productos",
                str(error)
            )

    def eliminar_producto(self) -> None:

        try:

            codigo = (
                self.producto_codigo_entry
                .get()
                .strip()
            )

            producto = (
                self.restaurante_servicio
                .buscar_producto_por_codigo(
                    codigo
                )
            )

            if producto is None:

                raise ValueError(
                    "No existe un producto "
                    "con ese código."
                )

            confirmar = (
                messagebox.askyesno(
                    "Productos",
                    (
                        "¿Desea eliminar el producto "
                        f"{producto.nombre}?"
                    )
                )
            )

            if not confirmar:
                return

            self.restaurante_servicio.eliminar_producto(
                codigo
            )

            self.refrescar_productos()
            self.limpiar_formulario_producto()

            messagebox.showinfo(
                "Productos",
                "Producto eliminado correctamente."
            )

        except ValueError as error:

            messagebox.showerror(
                "Productos",
                str(error)
            )

    def limpiar_formulario_producto(
        self
    ) -> None:

        entradas = (
            self.producto_codigo_entry,
            self.producto_nombre_entry,
            self.producto_categoria_entry,
            self.producto_precio_entry,
            self.producto_stock_entry
        )

        for entrada in entradas:

            entrada.delete(
                0,
                tk.END
            )

        self.producto_codigo_entry.focus()

    def refrescar_productos(self) -> None:

        for item in (
            self.tabla_productos.get_children()
        ):
            self.tabla_productos.delete(
                item
            )

        for producto in (
            self.restaurante_servicio
            .listar_productos()
        ):

            self.tabla_productos.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:.2f}",
                    producto.stock
                )
            )

    # =================================================
    # USUARIOS
    # =================================================

    def mostrar_usuarios(self) -> None:

        self.limpiar_contenido()

        tk.Label(
            self.frame_contenido,
            text="Usuarios registrados",
            bg="#f5f5f5",
            font=("Arial", 21, "bold")
        ).pack(
            anchor="w",
            pady=(0, 15)
        )

        contenedor_tabla = tk.LabelFrame(
            self.frame_contenido,
            text="Consulta de usuarios",
            padx=10,
            pady=10
        )

        contenedor_tabla.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "identificacion",
            "nombre",
            "correo",
            "usuario"
        )

        self.tabla_usuarios = ttk.Treeview(
            contenedor_tabla,
            columns=columnas,
            show="headings"
        )

        self.tabla_usuarios.heading(
            "identificacion",
            text="Identificación"
        )

        self.tabla_usuarios.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_usuarios.heading(
            "correo",
            text="Correo"
        )

        self.tabla_usuarios.heading(
            "usuario",
            text="Usuario"
        )

        self.tabla_usuarios.column(
            "identificacion",
            width=110,
            anchor="center"
        )

        self.tabla_usuarios.column(
            "nombre",
            width=180
        )

        self.tabla_usuarios.column(
            "correo",
            width=220
        )

        self.tabla_usuarios.column(
            "usuario",
            width=120,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            contenedor_tabla,
            orient="vertical",
            command=self.tabla_usuarios.yview
        )

        self.tabla_usuarios.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tabla_usuarios.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.refrescar_usuarios()

    def refrescar_usuarios(self) -> None:

        for item in (
            self.tabla_usuarios.get_children()
        ):
            self.tabla_usuarios.delete(
                item
            )

        for usuario in (
            self.restaurante_servicio
            .listar_usuarios()
        ):

            self.tabla_usuarios.insert(
                "",
                tk.END,
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.correo,
                    usuario.usuario
                )
            )

    # =================================================
    # SESIÓN
    # =================================================

    def cerrar_sesion(self) -> None:

        self.al_cerrar_sesion()