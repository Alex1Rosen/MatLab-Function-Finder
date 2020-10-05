import os

directory = r'C:\Users\magic\Documents\Applications\PyCharm\PyCharm Projects\solarstuff'
funcNames = [[]]
# First Row is function names
# Rows down are the functions they are called in

#First Get every function name
print("Input the directory to look through(only looks at .m). If None given, default to what is writen in the code")
inDir = input()
if inDir == '':
    inDir = directory

print("Input the name of the function you want to find")

inFunc = input()
#inFunc = "Drag_Polar"

print(f"Finding references of {inFunc}")
for filename in os.listdir(inDir):

    if filename.endswith(".m") or filename.endswith(".otherFileExtension"):

        #print("Using " + os.path.join(directory, filename))
        f = open(os.path.join(directory, filename), "r")
        lines = f.readlines()

        funcCount = 0;
        for line in lines:
            if inFunc in line:

                funcCount = funcCount +1

        #if funcCount > 0:
        print(f"Function: {inFunc} was used {funcCount} times in {filename}")
        f.close() # when done
