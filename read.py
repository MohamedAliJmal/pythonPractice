import os
os.chdir(os.path.dirname(__file__))
print(os.getcwd())
file=open("first.txt","a")

file.writelines("hama is comming")
