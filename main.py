import tkinter as tk 

import util

class App:
  def __init__(self):
    self.main_window = tk.Tk()
    self.main_window.geometry("1200x520+350+100")

    self.login_button_main_window = util.get_button(self.main_window, 'login', 'green', self.login,)
    self.login_button_main_window.place(x=750, y=300)

    self.register_button_main_window = util.get_button(self.main_window, 'register new user', 'gray', self.register, fg='black')
    self.register_button_main_window.place(x=750, y=400)

  def login(self):
    pass

  def register(self):
    pass

  def start(self):
    self.main_window.mainloop()

if __name__=="__main__":
  app = App()
  app.start()
