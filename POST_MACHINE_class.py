class post_machine():
    """
    class post_machine()
    Назначение класса - моделирование работы машины
    посредством обработки текущей команды, возврат обновленной ленты
    и ошибки в случае невозможности выполнения программы

    ----------
    Methods

    __init__(self, state, tape_list, write_head)
    Выполняется всякий раз, когда из класса создаётся объект.
    Используется для инициализации переменных класса.
    state - состояние машины (True - работает. False - не работает)
    tape_list - лента машины
    write_head - индекс пищущей головки на ленте

    get_state(self)
    Возвращает состояние машины (True - работает. False - не работает)

    get_tape_list(self)
    Возвращает ленту машины

    get_write_head(self)
    Возвращает индекс пищущей головки машины

    _can_do_command(self, current_command)
    Метод определяющий возможность выполнения той или иной команды поступившей машине
    current_command - текущая команда

    tape_extension(self)
    Метод удлиняющий ленту в случае необходимости (головка машины дошла до одного из краев)

    command_method(self, current_command)
    Основной метод класса, моделирующий выполнение команд
    current_command - текущая команда
    """

    def __init__(self, state, tape_list, write_head):
        """
        __init__(self, state, tape_list, write_head)
        Выполняется всякий раз, когда из класса создаётся объект.
        Используется для инициализации переменных класса.
        state - состояние машины (True - работает. False - не работает)
        tape_list - лента машины
        write_head - индекс пищущей головки на ленте
        """

        self.state = state
        self.tape_list = tape_list
        self.write_head = write_head

    def get_state(self):
        """
        get_state(self)
        Возвращает состояние машины (True - работает. False - не работает)
        """

        return self.state

    def get_tape_list(self):
        """
        get_tape_list(self)
        Возвращает ленту машины
        """

        return self.tape_list

    def get_write_head(self):
        """
        get_write_head(self)
        Возвращает индекс пищущей головки машины
        """

        return self.write_head

    def _can_do_command(self, current_command):
        """
        _can_do_command(self, current_command)
        Метод определяющий возможность выполнения той или иной команды поступившей машине
        current_command - текущая команда
        """

        #проверяем возможность выполнения команды согласно правилам работы машины
        #(невозможно поставить метку в непустое поле, как и убрать метку из пустого)
        if self.tape_list[self.write_head] == '1' and current_command == 'v':
            return False
        elif self.tape_list[self.write_head] == '0' and current_command == '-':
            return False
        else:
            return True

    def tape_extension(self):
        """
        tape_extension(self)
        Метод удлиняющий ленту в случае необходимости (головка машины дошла до одного из краев)
        """

        #расширяем ленту, если доходим до одного из ее концов
        if self.write_head == len(self.tape_list)-1:
            self.tape_list += ['0']*33
        elif self.write_head == 0:
            self.tape_list[:0] = ['0'] * 33

        return self.tape_list

    def command_method(self, current_command):
        """
        command_method(self, current_command)
        Основной метод класса, моделирующий выполнение команд
        current_command - текущая команда
        """

        #инициализируем поступившую программу и возможность ее выполнения,
        #после чего приступаем к ее реализации
        if current_command == 'v' and self._can_do_command(current_command):
            self.tape_list[self.write_head] = '1'

            return self.tape_list, self.write_head

        elif current_command == '-' and self._can_do_command(current_command):
            self.tape_list[self.write_head] = '0'

            return self.tape_list, self.write_head

        elif current_command == '>':
            if self.write_head==len(self.tape_list)-1:
                self.tape_list = self.tape_extension()
            self.write_head+=1

            return self.tape_list, self.write_head

        elif current_command == '<':
            if self.write_head == 0:
                self.tape_list = self.tape_extension()
            self.write_head-=1

            return self.tape_list, self.write_head

        elif current_command == 's':

            return "Программа окончила свое выполнение без ошибок"

        elif current_command == '?':
            if self.tape_list[self.write_head] == '1':
                return 22
            if self.tape_list[self.write_head] == '0':
                return 11
        #в случае ошибки, возвращаем не новую ленту и индекс головки, а ошибку
        elif not self._can_do_command(current_command):

            return "Программа не может окончить свое выполнение в связи с ошибкой"

        """else:
            self.tape_list = ['!']*len(self.tape_list)
            return [' &']*len(self.tape_list)"""
