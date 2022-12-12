import customtkinter
from POST_MACHINE_class import post_machine
from PIL import Image

class App(customtkinter.CTk, post_machine):
    def __init__(self):
        super().__init__()

        self.title("Post machine simulator")
        self.geometry("1200x720")
        self.minsize(1200, 900)
        self.maxsize(1200, 900)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        #############################################
        self.frame_menu = customtkinter.CTkFrame(self)
        self.frame_menu.grid(column = 0, row = 0, rowspan = 4, padx = (15, 0), pady = 15, sticky = "NSEW")

        self.label_logo = customtkinter.CTkLabel(self.frame_menu, text="_Post \nmachine", font=("Segoe UI", 50), compound="center",anchor="center")
        self.label_logo.grid(column=0, row=0, padx=20, pady=(20, 50), sticky="ew")

        self.btn_information = customtkinter.CTkButton(self.frame_menu,text="СПРАВКА О ПРОЕКТЕ",width=200,height=32,font = ("Segoe UI", 16),fg_color="#353535",text_color="#888888",command=self.btn_information_met)
        self.btn_information.grid(column = 0, row = 2, padx = 20, pady = (20, 10), sticky = "ew")

        self.btn_commands = customtkinter.CTkButton(self.frame_menu,text="ОБУЧЕНИЕ",width=200,height=32,font=("Segoe UI", 16),fg_color="#353535",text_color="#888888",command=self.btn_commands_met)
        self.btn_commands.grid(column=0, row=3, padx=20, pady=(0, 10), sticky="ew")

        self.btn_post_mac = customtkinter.CTkButton(self.frame_menu,text="МАШИНА ПОСТА",width=200,height=32,font=("Segoe UI", 16),fg_color="#353535",text_color="#888888",command=self.btn_post_mac_met)
        self.btn_post_mac.grid(column=0, row=4, padx=20, pady=(0, 10), sticky="ew")

        self.btn_ready_command = customtkinter.CTkButton(self.frame_menu, text="ГОТОВЫЕ КОМАНДЫ", width=200, height=32,font=("Segoe UI", 16), fg_color="#353535", text_color="#888888",command=self.btn_post_mac_met)
        self.btn_ready_command.grid(column=0, row=5, padx=20, pady=(0, 10), sticky="s")
        #############################################



        #############################################
        self.frame_inputConsole = customtkinter.CTkFrame(self, height=350)
        self.frame_inputConsole.grid(column=1, row=0, rowspan=1, padx=15, pady=(15, 0), sticky="NSEW")

        self.headline_command_input_field = customtkinter.CTkTextbox(self.frame_inputConsole, width=50, height=20,font=("Segoe UI", 20), activate_scrollbars=False,fg_color="#2B2B2B")
        self.headline_command_input_field.grid(row=0, column=0, padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_command_input_field.insert("0.0", "Ввод программы")
        self.headline_command_input_field.configure(state="disabled")

        self.command_input_field = customtkinter.CTkTextbox(self.frame_inputConsole, width=300, height=305,font=("Segoe UI", 20), activate_scrollbars=True,fg_color="#2f2f2f")
        self.command_input_field.grid(row=1, rowspan=3, column=0, padx=15, pady=(0, 20), sticky="NSEW")
        self.command_input_field.configure(state="disabled")

        self.headline_first_tape_input_field = customtkinter.CTkTextbox(self.frame_inputConsole, width=50, height=20,font=("Segoe UI", 20), activate_scrollbars=False,fg_color="#2B2B2B")
        self.headline_first_tape_input_field .grid(row=0, column=1, padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_first_tape_input_field.insert("0.0", "Ввод начального состояния ленты")
        self.headline_first_tape_input_field.configure(state="disabled")
        self.first_tape_input_field = customtkinter.CTkTextbox(self.frame_inputConsole, width=400, height=100,font=("Segoe UI", 20), activate_scrollbars=True,fg_color="#2f2f2f")
        self.first_tape_input_field.grid(row=1, rowspan=2, column=1, padx=15, sticky="n")



        self.check_first_tape_input_field = customtkinter.CTkCheckBox(master=self.frame_inputConsole, text="Зафиксировать начальное состояние ленты",onvalue=1, offvalue=0, command=self._fix1)
        self.check_first_tape_input_field.grid(row=2, column=1, padx=15, pady=55, sticky="nw")


        self.check_command_input_field = customtkinter.CTkCheckBox(master=self.frame_inputConsole,text="Зафиксировать программу",onvalue=1, offvalue=0, command=self._fix2)
        self.check_command_input_field.grid(row=4, column=0, padx=15, pady=(0,20), sticky="nw")
        self.check_command_input_field.configure(state='disabled')

        self.btn_start = customtkinter.CTkButton(self.frame_inputConsole, text="Начать выполнение", width=300, height=32,font=("Segoe UI", 16), fg_color="#2FA572", text_color="#2B2B2B",command=self._start)
        self.btn_start.grid(column=0, row=5, padx=15, pady=(0, 20), sticky="nw")
        self.btn_start.configure(state="disabled")
        #############################################



        #############################################
        self.frame_outputConsole = customtkinter.CTkFrame(self)
        self.frame_outputConsole.grid(column=1, row=1, rowspan=2, padx=15, pady=15, sticky="NSEW")

        self.headline_tape = customtkinter.CTkTextbox(self.frame_outputConsole, width=50, height=20,
                                                      font=("Segoe UI", 20), activate_scrollbars=False,
                                                      fg_color="#2B2B2B")
        self.headline_tape.grid(row=0, column=0, padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_tape.insert("0.0", "Лента машины")
        self.headline_tape.configure(state="disabled")


        self.output = customtkinter.CTkTextbox(self.frame_outputConsole, height=50, width=800, font=("Segoe UI", 20), activate_scrollbars=False)
        self.output.grid(row=1, column=0, padx=20, pady=(5, 5))
        self.output.configure(state="normal")
        self.output.insert("0.0", '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        self.output.configure(state="disabled")

        self.write_head_line = customtkinter.CTkSlider(self.frame_outputConsole, width=800, progress_color="#4A4D50")
        self.write_head_line.grid(row=2, column=0, padx=20)
        self.write_head_line.configure(state="disabled")

        self.headline_step = customtkinter.CTkTextbox(self.frame_outputConsole, width=50, height=20,font=("Segoe UI", 20), activate_scrollbars=False, fg_color="#2B2B2B")
        self.headline_step.grid(row=3, column=0, padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_step.insert("0.0", "Команда")
        self.headline_step.configure(state="disabled")

        self.step = customtkinter.CTkTextbox(self.frame_outputConsole, width=300, height=40, font=("Segoe UI", 20),activate_scrollbars=False)
        self.step.grid(row=4, padx=20, sticky="w")
        self.step.configure(state="disabled")

        self.headline_comp = customtkinter.CTkTextbox(self.frame_outputConsole, width=50, height=20,font=("Segoe UI", 20), activate_scrollbars=False, fg_color="#2B2B2B")
        self.headline_comp.grid(row=5, column=0, padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_comp.insert("0.0", "Результат выполнения")
        self.headline_comp.configure(state="disabled")
        self.rezult = customtkinter.CTkTextbox(self.frame_outputConsole, width=300, height=40, font=("Segoe UI", 20),  activate_scrollbars=False)
        self.rezult.grid(row=6, column=0, pady=(0, 20), padx=20, sticky="NSEW")
        self.rezult.configure(state="disabled")
        #############################################



    def btn_information_met(self):
        window_information = customtkinter.CTkToplevel(self)
        window_information.geometry("400x200")

        label = customtkinter.CTkLabel(window_information, text="Данный проект был сделан")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)
    def btn_commands_met(self):
        window_commands = customtkinter.CTkToplevel(self)
        window_commands.geometry("610x1100")

        img_tape = customtkinter.CTkImage(light_image=Image.open("img/edu.png"),
                                          dark_image=Image.open("img/edu.png"),
                                          size=(610, 1000))

        label_img = customtkinter.CTkLabel(window_commands, image=img_tape, text="")
        label_img.pack(side="bottom", fill="both", expand=True)
    def btn_post_mac_met(self):
        window_post_mac = customtkinter.CTkToplevel(self)
        window_post_mac.geometry("900x500")
        window_post_mac.title("Information about Post Machine")
        label_text = customtkinter.CTkLabel(window_post_mac,
                                       text="Маши́на По́ста — абстрактная вычислительная машина, \n"
                                             "предложенная Эмилем Постом в 1936 году, создана независимо от машины \n"
                                             "Тьюринга, но сообщение о машине Поста опубликовано на несколько месяцев \n"
                                             "позднее. Отличается от машины Тьюринга большей простотой, притом обе \n"
                                             "машины алгоритмически «эквивалентны» и обе разработаны для формализации \n"
                                             "понятия алгоритма и решения задач об алгоритмической разрешимости, то есть, \n"
                                             "демонстрации алгоритмического решения задач в форме последовательности команд \n"
                                             "для машины Поста.",
                                       font=("Segoe UI", 20),
                                       compound="center",
                                       anchor="center"
                                       )
        label_text.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        img_tape = customtkinter.CTkImage(light_image=Image.open("img/tape.png"),
                                          dark_image=Image.open("img/tape.png"),
                                          size=(850, 150))

        label_img= customtkinter.CTkLabel(window_post_mac,image = img_tape, text="")
        label_img.pack(side="bottom", fill="both", expand=True, padx=20, pady=20)
    def _fix1(self):
        if self.check_first_tape_input_field.get():
            self.first_tape_input_field.configure(state="disabled")
            self.command_input_field.configure(state="normal")
            self.check_command_input_field.configure(state='normal')
        else:
            self.first_tape_input_field.configure(state="normal")
            self.command_input_field.configure(state="disabled")
            self.check_command_input_field.configure(state='disabled')
    def _fix2(self):
        if self.check_command_input_field.get():
            self.command_input_field.configure(state="disabled")
            self.btn_start.configure(state="normal")
        else:
            self.command_input_field.configure(state="normal")
            self.btn_start.configure(state="disabled")
    def _start(self):

        #считываем список команд
        self.command_list = []

        line_commands_str = self.command_input_field.get('0.0', 'end').split('\n')

        self.command_list+=line_commands_str

        for i in range(len(self.command_list)):
            self.command_list[i] = self.command_list[i].replace(' ', '')
        self.command_list = self.command_list[:-1]

        #считываем изначаольное состояние ленты
        self.first_tape_list = []

        line_first_tape_str = self.first_tape_input_field.get('0.0', 'end').split('\n')
        line_first_tape_str = line_first_tape_str[:-1]
        for i in line_first_tape_str[0]:
            self.first_tape_list.append(int(i))
        self.first_tape_list += [0]*100
        self.first_tape_list[:0] = [0]*100
        #присваиваем индекс пищущей коретке
        self.wr_head = len(self.first_tape_list)//2

        #инициализируем машину
        p_m = post_machine(True, self.first_tape_list, self.wr_head)

        #делаем запуск
        work=True
        step = 1
        while work:
            current_command = self.command_list[step-1][1]
            self.step.configure(state="normal")
            self.step.delete("0.0", "end")
            self.step.insert("0.0", self.command_list[step - 1])
            self.step.insert("0.1", ': ')
            self.step.insert("0.2", step)
            self.step.configure(state="disabled")

            #next_command = self.command_list[next_command-1][2]

            ex=[]
            ex = p_m.command_method(current_command)
            print(ex)
            if ex !="Программа не может окончить свое выполнение в связи с ошибкой":
                current_tape, self.wr_head = ex[0], ex[1]
                self.output.configure(state="normal")
                self.output.insert("0.0", current_tape[self.wr_head - 24:self.wr_head + 25])
                self.output.configure(state="disabled")

            elif ex=="Программа не может окончить свое выполнение в связи с ошибкой":
                self.rezult.configure(state="normal")
                self.rezult.insert("0.0", ex)
                self.rezult.configure(state="disabled")
                work = False
                return None
            step = self.command_list[step - 1][2]

app = App()
app.mainloop()



