import unittest
from gen.examresult import ExamResult
from analysis.result import ResultAnalysis
class ExamResultTest(unittest.TestCase):
    def setUp(self):
        self.exam_result = ExamResult()
        
        
    def test_get_labels(self):
        labels = self.exam_result.gen_labels()
        self.assertTrue(len(labels) < 10)
        print(labels)
    
    def test_get_items(self):
        labels = self.exam_result.gen_labels()
        items = self.exam_result.gen_items(labels)
        for key in items:
            print(key, '=>', items[key])
            self.assertTrue(len(items[key]) < 10)
        
    def tearDown(self):
        pass
    

if __name__ == '__main__':
    unittest.main()