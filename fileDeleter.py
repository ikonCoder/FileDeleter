import os

# globals
currDir = os.getcwd()
deletionSel = input("enter the file you want to delete: ")


# script
if os.path.exists(deletionSel):
    os.remove(deletionSel)
else:
    print("The file does not exist")


