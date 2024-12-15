#Generador de soldados para el juego NUTS!
import random
def habilidades():
    habilidades = ("Agile(1,1)", "Athlete(1,2)", "Ball Player(1,3)", "Born Leader(1,4)", "Brawler(1,5)", "Clumsy(1,6)",
                   "Coward(2,1)", "Crack Shot(2,2)", "Dumbass(2,3)", "Fast(2,4)", "Greedy(2,5)", "Hard as Nails(2,6)",
                   "Initiative(3,1)", "Knifeman(3,2)", "Lucky(3,3)", "Marksman(3,4)", "Near Sigthed(3,5)",
                   "Nerves of Steel(3,6)",
                   "No Attribute(4,1)", "Poser(4,2)", "Quick Reflexes(4,3)", "Rage(4,4)", "Resilient(4,5)", "Runt(4,6)",
                   "Shirker(5,1)", "Sickly(5,2)","Slow(5,3)", "Slow to react(5,4)", "Stealthy(5,5)", "Steely Eyes(5,6)",
                   "Stone Cold(6,1)", "Tank Killer(6,2)", "Tough(6,3)", "Unlucky(6,4)", "Wussy(6,5)", "Choice(6,6)")
    attribute = random.choice(habilidades)
    return attribute

dice = (1,2,3,4,5,6)
#Creamos el dado para luego "lanzarlo" y asi obtener valores de 1 a 6.
#print(random.choice(dice)) #prueba
ejercito = int(input("Presiona 1 para EEUU, 2 para Reino Unido, 3 para Alemania, 4 para la Union Soviética: "))
#Estadounidenses
if ejercito == 1:
    tipo = int(input("Presiona 1 para Infantería, 2 para Rangers, 3 para Paracaídistas: "))
    names = ("Joe", "Ron", "Clint", "Arnie", "Phil", "John", "Paul", "Wade", "Tony", "Harry",
             "Mickey", "Alan", "Chris", "Tom", "Chip", "Dave", "Don", "Lee", "Steve", "Dan",
             "Al", "Bernie", "Jim", "Johnie", "Charlie", "Ed", "Clancy", "Andy", "Vic", "Red",
             "Carl", "Gus", "Roy", "Frank", "Woody", "George", "Ben", "Fred", "Walt", "Henry",
             "Abe", "Dick")
    if tipo == 1:
        print("Escuadra de Infantería")
        troop = range(12)
        for i in troop:
            a = random.choice(dice)
            if a == 1 or a == 2:
                rep = 3
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            elif a == 3 or a == 4 or a == 5:
                rep = 4
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            else:
                rep = 5
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
    elif tipo == 2:
        print("Escuadra de Rangers")
        troop = range(11)
        for i in troop:
            a = random.choice(dice)
            if a == 1 or a == 2:
                rep = 4
                name = random.choice(names)
                hab = habilidades()
                print(i + 1, name, rep, hab)
            elif a == 3 or a == 4 or a == 5:
                rep = 5
                name = random.choice(names)
                hab = habilidades()
                print(i + 1, name, rep, hab)
            else:
                rep = 6
                name = random.choice(names)
                hab = habilidades()
                print(i + 1, name, rep, hab)
    elif tipo == 3:
        print("Escuadra de Paracaídistas")
        troop = range(12)
        for i in troop:
            a = random.choice(dice)

            if a == 1 or a == 2:
                rep = 4
                name = random.choice(names)
                hab = habilidades()
                print(i + 1, name, rep, hab)
            elif a == 3 or a == 4 or a == 5:
                rep = 5
                name = random.choice(names)
                hab = habilidades()
                print(i + 1, name, rep, hab)
            else:
                rep = 6
                name = random.choice(names)
                hab = habilidades()
                print(i + 1, name, rep, hab)
    else:
        print("Por favor, selecciona una opción válida")

#Británicos
if ejercito == 2:
    tipo = int(input("Presiona 1 para Infantería, 2 para Infantería(1945), 3 para Paracaídistas, 4 para Comandos, "
                     "5 para Infantería en planeador: "))
    names = ("Joseph", "Ronald", "Arnold", "Philip", "John", "Paul", "Harold", "Thomas", "Christopher", "Jack",
             "Robert", "Clarence", "David", "Donald", "Steven", "Daniel", "Edmund", "Edward", "Thomas", "Archivald",
             "Bernard", "James", "Thomas", "Charles", "Ed", "Clancy", "Andrew", "Victor", "Raymond", "Percivald",
             "Charles", "Roger", "Frank", "George", "Benjamin", "Alfred", "Walter", "Henry", "Alexander", "Jack",
             "Richard", "Thomas")
    if tipo == 1:
        print("Escuadra de Infantería")
        troop = range(10)
        for i in troop:
            a = random.choice(dice)
            if a == 1:
                rep = 3
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            elif a == 2 or a == 3 or a == 4 or a == 5:
                rep = 4
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            else:
                rep = 5
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
    elif tipo == 2:
        print("Escuadra de Infantería(1945)")
        troop = range(8)
        for i in troop:
            a = random.choice(dice)
            if a == 1 or a == 2:
                rep = 3
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            elif a == 3 or a == 4 or a == 5:
                rep = 4
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            else:
                rep = 5
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
    elif tipo == 3:
        print("Escuadra de Paracaídistas")
        troop = range(10)
        for i in troop:
            a = random.choice(dice)
            if a == 1 or a == 2:
                rep = 4
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            elif a == 3 or a == 4 or a == 5:
                rep = 5
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            else:
                rep = 6
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
    elif tipo == 4:
        print("Escuadra de Comandos")
        troop = range(10)
        for i in troop:
            a = random.choice(dice)
            if a == 1 or a == 2:
                rep = 4
                name = random.choice(names)
                hab = habilidades()
                print(i + 1, name, rep, hab)
            elif a == 3 or a == 4 or a == 5:
                rep = 5
                name = random.choice(names)
                hab = habilidades()
                print(i + 1, name, rep, hab)
            else:
                rep = 6
                name = random.choice(names)
                hab = habilidades()
                print(i + 1, name, rep, hab)
    elif tipo == 5:
        print("Escuadra de Infantería en planeador")
        troop = range(10)
        for i in troop:
            a = random.choice(dice)
            if a == 1 or a == 2:
                rep = 4
                name = random.choice(names)
                hab = habilidades()
                print(i + 1, name, rep, hab)
            elif a == 3 or a == 4 or a == 5:
                rep = 5
                name = random.choice(names)
                hab = habilidades()
                print(i + 1, name, rep, hab)
            else:
                rep = 6
                name = random.choice(names)
                hab = habilidades()
                print(i + 1, name, rep, hab)
    else:
        print("Por favor, selecciona una opción válida")

