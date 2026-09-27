class Usuario:

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        usuario: str,
        contrasena: str
    ) -> None:

        if not identificacion.strip():
            raise ValueError(
                "La identificación no puede estar vacía."
            )

        if not nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not correo.strip():
            raise ValueError(
                "El correo no puede estar vacío."
            )

        if not usuario.strip():
            raise ValueError(
                "El usuario no puede estar vacío."
            )

        if not contrasena.strip():
            raise ValueError(
                "La contraseña no puede estar vacía."
            )

        self.identificacion = identificacion.strip()
        self.nombre = nombre.strip()
        self.correo = correo.strip()
        self.usuario = usuario.strip()
        self.contrasena = contrasena.strip()

    def a_diccionario(self) -> dict:

        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "usuario": self.usuario,
            "contrasena": self.contrasena
        }

    def __str__(self) -> str:

        return (
            f"{self.identificacion} | "
            f"{self.nombre} | "
            f"{self.correo} | "
            f"Usuario: {self.usuario}"
        )