import unittest
from gen.examresult import ExamResult
from analysis.result import ResultAnalysis
class ResultAnalysisTest(unittest.TestCase):

    def test_intersection(self):
        exam_result = ExamResult()
        _labels = exam_result.gen_labels()
        raw_data = exam_result.gen_items(_labels)
        analysis = ResultAnalysis()
        issues = analysis.issue_frequency(raw_data)
        print(issues)
        
        

if __name__ == '__main__':
    unittest.main()