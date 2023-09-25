import pickle
import classes_animals as ca

if __name__ == '__main__':
    tomas = ca.Cat("Thomas 4th", age=10)
    tomas.move()
    larry = ca.DogTerier(name="Lariontiy III")
    larry.move()

    with open('obj_pickled.txt', mode="wb") as fid:
        pickle.dump(tomas, fid)
        pickle.dump(larry, fid)