#Alemanes
if ejercito == 3:
    tipo = int(input("Presiona 1 para Infantería, 2 para Volksgrenadiers, 3 para Panzergrenadiers, 4 para Paracaídistas: "))
    names = ("Ludwig", "Otto", "Erwin", "Bruno", "Wolf", "Rolf", "Paul", "Thomas", "Karl", "Fritz",
             "Klaus", "Conrad", "Wilhelm", "Helmut", "Albrecht", "Franz", "Dieter", "Dietrich", "Hans",
             "Christoph", "Gustav", "Thorvald", "Ernst", "Albert", "Manfred", "Erich", "Adolph",
             "Leopold", "Emil", "Günther", "Werner", "Heinz", "Johann", "Arnold", "Jorgen", "Kurt",
             "Reinhart", "Lothar", "Gerd")
    if tipo == 1:
        print("Escuadra de Infantería")
        troop = range(10)
        for i in troop:
            a = random.choice(dice)
            if a == 1:
                rep = 3
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            elif a == 2 or a == 3 or a == 4 or a == 5:
                rep = 4
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            else:
                rep = 5
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
    elif tipo == 2:
        print("Escuadra de VolksGrenadiers")
        troop = range(10)
        for i in troop:
            a = random.choice(dice)
            if a == 1 or a == 2 or a == 3:
                rep = 3
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            elif a == 4 or a == 5:
                rep = 4
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            else:
                rep = 5
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
    elif tipo == 3:
        print("Escuadra de Panzergrenadiers")
        troop = range(9)
        for i in troop:
            a = random.choice(dice)
            if a == 1:
                rep = 3
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            elif a == 2 or a == 3 or a == 4:
                rep = 4
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            else:
                rep = 5
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
    elif tipo == 4:
        print("Escuadra de Paracaídistas")
        troop = range(11)
        for i in troop:
            a = random.choice(dice)
            if a == 1 or a == 2:
                rep = 4
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            elif a == 3 or a == 4 or a == 5:
                rep = 5
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            else:
                rep = 6
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
    else:
        print("Por favor, selecciona una opción válida")

#Rusos
if ejercito == 4:
    tipo = int(input("Presiona 1 para Infantería, 2 para Infanteria de asalto, 3 para Jinetes de Tanque: "))
    names = ("Vladimir", "Vasili", "Volodia", "Ilich", "Ivan", "Georgy", "Leonid", "Piotr", "Alexei", "Boris",
             "Dimitri", "Anatoly", "Andrey", "Nicolay", "Igor", "Ivan", "Andrei", "Elisei", "Fyodor", "Grigory",
             "Iosif", "Nikita", "Lavrenty", "Leon", "Ivan", "Kliment", "Konstantin", "Leonid", "Misha", "Sasha",
             "Valery", "Yuri", "Yevgeny", "Ivan")
    if tipo == 1:
        print("Escuadra de Infantería")
        troop = range(7) #Sería mejor ponerlos 10, pero este sistema respeta las listas de "NUTS!"
        for i in troop:
            a = random.choice(dice)
            if a == 1:
                rep = 3
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            elif a == 2 or a == 3 or a == 4 or a == 5:
                rep = 4
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            else:
                rep = 5
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
    elif tipo == 2:
        print("Escuadra de Infantería de asalto")
        troop = range(10)
        for i in troop:
            a = random.choice(dice)
            if a == 1 or a == 2 or a == 3:
                rep = 3
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            elif a == 4 or a == 5:
                rep = 4
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            else:
                rep = 5
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
    elif tipo == 3:
        print("Equipo de Jinetes de Tanque")
        troop = range(5)
        for i in troop:
            a = random.choice(dice)
            if a == 1 or a == 2:
                rep = 3
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            elif a == 3 or a == 4:
                rep = 4
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
            else:
                rep = 5
                name = random.choice(names)
                hab = habilidades()
                print(i+1, name, rep, hab)
    else:
        print("Por favor, selecciona una opción válida")