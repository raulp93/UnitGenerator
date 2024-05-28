import time

print("main.py is running...")

units = ['mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi']

def getUnit():
    """ Gets a random number and uses it to choose a random unit"""
    # using the Random Number Microservice API
    # 
    # change the file names below to the complete file directory of where the Request.txt file is locatated
    # that gets written to from the RandomNumberGenerator.py file

    
    with open("Random_Number_Generator\\CS-361-Assignment-8\\Request.txt", "w") as outfile:
        outfile.write("Send a number")
    # gives the program time to recieve the request and to respond with the number
    time.sleep(1.2)

    with open("Random_Number_Generator\\CS-361-Assignment-8\\Request.txt", "r") as infile:
        number = int(infile.read())
    
    return units[number % len(units)]
    



    


while True:
    with open("request.txt", "r") as infile:
        log = infile.read()
    open("request.txt", "w").close()
    
    if log == "send a unit":

        unit = getUnit()
    
        with open("response.txt", "w") as outfile:
            outfile.write(unit)

    time.sleep(1)