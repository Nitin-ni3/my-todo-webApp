import os

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """create if file not exist and Read the text file and return
     the list of To-Do's items. """
    filepath=f'files/{filepath}'
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            pass

    with open(filepath, 'r') as read_file:
        store_todos = read_file.readlines()
    return store_todos


def write_todos(todos_agr, filepath=FILEPATH):
    """ Write the To-Do's items list in the text file. """
    with open(f'files/{filepath}', 'w') as write_file:
        write_file.writelines(todos_agr)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())