def show_persons(title, person, blank=True):
    print('-'*20)
    print(title)
    print('-'*20)

    if (person):
        persons = list(person)
        persons.sort()
        for p in persons:
            print(p)
    if (blank):
        print()


noivo = set()
noiva = set()

while True:
    askPerson = input()
    if (askPerson == 'ACABOU'):
        break
    convidado, convidante = askPerson.split(';')
    if (convidante == 'noivo'):
        noivo.add(convidado)
    else:
        noiva.add(convidado)
        
show_persons('LISTA FINAL', noivo | noiva)
show_persons('APENAS NOIVA', noiva-noivo)
show_persons('APENAS NOIVO', noivo-noiva)
show_persons('POR AMBOS', noivo & noiva)
show_persons('POR APENAS UM DELES', noivo ^ noiva, blank=False)
