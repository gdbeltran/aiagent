

import unittest
import os
from functions.write_file import write_file

class TestWriteFile(unittest.TestCase):
    def setUp(self):
        self.working_directory = os.path.join(os.getcwd(), "calculator")
        
    def test_lorem_file(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)
        
    def test_more_lorem(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)
        
    def test_invalid(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)

if __name__ == "__main__":
    unittest.main()