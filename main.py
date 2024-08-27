import tkinter as tk
import cv2
from PIL import Image, ImageTk  

import util

class App:
  def __init__(self):
    self.main_window = tk.Tk()
    self.main_window.geometry("1200x520+350+100")

    self.login_button_main_window = util.get_button(self.main_window, 'login', 'green', self.login,)
    self.login_button_main_window.place(x=750, y=300)

    self.register_button_main_window = util.get_button(self.main_window, 'register new user', 'gray', self.register, fg='black')
    self.register_button_main_window.place(x=750, y=400)

    self.webcam_label = util.get_img_label(self.main_window)
    self.webcam_label.place(x=10, y=0, width=700, height=500)

    self.add_webcam(self.webcam_label)

  def add_webcam(self, label):
    if 'cap' not in self.__dict__:
      self.cap = cv2.VideoCapture(0)

    self._label = label
    self.process_webcam()

  def process_webcam(self):
    ret, frame = self.cap.read()

    self.most_recent_capture_arr = frame

    img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)

    self.most_recent_capture_pil = Image.fromarray(img_)

    imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)

    self._label.img = imgtk
    self._label.configure(image=imgtk)

    self._label.after(20, self.process_webcam)

  def login(self):
    pass

  def register(self):
    pass

  def start(self):
    self.main_window.mainloop()

if __name__=="__main__":
  app = App()
  app.start()
