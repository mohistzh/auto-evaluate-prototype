from gen.exam_result import ExamResult
import unittest
from gen.examresult import ExamResult
class ExamResultTest(unittest.TestCase):
    exam_result = None
    def setUp(self):
        exam_result = ExamResult()
    def tearDown(self):
        pass
    
    def test_gen_labels(self):
        print(self.exam_result.get_labels())
        pass

if __name__ == '__main__':
    unittest.main()