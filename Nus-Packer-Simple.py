from sys import exit
from time import sleep
from os import system
inputdir = input("Unpacked Game Directory (No Quotation Marks)(EX: C:/Game/Unpacked/WiiU Game): ")
inputdir = f'"{inputdir}"'

outputdir = input("\nPacked Game Directory (No Quotation Marks)(EX: C:/Game/Packed/WiiU Game): ")
outputdir = f'"{outputdir}"'

ckeyval = 0
while ckeyval != 32:
    commonkey = input("\nCommon Key (32 Characters): ")
    ckeyval = len(commonkey)
    if ckeyval != 32:
        print("\nInvalid Common Key: Make Sure It Has 32 Characters")


NusDir = input("\nDirectory NusPacker Is In (No Quotation Marks)(EX: C:/Java/NusPacker): ")

NusDir = f'"{NusDir}"'



infocheck = False
while infocheck == False:
    print(f"\nUnpacked Directory: {inputdir}")
    print(f"Output Directory: {outputdir}")
    print(f"Nuspacker Directory: {NusDir}")
    print(f"Common Key: {commonkey}")
    choice = input("\nAre These Correct? (y- Yes, n- no): ")
    if choice == "y":
        infocheck = True
    elif choice == "n":
        checkchange = False
        while checkchange == False:
            print("\n1- Unpacked Directory")
            print("2- Output Directory")
            print("3- Nuspacker Directory")
            print("4- Common Key")
            choice2 = input("\nWhat Would You Like To Change: ")
            if choice2 == "1":
                inputdir = input("Input New Directory Here: ")
                checkchange = True
            elif choice2 == "2":
                outputdir = input("Input New Directory Here: ")
                checkchange = True
            elif choice2 == "3":
                NusDir = input("Input New Directory Here: ")
                checkchange = True
            elif choice2 == "4":
                commonkey = input("New Common Key Here: ")
                checkchange = True


system("start cmd /K cd "f"{NusDir} & timeout 5 & java -jar NUSPacker.jar -in "f"{inputdir}"" -out "f"{outputdir}" " -encryptKeyWith " f"{commonkey}")


file = "Copy-Into-CMD.txt"
with open(file, 'w') as openfile:
    openfile.write(f'Step 1, Copy And Paste CD Command: \n\n    cd {NusDir}\n\nStep 2, Copy And Paste Nuspacker CMD Command:\n\n    java -jar NUSPacker.jar -in "{inputdir}" -out "{outputdir}" -encryptKeyWith {commonkey}')


