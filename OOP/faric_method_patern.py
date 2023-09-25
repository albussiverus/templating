import classes_animals as ca


class CatMaineCoon(ca.Cat):
    def __init__(
            self,
            name="MC name",
            age=2,
            colour: str = "white"
    ):
        super().__init__(name, age)
        if colour in {"blue", "yellow", "grey"}:
            self.colour = colour
            self.behaviour = "lasy at all"
        else:
            self.colour = 'white'
            self.behaviour = "playing arround with sun light"

    @staticmethod
    def fmaine_coon(active=True) -> ca.Cat:
        """fabric method allows to create objects using its parameters"""
        if active:
            cat = CatMaineCoon(name="ActiveSupperCatsilla", colour='white')
        else:
            cat = CatMaineCoon(name="Lasy old cat", colour='grey')

        return cat


if __name__ == "__main__":
    sherhan = CatMaineCoon.fmaine_coon()
    print(sherhan)
    ron = CatMaineCoon.fmaine_coon(False)
    print(ron)

