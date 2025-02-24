class Director:
    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return "<Director {}>".format(self.director_full_name)

    def __eq__(self, other):
        return self.director_full_name == other.director_full_name

    def __lt__(self, other):
        if self.director_full_name < other.director_full_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.director_full_name)