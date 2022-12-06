import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Post machine simulator")
        self.geometry("1200x720")
        self.minsize(1200, 720)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")



        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)



        self.frame_menu = customtkinter.CTkFrame(self, width=300, height=720)
        self.frame_menu.grid(column = 0, row = 0, rowspan = 2, padx = (15, 0), pady = 15, sticky = "NSEW")

        self.btn_information = customtkinter.CTkButton(self.frame_menu,
                                                       text="СПРАВКА О ПРОЕКТЕ",
                                                       width=200,
                                                       height=32,
                                                       font = ("Segoe UI", 16),
                                                       fg_color="#353535",
                                                       text_color="#888888",
                                                       command=self.btn_information_met())
        self.btn_information.grid(column = 0, row = 0, padx = 20, pady = (20, 10), sticky = "ew")
        self.btn_commands = customtkinter.CTkButton(self.frame_menu,
                                                       text="ОБУЧЕНИЕ",
                                                       width=200,
                                                       height=32,
                                                       font=("Segoe UI", 16),
                                                       fg_color="#353535",
                                                       text_color="#888888",
                                                       command=self.btn_information_met())
        self.btn_commands.grid(column=0, row=1, padx=20, pady=(0, 10), sticky="ew")
        self.btn_post_mac = customtkinter.CTkButton(self.frame_menu,
                                                    text="МАШИНА ПОСТА",
                                                    width=200,
                                                    height=32,
                                                    font=("Segoe UI", 16),
                                                    fg_color="#353535",
                                                    text_color="#888888",
                                                    command=self.btn_information_met())
        self.btn_post_mac.grid(column=0, row=2, padx=20, pady=(0, 10), sticky="ew")

        self.frame_outputConsole = customtkinter.CTkFrame(self, width=870, height=200)
        self.frame_outputConsole.grid(column=1, row=0, padx=15, pady=(15, 0), sticky="NSEW")

        self.frame_inputConsole = customtkinter.CTkFrame(self, width=870, height=505)
        self.frame_inputConsole.grid(column=1, row=1, padx=15, pady=15, sticky="NSEW")

    def btn_information_met(self):
        pass
    def btn_commands_met(self):
        pass
    def btn_post_mac_met(self):
        pass

app = App()
app.mainloop()


