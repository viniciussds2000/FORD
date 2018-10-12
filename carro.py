class Carro:
    def __init__(self,modelo,marca,ano,preco,estado,placa):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.preco = preco
        self.estado = estado
        self.placa = placa
        self.comprador = None
        self.vendedor = None
    def registrar_venda(self,comprador,vendedor):
        self.comprador = comprador
        self.vendedor = vendedor
    def get_modelo(self,modelo):
        return self.modelo