class base:
    def __init__(self):
        self.ingredientes = []

    def inicializar(self):
        pass

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def obtener_ingredientes_base(self):
        return self.ingredientes
    def precio_base(self):
        return 5.0
    def obtener_precio(self):
        return self.precio_base()
    def __str__(self):
        return f"Café con ingredientes: {', '.join(self.ingredientes)} y precio base: {self.precio_base()}"
    def __repr__(self):
        return self.__str__()
    