import unittest
from gen.examresult import ExamResult
class ExamResultTest(unittest.TestCase):
    def setUp(self):
        self.exam_result = ExamResult()
    
    def test_gen_labels(self):
        print(self.exam_result.get_labels())
        pass
    
    def test_gen_items(self):
        """
        docstring
        """
        print(self.exam_result.gen_items())
    
    def tearDown(self):
        pass
    

if __name__ == '__main__':
    unittest.main()