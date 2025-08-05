Assignment Title: Task Manager using Priority Queue

Descrption:

1. This is a simple command-line based Task Manager implemented in Python.
2. It utilizes a **priority queue backed by a heap data structure** to efficiently manage tasks based on their priority levels.
3. Tasks with lower numeric values have higher priority.
4. Same priority tasks follow FIFO(First-In-First-Out) rule i.e., First added task is first removed.

Features:

1. Adds a task with a unique ID, title, and priority.
2. View the current highest-priority task.
3. Remove the highest-priority task once it's completed.
4. Prevent duplicate task IDs using a mapping dictionary.

Technologies used:

1. Programming Language: Python 3.13.5
2. Data Structure: Min-Heap (`heapq` module)
