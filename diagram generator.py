import os

directory = r'C:\Users\magic\Documents\Applications\PyCharm\PyCharm Projects\solarstuff'
functionNames = []
funcName = "temp"
# First Row is function names
# Rows down are the functions they are called in

#First Get every function name
lastLine = "Constant_Weight_Sizing"
for filename in os.listdir(directory):

    if filename.endswith(".m") or filename.endswith(".exemple"):

        #print("Using " + os.path.join(directory, filename))
        f = open(os.path.join(directory, filename), "r")
        lines = f.readlines()
        # for (i=0, i< len(lines), i++):
        lineNumber = 0
        for line in lines:
            lineNumber = lineNumber + 1
            #Deternmine if each line has a functionS
            if "..." in line:
                lastLine = line;
                continue;

            if "..." in lastLine:
                # print("LastLine:" + lastLine)
                # print("thisLine:" + line)

                line = lastLine + line
                print("Combo:" + line)


            #print()
            if line[0:8] == "function":
                funcStart = line.find(" = ")
                funcEnd = line.find("(")
                funcName = line[funcStart+3:funcEnd]
            #
            # #Check if it has a function in it
            # stringsInFuncDeclaration = ["function", "(", ")", "="]
            # stringsIn = 0;
            #
            # for string in stringsInFuncDeclaration:
            #     if string in line:
            #         stringsIn = stringsIn + 1 # Not really sure why it doesn't like stringsIn++
            #
            # # If Line has all for strings
            # if stringsIn == 4:
            #     # Grab name
            #     funcStart = line.find(" = ")
            #     funcEnd = line.find("(")
            #     funcName = line[funcStart+3:funcEnd]

            if funcName not in functionNames:
                #print(f" Function Declaration({funcName}) in line " + str(lineNumber) + " of " + filename)
                functionNames.append(funcName)

            line = lastLine
        f.close() # when done

print(functionNames)
# Assign names to the 2d array

# #Now find file uses
# for filename in os.listdir(directory):
#     if filename.endswith(".m") or filename.endswith(".exemple"):
#         for line in lines:
#
#     f.close()  # when done


