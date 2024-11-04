##Jan Poreba
import random
import sys

class RandomNumberGenerator:
    """
    Pseudo random number generator
    Args:
        start: lower bound for random integers
        end: upper bound for random integers
    """

    def __init__(self, start=0, end=100):
        self.start = start
        self.end = end
        ##!TODO wyjatek start >= end


    def get_random(self):
        """
        Method generating random integer from [start, end]
        :return: random integer from [start, end]
        """
        return random.randint(self.start, self.end)



random_number_generator = RandomNumberGenerator(0, 100)
while True:
    command = sys.stdin.readline().strip()
    if command == "Shutdown":
        ##cleaning buffer
        sys.stdout.flush()
        break
    if command == "Hi":
        sys.stdout.write("Hi\n")
        ##cleaning buffer
        sys.stdout.flush()
    if command == "GetRandom":
        r = random_number_generator.get_random()
        sys.stdout.write(f"{r}\n")
        ##cleaning buffer
        sys.stdout.flush()


