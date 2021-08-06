import random
def Narrativa():
    print(''' 
Te encuentras entrando a una cueva,
ahí has varios enemigos que tendras 
que derrotar para ganar. A traves de 
los niveles vas a ir aprendiendo habilidades, 
ahora solo cuentas con tu ataque basico que hace 20 de daño.
Enter para continuar''')
    input()
    print('''
Ya va a empezar tu primera pelea, preparate 
Enter para continuar''')
    input()

def enemigo1():
    Vida = 100
    Daño = 5
    Esquivar = 30
    return Vida,Daño,Esquivar

def enemigo2():
    Vida = 100
    Daño = 15
    Esquivar = 20
    return Vida,Daño,Esquivar

def enemigo3():
    Vida = 200
    Daño = 25
    Esquivar = 15
    return Vida,Daño,Esquivar

def personaje():
    Vida = 150
    ataques = {'Basico':20}
    Esquivar = 13
    return Vida,ataques,Esquivar

def combate(vida,ataques,esquivar,vidaEnemigo,dañoEnemigo,esquivarEnemigo):
    combate_sigue = True
    usos = 0
    turno = 0
    while combate_sigue == True:
        accion = 0
        while accion not in ataques.keys():
            if usos ==2:
                del ataques[curacion]
            print(f'''Que quieres hacer jugador, aqui tus ataques y el daño o en algunas curación {ataques} 
            y te faltan {turno} para el ataque especial''')
            accion= input()

        if accion == 'Basico':
            if random.randint(1,esquivarEnemigo) != esquivarEnemigo:
                daño = ataques[accion]
                vidaEnemigo -= daño
                if vidaEnemigo <= 0:
                    print('Has logrado vencerlo')
                    combate_sigue == False
                    return 'Victoria', vida
            else:
                print('El enemigo lo ha esquivado')

        elif accion == 'Curacion' :
            curacion = ataques[accion]
            vida += curacion
            usos += 1
        
        elif accion == 'Especial' and turno <=0 :
            turno = 3
            if random.randint(1,esquivarEnemigo) != esquivarEnemigo:
                daño = ataques[accion]
                vidaEnemigo -= daño
                if vidaEnemigo <= 0:
                    print('Has logrado vencerlo')
                    combate_sigue == False
                    return 'Victoria', vida
            else:
                print('El enemigo lo ha esquivado')
        
        else: 
            print('Como tu especial estaba en cooldown se hizo un ataque basico')
            if random.randint(1,esquivarEnemigo) != esquivarEnemigo:
                daño = ataques[accion]
                vidaEnemigo -= daño
                if vidaEnemigo <= 0:
                    print('Has logrado vencerlo')
                    combate_sigue == False
                    return 'Victoria', vida
            else:
                print('El enemigo lo ha esquivado')

        if vidaEnemigo >= 1:
            print(f'Ahora va el turno del enemigo con daño {dañoEnemigo}')
            if random.randint(1,esquivar) != esquivar:
                vida -= dañoEnemigo
                if vida <= 0:
                    print('Has perdido')
                    combate_sigue == False
                    return 'Derrota', vida
            else:
                print('Has logrado esquivarlo')
        print(f'''
        Recuento de los datos: 
        tienes {vida} puntos de vida y 
        el enemigo tiene {vidaEnemigo} puntos de vida
        ''')
        if turno != 0:
            turno -=1 

def acabar_combate(ataques):
    print('''
    Como has acabado el combate victorio se te da la 
    opción de escojer una habilidad. 
    Está Ataque Especial con 50 puntos de daño, pero con 3 turnos de espera
    o Curacion que te da 20 de vida y solo se puede usar 2 veces por juego
    Escribe 1 para Ataque Especial o 2 para Curacion''')
    nuevo = input()
    if nuevo == '1':
        ataques['Especial'] = 50
    else: 
        ataques['Curacion'] = 20
    return ataques


def combate(vida,ataques,esquivar,vidaEnemigo,dañoEnemigo,esquivarEnemigo):
    combate_sigue = True
    usos = 0
    turno = 0
    while combate_sigue == True:
        accion = 0
        while accion not in ataques.keys():
            if usos ==2:
                del ataques[curacion]
            print(f'''Que quieres hacer jugador, aqui tus ataques y el daño o en algunas curación {ataques} 
            y te faltan {turno} para el ataque especial''')
            accion= input()

        if accion == 'Basico':
            if random.randint(1,esquivarEnemigo) != esquivarEnemigo:
                daño = ataques[accion]
                vidaEnemigo -= daño
                if vidaEnemigo == 0:
                    print('Has logrado vencerlo')
                    combate_sigue == False
                    return 'Victoria', vida
            else:
                print('El enemigo lo ha esquivado')

        elif accion == 'Curacion' :
            curacion = ataques[accion]
            vida += curacion
            usos += 1
        
        elif accion == 'Especial' and turno <=0 :
            turno = 3
            if random.randint(1,esquivarEnemigo) != esquivarEnemigo:
                daño = ataques[accion]
                vidaEnemigo -= daño
                if vidaEnemigo == 0:
                    print('Has logrado vencerlo')
                    combate_sigue == False
                    return 'Victoria', vida
            else:
                print('El enemigo lo ha esquivado')
        
        else: 
            print('Como tu especial estaba en cooldown se hizo un ataque basico')
            if random.randint(1,esquivarEnemigo) != esquivarEnemigo:
                daño = ataques[accion]
                vidaEnemigo -= daño
                if vidaEnemigo == 0:
                    print('Has logrado vencerlo')
                    combate_sigue == False
                    return 'Victoria', vida
            else:
                print('El enemigo lo ha esquivado')

        if vidaEnemigo != 0:
            print(f'Ahora va el turno del enemigo con daño {dañoEnemigo}')
            if random.randint(1,esquivar) != esquivar:
                vida -= dañoEnemigo
                if vida == 0:
                    print('Has perdido')
                    combate_sigue == False
                    return 'Derrota', vida
            else:
                print('Has logrado esquivarlo')
        print(f'''
        Recuento de los datos: 
        tienes {vida} puntos de vida y 
        el enemigo tiene {vidaEnemigo} puntos de vida
        ''')
        turno -=1 