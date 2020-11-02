import unittest
from gen.examresult import ExamResult
from analysis.result import ResultAnalysis
class ResultAnalysisTest(unittest.TestCase):

    def test_intersection(self):
        exam_result = ExamResult()
        labels = exam_result.gen_labels()
        raw_data = exam_result.gen_items(labels)
        analysis = ResultAnalysis(raw_data)
        analysis.intersection(labels)
        
        

if __name__ == '__main__':
    unittest.main()