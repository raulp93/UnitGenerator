# OVERVIEW:

This program is designed to work with the RandomNumberGenerator microservice. Ensure that the file pathways in main.py are updated to reflect the actual locations of the 'Request.txt' file that
The Random Number Generator program uses for communication.

The recommended method of using this program is create a directory on your machine and clone this repository to it. Within the same parent directory, create new directory and clone the 
Random Number Generator program. The URL for that program is: https://github.com/raulp93/Random_Number_Generator.git  It is forked from https://github.com/YuPhengXiong/CS-361-Assignment-8.git



# HOW TO REQUEST DATA:
To request data, a program must write 'send a unit' to the request.txt file in the directory that main.py is in.


# HOW TO RECEIVE DATA:

To receive data, a program must read the output in the 'response.txt' file that is in the same directory that main.py is in.
After requesting data, you must give the program about 1.5 seconds before attempting to read the data from 'response.txt'

# Sample test program:

There is a simple example program called test.py that is included. To view how this program works, run main.py, test.py, and RandomNumberGenerator.py each in seperate terminals. 
Use the terminal that test.py is running in to interact and request/recieve data.
