import PySimpleGUI as sg

layout = [[sg.Text("Welcome to Optimization Bot! We're here to enhance your experience. Please press the button below to potentially boost your PC's speed by 4-15%.")],[sg.Button('Click me')]]


import os
import shutil
import subprocess

#getting username
print("Just a second :),Hope you don't mind.")
def username():
    for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
       user= os.environ.get(name)
       if user:
          return user
       
#clearing tempfiles
def clear_tempfile(user):
   path = r"C:\Users\\" +user+"\AppData\Local\Temp"
   contents= os.listdir(path)
   for item in contents:
      item_path=os.path.join(path,item)
      try:
         if os.path.isfile(item_path):
            os.remove(item_path)
         elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
         else:
                print(f"Skipped: {item_path} (Not a file or directory)\n")
      except Exception as e:
            print(f"Error deleting {item_path}: {e}\n")

#clearing prefetch
def clear_prefetch(user):
   path = r"C:\Windows\Prefetch"
   contents= os.listdir(path)
   for item in contents:
      item_path=os.path.join(path,item)
      try:
         if os.path.isfile(item_path):
            os.remove(item_path)
         elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
         else:
                print(f"Skipped: {item_path} (Not a file or directory)\n")
      except Exception as e:
            print(f"Error deleting {item_path}: {e}\n")

def cmd_propmt(user):                #@Louis047
    result = subprocess.run(["ipconfig","/flushdns"], capture_output=True, text=True)
    if result.returncode == 0:
       print(result.stdout)
    else:
       print("Error running ipconfig:", result.stderr)
     
# Create the window
window = sg.Window(title="Hello World", margins=(100, 50),layout=layout)
# Event loop to process events and get input from the user
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Click me':
        
        user=username()
        print(user)
        clear_tempfile(user)
        clear_prefetch(user)
        cmd_propmt(user)
        print("Done.")

        