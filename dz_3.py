class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        add = self.cpu + self.memory
        return f'addition mit cpu and memory: {self.cpu} + {self.memory} = {add}'

    def __str__(self):
        return f'Cpu: {self.cpu}, Memory: {self.memory}'

    def __eq__(self, other):
        return self.memory == other

    def __ne__(self, other):
        return self.memory != other

    def __lt__(self, other):
        return self.memory < other

    def __gt__(self, other):
        return self.memory > other

    def __le__(self, other):
        return self.memory <= other

    def __ge__(self, other):
        return self.memory >= other


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = list(sim_cards_list)

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if sim_card_number == 1 and type(call_to_number) == int:
            return (f'Идет звонок на номер +{call_to_number} с симкарты'
                    f'-{sim_card_number}-{self.sim_cards_list[0]}')
        elif sim_card_number == 2 and type(call_to_number) == int:
            return (f'Идет звонок на номер +{call_to_number} с симкарты'
                    f'-{sim_card_number}-{self.sim_cards_list[1]}')
        else:
            return f'вы неправильно ввели номер или сим'

    def __str__(self):
        return f'Sim_cards_list: {self.sim_cards_list}'

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        return f'Маршрут построен на {location}'

    def __str__(self):
        return super().__str__()

pc = Computer(32, 1024)
xio_mi = Phone(['Beeline', 'Mega'])
smart_phone_1 = SmartPhone(8,64, ['Mega', 'O'])
smart_phone_2 = SmartPhone(16,128, ['Mega', 'Beeline'])
print(pc)
print(xio_mi)
print(smart_phone_1)
print(smart_phone_2)

print(pc.make_computations())
print(xio_mi.call(1, 996550525131))
print(pc.__eq__(smart_phone_1))
print(pc.__ne__(smart_phone_2))
print(pc.__ge__(pc))
print(smart_phone_1.__le__(pc))
print(smart_phone_2.__gt__(smart_phone_1))
print(smart_phone_2.__lt__(pc))
print(smart_phone_1.call(2, 996222938968))
print(smart_phone_2.call(1, 996772351563))
print(smart_phone_1.make_computations())
print(smart_phone_2.use_gps('Berlin'))





