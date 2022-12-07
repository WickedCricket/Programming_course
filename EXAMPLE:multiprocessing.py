# Deal with multiple task in python:
# Notes from mCoding's video "Unlocking your CPU cores in Python (multiprocessing)"

# Process: An instance of the Python interpreter has at least one thread called the MainThread.
# Thread: A thread of execution within a Python process, such as the MainThread or a new thread
# Source: https://superfastpython.com/multiprocessing-in-python/

# ________________________________________________________________________________________________________________________________________________
# Notes from mCoding's video "Unlocking your CPU cores in Python (multiprocessing)"

# 1. Asyncio: 
#   - Work together pause/wait usefull if; reading to disk, network (Usefull if there are idle phases of a process).
#   - Works for IO bound.

# 2. Threading:
#   - Python runs on a single thread on a single core (we do not utilise the hardware)
#   - Global interpreter lock aka "GIL" | WRITE + READ or WRITE = "data race" To be able to run a process,
#     The thread needs to aquire the "GIL" this means that despite python being able to run multiple threads,
#     only one of them can aquire GIL at a time and this execute python code.
#
#   - We DO gain a performance boost still due to other 'C' codes not caring about the enterpretor's need for GIL, only Python does.
#   - Works for IO bound.
#   - works well when trying to run GUI operations were responsiveness is required despite longer/complicated calculations.

# 3. Multiprocessing: 
#   - Works great for managing independant processes.
#   - Can use "pool objects"; call upon a pool function to tell what task you want executed and the pool takes care of the processes scheduling
#     scheduling the task and collecting the results in a thread and process safe way. Can tell pool max number of processess to start:
#     </> with Pool(processes = 5) as pool: </> | One can also leave it blank and it will only use one process pr core:
#     </> with Pool() as pool: </> | thus each process is it's own interpreter
#   - Does not fight for GIL as it now own it's own GIL.
#   - the "With" statement is used to make sure process coordinate and terminate gracefully (I do not understand what this really means).
#
#   - map : 
#   - imap : 
#   - imap_unordered :


# Introduction: multiple each number with itself (1*1=2, 2*2=4, 3*3=9 ect..) NOTE: We do use the pool function. 
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3, 100, 5, 9, 78, 1039, 5439, 34022, 2341, 2301, 1996, 2007, 2101236]))

# build upon this task: https://docs.python.org/3/library/multiprocessing.html
# Usefull resource: https://superfastpython.com/multiprocessing-in-python/
