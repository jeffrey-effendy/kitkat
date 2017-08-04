""" set of testcases for todo.py """


# core modules
import os
import unittest
from unittest.mock import patch

# test module
import todo


def generate_todo_object():
    """ helper method to generate todo object """
    todo_list = todo.Todo()
    todo_list._id = 4
    todo_list.id_to_todo = {1: "I need to think of a scenario",
                            2: "I need to write a test",
                            3: "I need to go sleep"}
    return todo_list


class TodoTestCase(unittest.TestCase):
    """ testcase collectinos for Todo class """

    def setUp(self):
        # generating initial todo_list
        self.todo_list = generate_todo_object()

    def tearDown(self):
        # data cleanup
        if os.path.exists("data/test.pkl"):
            os.remove("data/test.pkl")

    def test_add(self):
        """ to test add method
        Scenarios:
        1. If I add a todo, then there should be extra todos in the list
        2. If I add an empty todo, then it should raise a ValueError
           and there is no change in the list
        """
        # variable preparation for assertion later
        curr_id = self.todo_list._id
        todo_added = "search for more things to do"

        # scenario 1 test
        print("test scenario 1: START")
        self.todo_list.add(todo_added)

        err = "the length of id_to_todo should increase by 1"
        self.assertEqual(len(self.todo_list.id_to_todo), 4, err)

        err = "the string stored, should be equal to added string"
        self.assertEqual(self.todo_list.id_to_todo[curr_id], todo_added, err)

        err = "the next id should be changed"
        self.assertNotEqual(self.todo_list._id, curr_id, err)

        print("test scenario 1: PASS")

        # scenario 2 test
        print("test scenario 2: START")

        # adding empty string or None should return error
        self.assertRaises(ValueError, self.todo_list.add, "")
        self.assertRaises(ValueError, self.todo_list.add, None)

        # the list should not get updated
        err = "list is updated when ValueError is raised"
        self.assertEqual(len(self.todo_list.id_to_todo), 4, err)

        print("test scenario 2: PASS")

    def test_remove(self):
        """ to test remove method
        Scenarios:
        1. If I remove a todo, then there should be one less todos in the list
        2. If I remove non existent todo, then it should return a KeyError and
           there should not be a change in the list
        """
        # scenario 1 test
        print("test scenario 1: START")
        id_to_remove = 2
        self.todo_list.remove(id_to_remove)

        err = "id 2 should not exist"
        self.assertNotIn(id_to_remove, self.todo_list.id_to_todo, err)

        err = "the length should only decrease by 1"
        self.assertEqual(len(self.todo_list.id_to_todo), 2, err)

        print("test scenario 1: PASS")

        # scenario 2 test
        print("test scenario 2: START")
        id_to_remove = 5

        # removing non existent id should return error
        self.assertRaises(KeyError, self.todo_list.remove, id_to_remove)

        # the list should not get updated
        err = "list is updated when ValueError is raised"
        self.assertEqual(len(self.todo_list.id_to_todo), 2, err)

        print("test scenario 2: PASS")

    def test_save_load(self):
        """ to test save/load method
        Scenarios:
        1. If I save the list, then a file should exist in the data folder
        2. If I load from saved file, I will receive list with same state
        """
        # scenario 1 test
        print("test scenario 1: START")

        self.todo_list.save("test.pkl")
        self.assertTrue(os.path.exists("data/test.pkl"))

        print("test scenario 1: PASS")

        # scenario 2 test
        print("test scenario 2: START")

        empty_list = todo.Todo()
        empty_list.load("test.pkl")

        err = "the todo_list state should be similar"
        self.assertEqual(empty_list._id, self.todo_list._id, err)
        self.assertDictEqual(empty_list.id_to_todo, self.todo_list.id_to_todo, err)

        print("test scenario 2: PASS")

    @patch("storage.save")
    def test_save(self, mock_save):
        """ to test save method
        Scenarios:
        1. If call with proper name, then it will return success and call the
           function storage.save properly
        """
        # scenario 1 test
        print("test scenario 1: START")

        status = self.todo_list.save("test.pkl")

        err = "save is not run successfully"
        self.assertTrue(status, err)

        # save should be called with proper arguments
        mock_save.assert_called_with(dict(self.todo_list), "test.pkl")

        print("test scenario 1: PASS")

    @patch("storage.load")
    def test_load(self, mock_load):
        """ to test load method
        Scenarios:
        1. If call with proper name, then it will return success and call the
           function storage.load properly, the loaded list should be the same
           as the test list
        """
        # set the mock_load return value
        mock_load.return_value = dict(self.todo_list)

        # scenario 1 test
        print("test scenario 1: START")

        empty_list = todo.Todo()
        status = empty_list.load("test.pkl")

        err = "load is not run successfully"
        self.assertTrue(status, err)

        # load should be called with proper arguments
        mock_load.assert_called_with("test.pkl")

        err = "the todo_list state should be similar"
        self.assertEqual(empty_list._id, self.todo_list._id, err)
        self.assertDictEqual(empty_list.id_to_todo, self.todo_list.id_to_todo, err)

        print("test scenario 1: PASS")
