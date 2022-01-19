class IceCreame:
    def release(self, taste):
        pass

class Waffle(IceCreame):
    def release(self, taste):
        print(f"Вот вам вафельная мороженка со вкусом {taste}")

class Stick(IceCreame):
    def release(self, taste):
        print(f"Вот вам мороженка на палочке со вкусом {taste}")

class ICFactory:
    def create(self)-> IceCreame:
        pass

class WaffleFactory(ICFactory):
    def create(self):
        return Waffle()

class StickFactory(ICFactory):
    def create(self):
        return Stick()

creator = WaffleFactory()
waffle=creator.create()

creator = StickFactory()
stick=creator.create()

waffle.release("клубничка")
stick.release("шоколад")
# print(waffle, stick, sep="\n")

class SayHelo:
    def sayhi(self):
        print("Hi")

hj=SayHelo()
hj.sayhi()