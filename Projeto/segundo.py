class bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        self.marhca = 1

    def buzinar(self):
        print("PLIM PLIM...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("VRUUUUUUMM!!!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.parar()
b1.correr()

print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = bicicleta("verde", "monark", 2023, 900)
print(b2)
