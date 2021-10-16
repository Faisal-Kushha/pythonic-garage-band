class Musician:
    """
    A musician which represent the base class and handle common functionality
    """
    members = []

    def __init__(self, name):
        self.name = name
        Musician.members.append(self.name)

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def get_instrument(self):
        pass

    def play_solo(self):
        pass


class Band(Musician):
    """
    A Band class which have name attribute (string) and members attribute which is a list of instances that inherit from base class. it has four methods: play_solos, __str__ , __repr__, to_list.
    """
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solos_list = []
        solos_list.append(Guitarist.play_solo(self))
        solos_list.append(Bassist.play_solo(self))
        solos_list.append(Drummer.play_solo(self))
        return solos_list

    def __str__(self):
        return f'We are {self.name} and we are music band'

    def __repr__(self):
        return f'Band inctance. Name = {self.name}'

    @classmethod
    def to_list(cls):
        print(cls.instances)
        return cls.instances


class Guitarist(Musician):
    """
    A sub class which has four methods: play_solo, __str__ , __repr__, get_instrument .
    """

    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return 'face melting guitar solo'


class Bassist(Musician):
    """
    A sub class which has four methods: play_solo, __str__ , __repr__, get_instrument .
    """

    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return 'bom bom buh bom'


class Drummer(Musician):
    """
    A sub class which has four methods: play_solo, __str__ , __repr__, get_instrument .
    """

    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return 'rattle boom crash'


def x():
    a = Band('ahmad')
    d = a.to_list()
    return d


if __name__ == "__main__":
    print(x())
