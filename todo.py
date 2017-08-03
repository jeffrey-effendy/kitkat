""" contain implementation of Todo class """


# self modules
import storage


class Todo:
    """ a class initialise todo class """

    NO_ID_ERROR = "specified id does not exist"

    EMPTY_LIST = "there are no todos in the list"

    INV_ARGUMENTS = "arguments are invalid"

    def __init__(self):
        self._id = 1
        self.id_to_todo = {}

    def add(self, todo):
        """ method to remove single todo
        Args:
            todo: string
        Returns:
            None
        Raises:
            ValueError - when todos is falsy
        """
        if not todo:
            raise ValueError(self.INV_ARGUMENTS)
        self.id_to_todo[self._id] = str(todo)
        self._id = self._id + 1

    def remove(self, tid):
        """ method to remove single todo
        Args:
            tid: integer
        Returns:
            None
        Raises:
            KeyError: when no id is inside the list
        """
        if tid not in self.id_to_todo:
            raise KeyError(self.NO_ID_ERROR)
        del self.id_to_todo[tid]
    
    def show(self, tid):
        """ method to show a single todo
        Args:
            tid: integer
        Returns:
            string
        Raises:
            KeyError: when no id is inside the list
        """
        if tid not in self.id_to_todo:
            raise KeyError(self.NO_ID_ERROR)
        return self.id_to_todo[tid]

    def show_all(self):
        """ method to show a single todo
        Args:
            tid: integer
        Returns:
            [string]
        """
        if not self.id_to_todo:
            return [self.EMPTY_LIST]
        out = []
        text = "[{}] {}"
        for tid, todo in self.id_to_todo.items():
            out.append(text.format(tid, todo))
        return out

    def save(self, filename):
        """ save current state of todos list
        Args:
            filename: string
        Returns:
            None
        """
        pyobj = {"_id": self._id, "id_to_todo": self.id_to_todo}
        storage.save(pyobj, filename)

    def load(self, filename):
        """ save current state of todos list
        Args:
            filename: string
        Returns:
            None
        """
        pyobj = storage.load(filename)
        self._id = pyobj["_id"]
        self.id_to_todo = pyobj["id_to_todo"]
