##Jan Poreba
import subprocess
import statistics
import sys
import json


class ProcessError(Exception):
    """
    Exception raised for error with process
    Args:
        message: explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectResponseError(Exception):
    """
    Exception raised for error with incorrect response
     Args:
        message: explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)




class Controller:
    """
    It defines and control set of actions
    Args:
        program: path to launching program
    """
    def __init__(self, program="pseudo_random_number_generator.py"):
        self.program = program
        self.size = 100
        self.average = -1
        self.median = -1
        f = open("runners.json", "r")
        runners = json.load(f)
        f.close()
        python_command = runners["python"]
        try:
            self.process = subprocess.Popen(
                [python_command, self.program],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            self.random_nums = []
        except FileNotFoundError:
            raise FileNotFoundError(f"Program {program} hasn't been launched\nCheck filename of program A or set python running commend according to your python environment")


    def send_command(self, command):
        """
        Method responsible for sending commands to program A
        :param command: send command
        """
        try:
            self.process.stdin.write(command + '\n')
            #cleaning buffer
            self.process.stdin.flush()
        except (AttributeError, BrokenPipeError, TypeError) as e:
            raise ProcessError("Subprocess may be finished or have not been launched")

    def receive_response(self):
        """
        Method responsible for receiving response from program A
        """
        try:
            response = self.process.stdout.readline().strip()
            return response
        except (AttributeError, OSError, ValueError) as e:
            raise ProcessError("Subprocess may be finished or have not been launched")


    def verify(self, expected):
        """
        Method responsible for verifying command
        :param expected: expected command
        :return: if correct response True else False
        """
        res = self.receive_response()
        if res != expected:
            raise IncorrectResponseError("Incorrect response message\nCheck filename of launching program.")


    def get_random(self):
        """
        Method responsible for retrieving random number
        :return: received random integer
        """
        self.send_command("GetRandom")
        comm = self.receive_response()
        r = int(comm)
        return r

    def retrieve_random_nums(self):
        """
        Method responsible for retrieving #size random numbers
        """
        for _ in range(self.size):
            r = self.get_random()
            self.random_nums.append(r)

    def sort_list(self):
        """
        Method sorting list of random integers
        """
        self.random_nums.sort()

    def print_list(self):
        """
        Method printing sorted list of random numbers
        :return:
        """
        print(f"Sorted list of random numbers {self.random_nums}")

    def get_average(self):
        """
        Method counting of retrieved random numbers
        """
        self.average = statistics.mean(self.random_nums)

    def get_median(self):
        """
        Method counting the median of retrieved random numbers
        """
        self.median = statistics.median(self.random_nums)

    def print_average(self):
        """
        Method printing the average of retrieved random numbers
        """
        print(f"Average {self.average}")

    def print_median(self):
        """
        Method printing the median of retrieved random numbers
        """
        print(f"Median {self.median}")


"""
main function of program executing sequence of actions according to the instruction of the task
"""
def main():
    try:
        if len(sys.argv) > 1:
            controller = Controller(sys.argv[1])
        else:
            controller = Controller()
        controller.send_command("Hi")
        controller.verify("Hi")
        controller.retrieve_random_nums()
        controller.send_command("Shutdown")
        controller.sort_list()
        controller.print_list()
        controller.get_median()
        controller.print_median()
        controller.get_average()
        controller.print_average()
    except FileNotFoundError as e:
        print(str(e))
    except (ValueError, TypeError):
        print("Got incorrect data")
    except (ProcessError, IncorrectResponseError) as e:
        print(e.message)




if __name__ == "__main__":
    main()

