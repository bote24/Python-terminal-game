import Funciones
import sys
E1V, E1D, E1E = Funciones.enemigo1()
E2V, E2D, E2E = Funciones.enemigo2()
E3V, E3D, E3E = Funciones.enemigo3()
personajeVida, personajeAtaques, personajeEsquivar =Funciones.personaje()
Funciones.Narrativa()

resultado, personajeVida =Funciones.combate(personajeVida, personajeAtaques, personajeEsquivar,E1V, E1D, E1E)
if resultado == 'Derrota':
    sys.exit()
personajeAtaques= Funciones.acabar_combate(personajeAtaques)

resultado, personajeVida =Funciones.combate(personajeVida, personajeAtaques, personajeEsquivar,E2V, E2D, E2E)
if resultado == 'Derrota':
    sys.exit()
personajeAtaques= Funciones.acabar_combate(personajeAtaques)

resultado, personajeVida =Funciones.combate(personajeVida, personajeAtaques, personajeEsquivar,E3V, E3D, E3E)
if resultado == 'Derrota':
    sys.exit()
print('Has acabado el juego, gracias por jugar')
