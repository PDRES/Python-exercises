from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#0 creo los objetos 
caja= MoneyMachine()
cafetera= CoffeeMaker()
menu = Menu()
#1 Voy a crear un ticket, llamo al metodo especifico del objeto caja 

caja.report()
cafetera.report()

flag = True

while flag: 
    opciones =menu.get_items()
    choice = input(f"Que te gustaria tomar de esta lista ?({opciones}) :")

    #Las dos primeras opciones no tienen mucho sentido
    if choice == 'off': #apagar maquina
        flag = False
    elif choice == "report": #sacar informes. lat
        #aqui imprimimos el informe de la cafetera y de la caja 
        cafetera.report()
        caja.report()
    else: 
        bebida= menu.find_drink(choice)
        if cafetera.is_resource_sufficient(bebida) and (caja.make_payment(bebida.cost)):
            cafetera.make_coffee(bebida)

