import os
import shutil

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

#clearing recent
if __name__ ==  "__main__":
    user=username()
    clear_tempfile(user)

    print("Cleaned Successfully")
   

