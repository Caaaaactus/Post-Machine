class post_machine:
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
    def __init__ (self, state, write_head, tape_list):
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

        Назначение - автоматически вызываемый при создании каждого экземпляра метод
        '''
        self.state = state
        self.write_head = write_head
        self.tape_list = tape_list

    def get_state(self):
        '''
        get_state(self)

        Назначение - метод возврата состояния
        '''
        return self.state

    def get_write_head(self):
        '''
        get_write_head(self)

        Назначение - метод возврата положения пишущей головки
        '''
        return self.write_head

    def get_tape_list(self):
        '''
        get_tape_list(self)

        Назначение - метод возврата ленты
        '''
        return self.tape_list

    def update_state(self, current_command, state, write_head, tape_list):
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
        1)  при постановке метки, т.к. в используемой ячейке УЖЕ содержится метка
        2) при стирании метки, т.к. в используемой ячейке НЕ содержится метка
        '''
        if tape_list[write_head] == 1 and current_command[1] == 'v':

            print(f"Команда {current_command[0]} не может быть выполнена, т.к. в используемой ячейке УЖЕ содержится метка")
            return not state

        elif tape_list[write_head] == 0 and current_command[1] == '-':

            print(f"Команда {current_command[0]} не может быть выполнена, т.к. в используемой ячейке НЕ содержится метка")
            return not state

        else:

            return state



if __name__ == "__main__":
    t_l = [0]*32
    s = True
    w_h = 5

    p_m = post_machine(s, w_h, t_l)

    print(p_m.__doc__)








