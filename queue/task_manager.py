import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
print("current directory is: ", current_dir)

parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
print("parent directory is: ", parent_dir)
sys.path.append(parent_dir)

from LinkedList.DoublyLinkedList import DoublyLinkedList

def check_input_type(task_input):
    if task_input.strip():
        return task_input
    else:
        raise ValueError("Please input a valid task")
    

def add_task(task_queue: DoublyLinkedList, front=False, rear=False, index=None):
    title = check_input_type(input("Enter task title: "))
    description = check_input_type(input("Enter task description: "))

    if rear:
        task_queue.add({"title": title, "description": description})
    elif front:
        task_queue.addFirst({"title": title, "description": description})
    elif index is None:
        raise ValueError("Please specify how do you want to insert value")
    elif index is not None:
        task_queue.addAt(index, {"title": title, "description": description})

    print("Task added successfully!")


def complete_task(task_queue: DoublyLinkedList, front=False, rear=False, index=None):
    if sum([front is True, rear is True, index is not None]) > 1:
        raise Exception("You can only tick off one completed task at a time")
    
    if sum([front is False, rear is False, index is None]) == 3:
        raise Exception("You have to specify which task is completed")
    
    if front:
        task_queue.removeFirst()
    elif rear:
        task_queue.removeFirst()
    elif index is not None:
        task_queue.removeAt(index)
    
    print(task_queue)


def update_task(task_queue: DoublyLinkedList, index):
    new_title = check_input_type(input("Enter new task title: "))
    new_description = check_input_type(input("Enter new task description: "))

    updated_task = {"title": new_title, "description": new_description}

    task_queue.updateAtIndex(index, updated_task)


def view_task(task_queue: DoublyLinkedList):
    print(task_queue)


if __name__ == '__main__':
    task_queue = DoublyLinkedList()

    print("Interactive Task Manager")
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            add_task_position = input("Please type 'front' if you would like to add new task as the first task or type 'rear' to add task at the end, or specify the index: ")
            if add_task_position == "front":
                front = True
                add_task(task_queue, front=front)
            elif add_task_position == "rear":
                rear = True
                add_task(task_queue, rear=rear)
            elif add_task_position.strip() and add_task_position != "front" and add_task_position != "rear":
                index = int(add_task_position)
                add_task(task_queue, index=index)
        elif choice == "2":
            view_task(task_queue)
        elif choice == "3":
            update_task_index = int(input("Please enter the index of the task that you want to update: "))
            update_task(task_queue, 2)
        elif choice == "4":
            complete_task_position = input("Please type 'front' if you would like to delete the first task or type 'rear' to delete the last task, or specify the index of the task that you want to delete: ")
            if complete_task_position == "front":
                front = True
                complete_task(task_queue, front=front)
            elif complete_task_position == "rear":
                rear = True
                complete_task(task_queue, rear=True)
            elif complete_task_position.strip() and complete_task_position != "front" and complete_task_position != "rear":
                index = int(complete_task_position)
                complete_task(task_queue, index=index)
        elif choice == "5":
            print("Exiting the Task Manager")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option (1-5).")
