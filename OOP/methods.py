class Coordinate:
    # pair: list = [0, 0]

    def __init__(self, x, y,  *args, **kwargs):
        print("I'm here")
        self.pair = [0, 0]
        self.pair[0] = x
        self.pair[1] = y

    def __str__(self):
        return "this is coordinate"
    def show_x(self):
        print(self.pair[0])

    def show_y(self):
        print(self.pair[1])

    def show(self):
        self.__privat()

    def _protect(self):
        self.show_x()
        self.show_y()

    def __privat(self):
        self.show_x()
        self.show_y()

    def __del__(self):
        print("good bye")


print("*"*5)
coord = Coordinate(0, 2)
print("*"*5)
coord.show_x()
coord.pair[1] = 12
print(coord.pair)

coord.show()

coord_2 = Coordinate(x=120, y=12000)
# coord_2.show()
# print(str(coord_2))
# # del(coord_2)

# coord.__privat()

