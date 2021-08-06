import Funciones
import sys
E1V, E1D, E1E = Funciones.enemigo1()
E2V, E2D, E2E = Funciones.enemigo2()
E3V, E3D, E3E = Funciones.enemigo3()
personajeVida, personajeAtaques, personajeEsquivar =Funciones.personaje()
Funciones.Narrativa()
print(f'Ahora iras contra el segundo enemigo con {E1V} puntos de vida y {E1D} puntos de daño')
resultado, personajeVida =Funciones.combate(personajeVida, personajeAtaques, personajeEsquivar,E1V, E1D, E1E)
if resultado == 'Derrota':
    sys.exit()
personajeAtaques= Funciones.acabar_combate(personajeAtaques)
print(f'Ahora iras contra el segundo enemigo con {E2V} puntos de vida y {E2D} puntos de daño')
resultado, personajeVida =Funciones.combate(personajeVida, personajeAtaques, personajeEsquivar,E2V, E2D, E2E)
if resultado == 'Derrota':
    sys.exit()
personajeAtaques= Funciones.acabar_combate(personajeAtaques)
print(f'Ahora iras contra el segundo enemigo con {E3V} puntos de vida y {E3D} puntos de daño')
resultado, personajeVida =Funciones.combate(personajeVida, personajeAtaques, personajeEsquivar,E3V, E3D, E3E)
if resultado == 'Derrota':
    sys.exit()
print('Has acabado el juego, gracias por jugar')
