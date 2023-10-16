"""
Name: Liam Keefe
Course: CS361 Assignment 1
Due Date: 10/9/2023
Description: refer to readme_schedule.txt
"""
import time
    
import prng
import imgsrv
    
def create_ui()-> None:
    """_summary_
    """
    print()
    print("Hello and Welcome to Assignment 1 for CS361.")
    print("This program takes an option to run/not run, if choosen to run, the program will display a random image.")
    print()
    while(1):
        inputVar = input("Please input whether to display random [desert] image, 1 for image, 2 to exit: ")
        
        print("You have input: " + inputVar)
        print()
        
        if (inputVar == "1"):
            with open("prng-service.txt", 'w+') as t:
                t.write("run")
            time.sleep(5)
            with open("prng-service.txt", 'r+') as t:
                digVal = t.readline()
                t.write('')
            
            with open("imgsrv-service.txt", 'w+') as h:
                h.write(digVal)
            
            time.sleep(5)
            
            with open("imgsrv-service.txt", 'r') as h:
                filePath = h.readline()
            
            print("File path: ")
            print(filePath)
            print()

                    
        elif (int(inputVar) == 2):
            print("You are now exiting the service, Goodbye")
            with open("prng-service.txt", 'w') as f:
                f.write('')
                f.write('0')
            with open("imgsrv-service.txt", 'w') as f:
                f.write('')
                f.write('0')
            
            exit()
            
        else:
            print("You have input an invalid option, please try again")
            print()
        
    return

def main():
    create_ui()
    
if __name__ == '__main__':
    main()