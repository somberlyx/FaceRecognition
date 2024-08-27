import tkinter as tk 

import util

class App:
  def __init__(self):
    self.main_window = tk.Tk()
    self.main_window.geometry("1200x520+350+100")

    self.login_button_main_window = util.get_button(self.main_window, 'login', 'green', self.login,)

    self.register_button_main_window = util.get_button(self.main_window, 'register new user', 'gray', self.register_new_user, fg='black')

  def start(self):
    self.main_window.mainloop()

if __name__=="__main__":
  app = App()
  app.start()
