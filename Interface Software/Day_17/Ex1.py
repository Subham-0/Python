# Multi-Threading

"""
There are two types of Processes:
1. Thread-based multitasking
2. Process-based multitasking

Thread-based multitasking:
In thread-based multitasking, many processes run concurrently, all originating from the main thread of a program.

Every program is run by a framework, which is called the main thread. Each main thread has a default thread priority, typically set to 5.

Threads are managed by a thread scheduler, a component of the operating system. The thread scheduler determines the execution order of threads based on their priorities. If threads have the same priority, the scheduler typically follows a "first come, first served" approach.

Child thread and its life cycle:
Every main thread, once created, automatically goes through a life cycle, enabling the thread to start and execute the main program. In contrast, a child thread has its own life cycle stages:

1. Create the child thread.
2. After creating the child thread, call the "start" method. This makes the child thread available to the thread scheduler. Then, call the "run" method to execute the task assigned to the child thread.

How to create a child thread:
1. To create a child thread, we extend a class called "Thread".
2. The "Thread" class is part of the "threading" module in Python.
3. Once we create an object of the "Thread" class, we call the "start" method, which automatically invokes the "run" method.
4. Every program is initially run by the main thread. To retrieve the name of the main thread, we can access its name property."""

# For example, to create and start a child thread in Python:

import threading

# Define a function to be executed by the child thread
def print_numbers():
    for i in range(1, 6):
        print("Child Thread:", i)

# Create a child thread
child_thread = threading.Thread(target=print_numbers)

# Start the child thread
child_thread.start()

# Main thread continues its execution
for i in range(1, 4):
    print("Main Thread:", i)

# Wait for the child thread to complete
child_thread.join()

# Output:
# Child Thread: 1
# Main Thread: 1
# Child Thread: 2
# Child Thread: 3
# Main Thread: 2
# Child Thread: 4
# Main Thread: 3
# Child Thread: 5

"""This example demonstrates how the child thread executes concurrently with the main thread, printing numbers in parallel.

When working with threads, it is important to use synchronization techniques such as locks and semaphores to prevent conflicts and ensure data integrity in multi-threaded programs.
"""

    
from threading import *
def show():
    print("Happy Utkal Divas")
   
for i in range(5):
     t= Thread(target=show)
     t.start()
     print(t)