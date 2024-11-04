##Jan Poreba
import random
import sys

class RandomNumberGenerator:

    def __init__(self, start=0, end=100):
        self.start = start
        self.end = end
        ##TODO wyjatek start >= end

    def get_random(self):
        return random.randint(self.start, self.end)



random_number_generator = RandomNumberGenerator(-1000, 1000)
while True:
    command = sys.stdin.readline().strip()
    if command == "Shutdown":
        sys.stdout.flush()
        break
    if command == "Hi":
        sys.stdout.write("Hi\n")
        sys.stdout.flush()
    if command == "GetRandom":
        r = random_number_generator.get_random()
        sys.stdout.write(f"{r}\n")
        sys.stdout.flush()
    #TODO: obsluga braku komendy?



