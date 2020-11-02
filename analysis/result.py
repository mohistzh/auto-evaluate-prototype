from collections import defaultdict
class ResultAnalysis:
    
    def _one_dimention(self, raw_data):
        arr = []
        for val in raw_data.values():
            arr.extend(val)
        return arr
    
    
    def issue_frequency(self, raw_data):
        arr = self._one_dimention(raw_data)
        base = len(arr)
        issues = defaultdict(int)
        for item in arr:
            issues[item] += 1
        
        percentage = defaultdict(int)
        for key in issues:
            percentage[key] = str(round((issues[key] / base * 100), 2)) + '%'
        
        return issues, percentage
        