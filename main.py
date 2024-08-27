import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk  
import os
import datetime
import subprocess
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

    self.db_dir = './db'
    if not os.path.exists(self.db_dir):
      os.mkdir(self.db_dir)

    self.log_path = './log.txt'

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
    unknown_img_path = './.tmp.jpg'

    cv2.imwrite(unknown_img_path, self.most_recent_capture_arr)

    output = subprocess.check_output(['face_recognition', self.db_dir, unknown_img_path])
    
    output = output.decode('utf-8')

    # Print the output to see its format
    print("Raw output from face_recognition:", output)

    # Example output: "./db/person1.jpg, person1\n"
    if output.strip() and ',' in output:
        name = output.split(',')[1].strip()
    else:
        name = 'unknown_person'

    if name in ['unknown_person', 'no_persons_found']:
        util.msg_box('Unknown user. Please register new user or try again')
    else:
        util.msg_box('Welcome back!', f'Welcome, {name}')
        with open(self.log_path, 'a') as f:
            f.write('{},{}\n'.format(name, datetime.datetime.now()))
            f.close()
    
    print(output)
    
    os.remove(unknown_img_path)

  def register(self):
    self.register_window = tk.Toplevel(self.main_window)
    self.register_window.geometry("1200x520+370+120")

    self.accept_button_register_main_window = util.get_button(self.register_window, 'Accept', 'green', self.accept_register,)
    self.accept_button_register_main_window.place(x=750, y=300)

    self.try_again_button_register_main_window = util.get_button(self.register_window, 'Try Again', 'red', self.try_again_register,)
    self.try_again_button_register_main_window.place(x=750, y=400)

    self.capture_label = util.get_img_label(self.register_window)
    self.capture_label.place(x=10, y=0, width=700, height=500)

    self.add_img_to_label(self.capture_label)

    self.entry_text_register = util.get_entry_text(self.register_window)
    self.entry_text_register.place(x=750, y=150)

    self.text_label_register = util.get_text_label(self.register_window, 'Input username:')
    self.text_label_register.place(x=750, y=100)

  def add_img_to_label(self, label):
    imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
    label.imgtk = imgtk
    label.configure(image=imgtk)

    self.register_capture = self.most_recent_capture_arr.copy()

  def accept_register(self):
   name = self.entry_text_register.get(1.0, 'end-1c').strip()
   if not name:
      messagebox.showerror("Error", "Username cannot be empty.")
      return

  # Save the temporary image to check for matches
   temp_img_path = './.temp_register.jpg'
   cv2.imwrite(temp_img_path, self.register_capture)

  # Perform face recognition to check for existing users
   output = subprocess.check_output(['face_recognition', self.db_dir, temp_img_path])
   output = output.decode('utf-8')

  # Print the output to see its format
   print("Raw output from face_recognition during registration:", output)

   if output.strip() and ',' in output:
      existing_name = output.split(',')[1].strip()
   else:
      existing_name = 'unknown_person'

  # Check if the face matches an existing user
   if existing_name != 'unknown_person':
      util.msg_box('User Already Exists', f'The face you are trying to register matches with "{existing_name}". Please log in instead.')
      os.remove(temp_img_path)  # Clean up the temporary image
      return

   # No matching face found, proceed with registration
   file_path = os.path.join(self.db_dir, f'{name}.jpg')
   if cv2.imwrite(file_path, self.register_capture):
      util.msg_box("Success", f"User '{name}' registered successfully!")
      self.register_window.destroy()
   else:
      messagebox.showerror("Error", "Failed to save image.")

   os.remove(temp_img_path)  # Clean up the temporary image


  def try_again_register(self):
    # Clear the current image displayed in the label
    self.capture_label.configure(image='')

    # Capture a new image from the webcam
    self.register_capture = self.most_recent_capture_arr.copy()

    # Display the new captured image in the label
    self.add_img_to_label(self.capture_label)


  def start(self):
    self.main_window.mainloop()

if __name__=="__main__":
  app = App()
  app.start()
