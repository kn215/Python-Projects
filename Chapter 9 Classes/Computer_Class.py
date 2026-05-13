class Computer:
    def __init__(self, cpu, ram, gpu):

        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
      

    
    def describe_computer(self):
        print(f" The computer has the following specifications:")
        # for computer in self.computer:
        print(f"\n{self.cpu}")

my_computer = Computer('14700k', 32, 4070)

my_computer.describe_computer()