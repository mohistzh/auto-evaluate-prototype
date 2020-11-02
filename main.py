from gen.examresult import ExamResult
from analysis.result import ResultAnalysis

def main():
    result = ExamResult()
    labels = result.gen_labels()
    items = result.gen_items(labels)
    print("---------------------------Item Bank Data Sample---------------------------")
    for key in items:
        print(key, ' => ', items[key])
    
    
    print("----------------------------------------------------------------------------")
    print()
    
    print("-------------------------Analysis of Results--------------------------------")
    analysis = ResultAnalysis()
    data = analysis.issue_frequency(items)
    percentage = data[1]
    for key in percentage:
        print(key, ' => ', percentage[key])

    print("----------------------------------------------------------------------------")
    
    
if __name__ == '__main__':
    main()