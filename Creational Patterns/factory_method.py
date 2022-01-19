class IceCreameFactory(object):
    def __init__(self, name):
        self.name=name

    def __str__(self):
        return f"Name of IceCreame is: {self.name}"

    @staticmethod
    def create_waffle_IC(name):
        return IceCreameFactory(name)

    @staticmethod
    def create_stick_IC(name):
        return IceCreameFactory(name)

waffle=IceCreameFactory.create_waffle_IC("Waffle")
stick=IceCreameFactory.create_stick_IC("StickIC")
print(waffle, "\n", stick)
