import heapq

class TaskList:
    def __init__(self):
        """
        Initializes an empty priority queue for tasks and a dictionary to map task IDs.
        """
        self.data = []
        heapq.heapify(self.data)
        self.task_map = {}
        self.count=0

    def add_task(self, task_id, task_title, task_priority):
        """
        Adds a new task to the priority queue.

        Arguments:
        task_id (int): Unique identifier for the task
        task_title (str): Name of the task
        task_priority (int): Priority of the task (Lower number means higher priority)
        """
        self.count+=1
        task = (task_priority, self.count, task_title, task_id)
        heapq.heappush(self.data, task)
        self.task_map[task_id] = task
        print("Task added successfully!")

    def view_task(self):
        """
        Displays the highest priority task in the queue.
        """
        if not self.data:
            print("The task list is empty.")
            return
        priority, count, title, task_id = self.data[0]
        print(f"Highest priority task -> {{Id: {task_id}, Title: {title}, Priority: {priority}}}")

    def remove_task(self):
        """
        Removes and displays the highest priority task from the queue.
        """
        if not self.data:
            print("The task list is empty.")
            return
        removed_task = heapq.heappop(self.data)
        task_id = removed_task[3]
        self.task_map.pop(task_id)
        print(f"Task completed and removed -> {{Id: {task_id}, Title: {removed_task[2]}, Priority: {removed_task[0]}}}")

    def check_task(self, task_id):
        """
        Checks if a task with the given ID already exists.

        Argument:
        task_id (int): Unique identifier for the task

        Returns:
        bool: True if task exists, False otherwise
        """
        return task_id in self.task_map

def menu():
    """
    Displays the Task Manager menu and reads user input.

    Returns:
    int or None: The chosen option by the user, or None if input is invalid.
    """
    print("\n----------------------------")
    print("Task Manager Menu")
    print("----------------------------")
    print("1 to Add a new task")
    print("2 to View task")
    print("3 to Remove a task")
    print("4 to Exit the Task Manager")
    print("----------------------------")
    try:
        return int(input("Please enter your choice: "))
    except ValueError:
        return None

print("*****Welcome to Task Manager*****")
task_manager = TaskList()
choice = menu()

while choice != 4:
    if choice == 1:
        try:
            task_id = int(input("Enter task ID: "))
            if task_manager.check_task(task_id):
                print(f"Task ID {task_id} already exists.")
            else:
                task_title = input("Enter task title: ")
                task_priority = int(input("Enter task priority (lower number = higher priority): "))
                task_manager.add_task(task_id, task_title, task_priority)
        except ValueError:
            print("Task ID and priority must be integers.")
    elif choice == 2:
        task_manager.view_task()
    elif choice == 3:
        task_manager.remove_task()
    else:
        print("Invalid option. Please choose a valid menu item.")
    choice = menu()
else:
    print("You signed out. Have a productive day!")
