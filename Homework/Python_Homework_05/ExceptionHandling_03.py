try:
    FileName=input("Enter your file name: ")
    file=open(FileName)
    print("Accessed successfully!")
    file.close()
except FileNotFoundError:
    print("It seems there is no such kinda file!")
