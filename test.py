print("Welcome")
s1=125
seconds_in_a_day=20
seconds_in_a_week = 7 * seconds_in_a_day
print(seconds_in_a_week)

# parent class
class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):
    def __init__(self):
        # call super() function
        # super(self).__init__()
        print("Penguin is ready")
    def whoisThis(self):				#Function Overriding
        print("Penguin")
    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()