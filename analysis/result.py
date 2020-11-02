class ResultAnalysis:
    def __init__(self, raw_data):
        self.arr = self._one_dimention(raw_data)
        
    def _one_dimention(self, raw_data):
        arr = []
        for val in raw_data.values():
            arr.extend(val)
        return arr
    
    
    def intersection(self, labels):
        '''
            [labels] raw labels data
        '''
        print(self.arr)
        pass
        