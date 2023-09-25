import pickle
import classes_animals as ca

if __name__ == '__main__':
    tomas = ca.Cat("Thomas 4th", age=10)
    tomas.move()
    pickled_string = pickle.dumps(tomas)
    print(pickled_string)
