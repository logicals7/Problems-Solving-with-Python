# our class Ship
class Ship:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination

    # the old sail method that you need to rewrite
    def sail(self):
        return "The {} has sailed for {}!".format(self.name, self.destination)

inp_destination = input()
black_pearl = Ship("Black Pearl", inp_destination)
print(black_pearl.sail())