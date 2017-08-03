""" module to display the UI to the terminal """


# self modules
from todo import Todo


HELPER = """
Add a todo list:        >>> add [string]
Remove a todo list:     >>> del [list_id]
List out all todos:     >>> ls
List out a todo list:   >>> ls [list_id]
Save todos list:        >>> save [string]
Load todos list:        >>> load [string]
Quit the application:   >>> You can't quit the application
"""

WELCOME = """
DumbTodos v0.0.0 (this is a demo and will always be demo)
Press "help" for help (duh)
"""


def ask_option():
    """ ask for user input and tokenise them
    Args:
        None
    Returns:
        (string, integer|string)
    """
    input_text = input(">>> ").split(" ")
    cmd, args = input_text[0], str.join(" ", input_text[1:])
    if args.isdigit():
        args = int(args)
    return cmd, args


def main():
    """ main UI function """

    todo_list = Todo()

    while True:
        cmd, args = ask_option()
        cmd = cmd.lower()

        try:
            if cmd == "add":
                todo_list.add(args)

            elif cmd == "del":
                todo_list.remove(args)

            elif cmd == "ls" and args:
                print(todo_list.show(args))

            elif cmd == "ls":
                for todo in todo_list.show_all():
                    print(todo)

            elif cmd == "save":
                todo_list.save(args)

            elif cmd == "load":
                todo_list.load(args)

            elif cmd == "help":
                print(HELPER)

            elif cmd == "q":
                break

            else:
                print("Invalid option")

        except Exception as err:
            print("ERROR: " + str(type(err)) + " - " + str(err))


if __name__ == "__main__":
    print(WELCOME)
    print(HELPER)
    main()
