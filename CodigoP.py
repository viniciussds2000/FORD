from Concessionaria import Concessionaria
from carro import Carro

v12= Concessionaria("V12 MOTORS")

print(v12.get_nome())
print(v12.get_carros())


up = Carro("up","VW",2018,20000,"NOVO","PPP101")

v12.add_carro(up)

print(v12.get_carros()[0].get_modelo())

mobi=("MOBI","FIAT",2017,17000,"USADO","GOD777")

for carro in v12.get_carros():
    print(item.get_placa())
