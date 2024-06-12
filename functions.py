FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ this function gets all the todos from the text file """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """ this function writes a todo onto the text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)