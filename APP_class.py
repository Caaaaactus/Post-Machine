import customtkinter


from PIL import Image

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Post machine simulator")
        self.geometry("1200x720")
        self.minsize(1200, 720)
        self.maxsize(1200, 720)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        #############################################
        self.frame_menu = customtkinter.CTkFrame(self, width=300, height=720)
        self.frame_menu.grid(column = 0, row = 0, rowspan = 2, padx = (15, 0), pady = 15, sticky = "NSEW")

        self.label_logo = customtkinter.CTkLabel(self.frame_menu, text="_Post \nmachine", font=("Segoe UI", 50), compound="center",anchor="center")
        self.label_logo.grid(column=0, row=0, padx=20, pady=(20, 50), sticky="ew")

        self.btn_information = customtkinter.CTkButton(self.frame_menu,text="СПРАВКА О ПРОЕКТЕ",width=200,height=32,font = ("Segoe UI", 16),fg_color="#353535",text_color="#888888",command=self.btn_information_met)
        self.btn_information.grid(column = 0, row = 2, padx = 20, pady = (20, 10), sticky = "ew")

        self.btn_commands = customtkinter.CTkButton(self.frame_menu,text="ОБУЧЕНИЕ",width=200,height=32,font=("Segoe UI", 16),fg_color="#353535",text_color="#888888",command=self.btn_commands_met)
        self.btn_commands.grid(column=0, row=3, padx=20, pady=(0, 10), sticky="ew")

        self.btn_post_mac = customtkinter.CTkButton(self.frame_menu,text="МАШИНА ПОСТА",width=200,height=32,font=("Segoe UI", 16),fg_color="#353535",text_color="#888888",command=self.btn_post_mac_met)
        self.btn_post_mac.grid(column=0, row=4, padx=20, pady=(0, 10), sticky="ew")
        #############################################



        #############################################
        self.frame_outputConsole = customtkinter.CTkFrame(self, width=870, height=300)
        self.frame_outputConsole.grid(column=1, row=0, padx=15, pady=(15, 0), sticky="NSEW")


        self.headline_tape = customtkinter.CTkTextbox(self.frame_outputConsole, width=50, height=20, font=("Segoe UI", 20), activate_scrollbars=False, fg_color="#2B2B2B")
        self.headline_tape.grid(row=0, column=0,  padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_tape.insert("0.0", "Лента машины")
        self.headline_tape.configure(state="disabled")


        self.output = customtkinter.CTkTextbox(self.frame_outputConsole,height=50, width=800,  font=("Segoe UI", 20), activate_scrollbars=False)
        self.output.grid(row=1, column=0, padx=20, pady=(5,5))

        self.write_head_line = customtkinter.CTkSlider(self.frame_outputConsole, width=800, progress_color="#4A4D50")
        self.write_head_line.grid(row=2, column=0, padx=20, pady=(0, 20))
        self.write_head_line.configure(state="disabled")

        self.step = customtkinter.CTkTextbox(self.frame_outputConsole, width=300, height=40, font=("Segoe UI", 20), activate_scrollbars=False)
        self.step.grid(row=3,padx=20, sticky="w")

        self.fail = customtkinter.CTkTextbox(self.frame_outputConsole, width=300, height=40, font=("Segoe UI", 20), activate_scrollbars=False)
        self.fail.grid(row=4,pady=(10,20))
        #############################################



        #############################################
        self.frame_inputConsole = customtkinter.CTkFrame(self, width=870, height=405)
        self.frame_inputConsole.grid(column=1, row=1, padx=15, pady=15, sticky="NSEW")
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
    def console_output_met(self):
        pass


app = App()
app.mainloop()



