import os
import sys
# Eclipse Interpreter
currentlinereading = ""
ReadFile = "null"
lines = []
ifconsolemoduleloaded = False

currentline = 0
havereadthroughfile = False # STAY FALSE ON INTERPRETER BOOT
configline = sys.argv[1]


ReadFile = configline

if os.path.exists(ReadFile) == False:
    print("ERROR: File Cannot be found:",ReadFile)
    print("Interpreter Halted.")
    os.system("pause")
    quit()
file = open(ReadFile)
filelines = file.readlines()
for i in filelines:
    

    
        lines.append(i)
    
        currentlinereading = lines[currentline]
        
    
        if(currentlinereading.startswith("console.output")):
            currentlinereading = currentlinereading[15:]
            print(currentlinereading)
            lines.pop(currentline)

        elif(currentlinereading.startswith("console.end")):
                quit()
        
        elif(currentlinereading.startswith("console.pause")):
            input("Press Enter to continue...")


        elif(currentlinereading.startswith("console.system")):
            currentlinereading = currentlinereading[15:]
            os.system(currentlinereading)
        
        elif(currentlinereading.startswith("//")):
            # THIS IS JUST COMMENT
            lines.pop(currentline)
            



            

        