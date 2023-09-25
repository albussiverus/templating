import pickle
"""run this file if obj_pickled.txt created by serialisation.py"""

if __name__ == '__main__':

    """there is no object declaration or description of classes we only
    reading dumped object fro dump file"""
    with open('obj_pickled.txt', 'rb') as fid:
        thomas_cat = pickle.load(fid)
        larry_dog = pickle.load(fid)


    thomas_cat.move()
    larry_dog.say()
