# Todos:
# make object oriented
# change order to display
# Search feature

# Old options: print("Enter: 1 to add, 2 to remove, 3 to move")
#              "4 to search, 5 to create a new list, 6 to see existing lists")

import os


class TodoList:
    def __init__(self):
        self.todos = ['todos', 'here']
        self.indent_width = "  "
        self.options = ['display todo list',
                        'add',
                        'remove',
                        'create a new list',
                        'search for a todo',
                        'swap 2 todo positions']

    def display_options(self):
        count = 1
        print('Press:')
        for option in self.options:
            print(self.indent_width + str(count) + ". To " + option)
            count += 1

    def add_todo(self):
        response = input("Please input a todo: \n")
        self.todos.append(response)

    def printTodos(self):
        count = 1
        for todo in self.todos:
            print(self.indent_width + str(count) + ". " + todo)
            count += 1

    def remove_todo(self):
        index = int(input("Which item would you like to remove?"))
        self.todos.pop(index-1)

    def new_list(self):
        pass

    def search_list(self):
        query = input('What would you like to search for?')
        if(self.todos.index(query)):
            print(query + ' is number ' + self.todos.index(query))
        else:
            print('Item not found')

    def swap_todos(self):
        i1 = int(input('Input index of first item'))
        i2 = int(input('Input index of second item'))
        self.todos[i1], self.todos[i2] = self.todos[i2], self.todos[i1]

        # first_val = int(input('Input index of first item')
        # if (first_val > len(list)):


todo_list = TodoList()

# print('Welcome to Python todo!')
while (True):
    print('---------------------------------------------------')
    todo_list.display_options()

    choice1 = int(input(''))
    os.system('cls||clear')

    if choice1 == 1 or choice1 == todo_list:
        todo_list.printTodos()
    elif choice1 == 2:
        todo_list.add_todo()
    elif choice1 == 3:
        todo_list.remove_todo()
    elif choice1 == 4:
        todo_list.new_list()
    elif choice1 == 5:
        todo_list.search_list()
    elif choice1 == 6:
        todo_list.swap_todos()
        todo_list.printTodos()
