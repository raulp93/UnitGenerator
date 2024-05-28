import time

while True:

    A = input("Enter a 1 to request a random unit for conversion: ")

    if A != "1":
        print("ok bye.")
        exit()
    
    else:
        with open("request.txt", 'w') as outfile:
            outfile.write("send a unit")
        time.sleep(1.5)

        with open("response.txt", "r") as infile:
            unit = infile.read()
        print("\nThe random unit is: ", unit)


