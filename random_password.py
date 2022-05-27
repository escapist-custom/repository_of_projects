import random
class Random_password:
    def __init__(self):
        self.symbols = 'qwertyuiopasdfghjklmnbvcxz1234567890_' # list of available symbols
        self.list1 = [] # list, which will full of passwords
        self.am = input('Enter name of the list of passwords: ') # this command input name of list for next command
        self.nam_of_file = self.am + '.txt'
    def rand(self):
        for i in range(60001):
            list2 = [] # this list for input of passwords in main list (list1)
            for j in range(1, 6):
                list2.append(random.choice(self.symbols))
            list2 = ''.join(list2)
            self.list1.append(list2)
class File(Random_password):
    def writing_in_file(self): # function for inputting in file the passwords
        with open(f'''C:\\Users\\Кирилл\\Saved Games\\PycharmProjects\\pythonProject1\\files_with_.txt\\{self.nam_of_file}''', 'w') as p:
            p.write(str(self.list1))

a = File()
a.rand()
a.writing_in_file()