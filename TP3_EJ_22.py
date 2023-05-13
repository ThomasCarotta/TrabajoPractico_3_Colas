from Operaciones_cola import Cola

#22_ Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce 
# el nombre del personaje, el nombre del superhéroe y su género (Masculino M y FemeninoF) 
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, 
# etc., desarrollar un algoritmo que resuelva las siguientes actividades:
#A_determinar el nombre del personaje de la superhéroe Capitana Marvel;
#B_mostrar los nombre de los superhéroes femeninos;
#C_mostrar los nombres de los personajes masculinos;
#D_determinar el nombre del superhéroe del personaje Scott Lang;
#E_mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
#F_determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

cola=Cola()

superheroes=[{"Nombre_P":"Tony Stark","Nombre_S":"Iron Man","Genero":"M"},
             {"Nombre_P":"Steve Rogers","Nombre_S":"Capitan America","Genero":"M"},
             {"Nombre_P":"Natasha Romanoff","Nombre_S":"Black Widow","Genero":"F"},
             {"Nombre_P":"Carol Danvers","Nombre_S":"Capitana Marvel","Genero":"F"},
             {"Nombre_P":"Scott Lang","Nombre_S":"Ant Man","Genero":"M"},
             {"Nombre_P":"Peter Parker ","Nombre_S":"Spider Man","Genero":"M"},
             {"Nombre_P":"Stephen Strange","Nombre_S":"Doctor Strange","Genero":"M"},
             {"Nombre_P":"Wanda Maximoff","Nombre_S":"Scarlet Witch","Genero":"F"},]

for personajes in superheroes:
    cola.arrive(personajes)

while cola.size()>0:
    superhero=cola.atention()
    if (superhero["Nombre_S"]=="Capitana Marvel"):
        print(f'el nombre de la Capitana Marvel es {superhero["Nombre_P"]}')

    if (superhero["Genero"]=="F"):
        print(f'Nombre de la superheroina: {superhero["Nombre_S"]} ')

    if (superhero["Genero"]=="M"):
        print(f'Nombre del personaje: {superhero["Nombre_P"]}')

    if (superhero["Nombre_P"]=="Scott Lang"):
        print(f'el nombre de Scott Lang es {superhero["Nombre_S"]}')

    if (superhero["Nombre_P"][0]=='S') or (superhero["Nombre_S"][0]=='S'):
        print(superhero)

    if (superhero["Nombre_P"]=="Carol Danvers"):
        print(f'Carol Danvers, {superhero["Nombre_S"]}, se encuentra en la cola')
    