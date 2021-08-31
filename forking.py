import os

# Press the green button in the gutter to run the script.
# Use this version on Linux or Mac
# Comment out if you are using Windows
if __name__ == '__main__':
    print(f"Main is running is {os.getpid()}")
    print(f"Main's parent is {os.getppid()}")
# Uncomment the following two lines of code
#    result = os.fork()
#    if result == 0: #Remember, result returns pid of the child to the parent
#   1. Add two lines of code inside of this if statement which print the PID of the child and the pid of the parent
#    else:
#   2. Add two lines of code inside of this else statement which print the PID of the child and the pid of the parent


# Uncomment and use this version if you are running on Windows
"""
import multiprocessing

def child():
#   2. Add two lines of code inside of this else statement which print the PID of the child and the pid of the parent

if __name__ == '__main__':
    print(f"Main's PID is {os.getpid()}")
    print(f"Main's parent is {os.getppid()}")
        
    p1 = multiprocessing.Process(target=child)
    p1.start()
    #   1. Add two lines of code inside of this if statement which print the PID of the child and the pid of the parent
    #   1. HINT - you'll need to use the multiprocessing library to child's PID here. Take a look at the methods associated with the process class.
    p1.join()
"""