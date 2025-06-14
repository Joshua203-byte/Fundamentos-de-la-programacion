def load_file():
    fileppath=input("Enter the path of the file to load: ")

    file=open(fileppath, "r", encoding="utf-8")
    lines=file.readlines()
    file.close()
    return lines
my_file=load_file()
print(my_file)

def set_enviroment(raw_file):
    enviroment=[]
    for line in raw_file:
        line
    return enviroment