import shelve
import classes_animals as ca

tom = ca.Cat(name="Thomas", age=4)
# tom.move()
jack = ca.Dog(name="Jack", age=12)
# jack.say()
# jack.eat()
larry = ca.DogTerier(name="Lariontiy III")

if __name__ == '__main__':

    dbsh = shelve.open('dbl')
    dbsh["tom"] = tom
    dbsh["larry"] = larry
    dbsh["jack"] = jack
    dbsh.close()
