from  media import media1
from mediana import mediana1
from varianca import varianca1
from desvio import desvio1
from moda import moda1



empresa2 = [5000,4000,3000,2000,7000]


def handle(lista, salarios):

    print('EMPRESA', salarios)
    print('----------------------------')
    media1(lista)
    mediana1(lista)
    moda1(lista)
    varianca1(lista)
    desvio1(lista)
  
handle(empresa2, empresa2)   
