import tkinter as tk
from tkinter import ttk


class LoginView(tk.Frame):

    def __init__(
        self,
        master,
        restaurante_servicio,
        al_iniciar_sesion
    ) -> None:

        super().__init__(
            master,
            bg="#eef3f8"
        )

        self.restaurante_servicio = (
            restaurante_servicio
        )

        self.al_iniciar_sesion = (
            al_iniciar_sesion
        )

        self.usuario_entry = None
        self.contrasena_entry = None
        self.mensaje_error = None

        self.definir_estilos()
        self.construir_interfaz()

    def definir_estilos(self) -> None:

        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "Login.TButton",
            font=("Arial", 11, "bold"),
            padding=(14, 8)
        )

    def construir_interfaz(self) -> None:

        contenedor = tk.Frame(
            self,
            bg="white",
            padx=35,
            pady=30
        )

        contenedor.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        tk.Label(
            contenedor,
            text="RESTAURANTE APP",
            bg="white",
            font=("Arial", 22, "bold")
        ).pack(
            pady=(0, 5)
        )

        tk.Label(
            contenedor,
            text="Inicio de sesión",
            bg="white",
            font=("Arial", 11)
        ).pack(
            pady=(0, 20)
        )

        tk.Label(
            contenedor,
            text="Usuario",
            bg="white",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w"
        )

        self.usuario_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 11)
        )

        self.usuario_entry.pack(
            pady=(5, 15),
            ipady=4
        )

        tk.Label(
            contenedor,
            text="Contraseña",
            bg="white",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w"
        )

        self.contrasena_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 11),
            show="*"
        )

        self.contrasena_entry.pack(
            pady=(5, 10),
            ipady=4
        )

        self.mensaje_error = tk.Label(
            contenedor,
            text="",
            bg="white",
            fg="red",
            font=("Arial", 10)
        )

        self.mensaje_error.pack(
            pady=(0, 10)
        )

        ttk.Button(
            contenedor,
            text="Iniciar sesión",
            command=self.iniciar_sesion,
            style="Login.TButton"
        ).pack(
            fill="x"
        )

        self.contrasena_entry.bind(
            "<Return>",
            lambda evento: self.iniciar_sesion()
        )

        self.usuario_entry.focus()

    def iniciar_sesion(self) -> None:

        nombre_usuario = (
            self.usuario_entry.get().strip()
        )

        contrasena = (
            self.contrasena_entry.get().strip()
        )

        if not nombre_usuario or not contrasena:

            self.mensaje_error.config(
                text="Ingrese usuario y contraseña."
            )

            return

        usuario = (
            self.restaurante_servicio
            .validar_acceso(
                nombre_usuario,
                contrasena
            )
        )

        if usuario is None:

            self.mensaje_error.config(
                text="Credenciales incorrectas."
            )

            return

        self.mensaje_error.config(
            text=""
        )

        self.al_iniciar_sesion(
            usuario
        )