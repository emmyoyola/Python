### Clases ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self) -> None:
        pass


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname =surname

my_person = Person("Emmy", "Oyola")
print(my_person.name)
print(f"{my_person.name} {my_person.surname}")


class Person:
    def __init__(self):
        self.name = "Emmy"
        self.surname = "Oyola"

my_person = Person()
print(f"{my_person.name} {my_person.surname}")


class Person:
    def __init__(self, name, surname, alias = "Sin Alias"):
        self.full_name = f"{name} {surname} ({alias})"
    
    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Emmy", "Oyola")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Emmy", "Oyola", "Lulu")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Héctor de león (El loco de los perros)"
print(my_other_person.full_name)
