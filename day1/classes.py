class Room:
    # here length and breadth are the argument of thr classes

    # constructor

    def __init__(self, length=0, breadth=0):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def peremeter(self):
        return 2*(self.length + self.breadth)

    def print_details(self):
        print(f"Room dimension :{self.length} x {self.breadth}")
        print(f"Area:{self.area()} square meters")
        print(f"peremeter :{self.peremeter()} meters")


room1 = Room(2, 5)
room1.print_details()
