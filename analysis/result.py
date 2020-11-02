class ResultAnalysis:
    def __init__(self, raw_data):
        self.arr = self._one_dimention(raw_data)
        
    def _one_dimention(self, raw_data):
        return raw_data.values()
    
    
    def intersection(self, labels):
        '''
            [labels] raw labels data
        '''
        print(self.arr)
        pass
        