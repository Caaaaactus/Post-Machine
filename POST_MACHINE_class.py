"""class post_machine:
    '''
    Класс машина Поста post_machine

    Методы:
        ----------------------------------------------------------------------
        __init__(self, state, write_head, tape_list)
            state:
                type bool
                Переменная показывающая способность или неспособность продолжить работу программы
            write_head
                type int
                Переменная хранящая индекс пишущей головки
            tape_list
                type list
                Список - имитация ленты

        Назначение - автоматически вызываемый при создании каждого экземпляра метод
        ----------------------------------------------------------------------
        get_state(self)

        Назначение - метод возврата состояния
        ----------------------------------------------------------------------
        get_write_head(self)

        Назначение - метод возврата положения пишущей головки
        ----------------------------------------------------------------------
        get_tape_list(self)

        Назначение - метод возврата ленты
        ----------------------------------------------------------------------
        get_command_list(self)

        Назначение - метод возврата списка комманд
        ----------------------------------------------------------------------
        update_state(self, current_command, state, write_head, tape_list)
            current_command:
                type list
                Список - текущая команда
            state:
                type bool
                Переменная показывающая способность или неспособность продолжить работу программы
            write_head
                type int
                Переменная хранящая индекс пишущей головки
            tape_list
                type list
                Список - эмитация ленты

        Назначение - проверка возможности выполнения команды
        ----------------------------------------------------------------------
    '''

    ##################################################################################################
    def __init__(self, state, write_head, tape_list, command_list):
        '''
        __init__(self, state, write_head, tape_list)
            state:
                type bool
                Переменная показывающая способность или неспособность продолжить работу программы
            write_head
                type int
                Переменная хранящая индекс пишущей головки
            tape_list
                type list
                Список - имитация ленты
            command_list
                type list
                Список - список команд

        Назначение - автоматически вызываемый при создании каждого экземпляра метод
        '''
        self.state = state
        self.write_head = write_head
        self.tape_list = tape_list
        self.command_list = command_list
        self.first = True

    def _get_state(self):
        '''
        get_state(self)

        Назначение - метод возврата состояния
        '''
        return self.state

    def _get_write_head(self):
        '''
        get_write_head(self)

        Назначение - метод возврата положения пишущей головки
        '''
        return self.write_head

    def _get_tape_list(self):
        '''
        get_tape_list(self)

        Назначение - метод возврата ленты
        '''
        return self.tape_list

    def _get_command_list(self):
        '''
        get_command_list(self)

        Назначение - метод возврата списка комманд
        '''
        return self.command_list

    def _update_state(self, current_command):
        '''
        update_state(self, current_command, state, write_head, tape_list)
            current_command:
                type list
                Список - текущая команда
            state:
                type bool
                Переменная показывающая способность или неспособность продолжить работу программы
            write_head
                type int
                Переменная хранящая индекс пишущей головки
            tape_list
                type list
                Список - имитация ленты

        Назначение - проверка возможности выполнения команды

        Логика работы:
        Анализируем возможность выполнить команду пользователя, проверяя ее на возможные ошибки
        Невозможно выполнить команду если она удовлетворяет следующим критериям
        1) при постановке метки, т.к. в используемой ячейке УЖЕ содержится метка
        2) при стирании метки, т.к. в используемой ячейке НЕ содержится метка
        '''
        if self.tape_list[self.write_head] == 1 and current_command[1] == 'v':
            print(f"Команда {current_command[0]} не может быть выполнена, т.к. в используемой ячейке УЖЕ содержится метка")
            return not self.state
        elif self.tape_list[self.write_head] == 0 and current_command[1] == '-':
            print(f"Команда {current_command[0]} не может быть выполнена, т.к. в используемой ячейке НЕ содержится метка")
            return not self.state
        else:
            return self.state

    ##################################################################################################

    def post_machine_working(self, i=0):

        if self.first:
            #print('----------------------')
            #print("Начальное состояние ленты")
            self._get_tape_list()
            #print('----------------------')
            self.first = False
        else:
            #print('----------------------')
            #print(self.tape_list)
            self._get_tape_list()
            #print('----------------------')

        current_command = self.command_list[i]
        can_work = self._update_state(current_command)

        task = current_command[1]

        if can_work:
            if task == 'stop':
                #print("Программа окончила свое выполнение")
                return None
            elif task == 'v':
                self.tape_list[self.write_head] = 1
                i = current_command[2] - 1
            elif task == '-':
                self.tape_list[self.write_head] = 0
                i = current_command[2] - 1
            elif task == '>':
                if self.write_head == len(self.tape_list) - 1:
                    self.tape_list += [0] * 32
                self.write_head += 1
                i = current_command[2] - 1
            elif task == '<':
                if self.write_head == 0:
                    self.tape_list[:0] = [0] * 32
                    self.write_head += 32
                self.write_head -= 1
                i = current_command[2] - 1
            elif task == '?':
                if self.tape_list[self.write_head] == 1:
                    i = current_command[2][0] - 1
                else:
                    i = current_command[2][1] - 1
            return self.tape_list, self.post_machine_working(i)
        else:
            #print("Программа окончила свое выполнение в связи с некоректной командой")
            return "Программа окончила свое выполнение в связи с некоректной командой", None"""


class post_machine():

    def __init__(self, state, tape_list, write_head):
        self.state = state
        self.tape_list = tape_list
        self.write_head = write_head

    def _can_do_command(self, current_command):
        if self.tape_list[self.write_head] == 1 and current_command == 'v':
            return False
        elif self.tape_list[self.write_head] == 0 and current_command == '-':
            return False
        else:
            return True

    def tape_extension(self):
        if self.write_head == len(self.tape_list):
            self.tape_list += [0]*33
        elif self.write_head == 0:
            self.tape_list[:0] = [0] * 33

        return self.tape_list
    def command_method(self, current_command):
        if current_command == 'v' and self._can_do_command(current_command):
            self.tape_list[self.write_head] = 1

            return self.tape_list, self.write_head

        elif current_command == '-' and self._can_do_command(current_command):
            self.tape_list[self.write_head] = 0

            return self.tape_list, self.write_head

        elif current_command == '>':
            if self.write_head == 0 or self.write_head==len(self.tape_list):
                self.tape_list = self.tape_extension()
            self.write_head+=1

            return self.tape_list, self.write_head

        elif current_command == '<':
            if self.write_head == 0 or self.write_head==len(self.tape_list):
                self.tape_list = self.tape_extension()
            self.write_head-=1

            return self.tape_list, self.write_head

        elif current_command == 's':

            return "Программа окончила свое выполнение"

        elif not self._can_do_command(current_command):

            return "Программа не может окончить свое выполнение в связи с ошибкой"

        else:
            self.tape_list = ['!']*len(self.tape_list)
            return [' &']*len(self.tape_list)



fstate = True
tape = [0]*32
wr = 14
commandlist = [
    [1, 'v', 2],
    [2, 'v', 3],
    [3, 'stop', 3]
]

