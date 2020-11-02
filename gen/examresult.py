import random

class ExamResult:
        
    def gen_labels(self):
        '''
            Generate label collections which use to associate with item
        '''
        _labels = []
        for num in range(1, 10):
            random_num = random.randint(1000000, 9999999)
            _labels.append(random_num)
        return _labels
  
    def gen_items(self, labels):
        '''
            Generate items with the given count
            Item data structure should be more complex in Product env
            In this case, I only need to use label collection, hence the data structure like this:
            "item1": {label1, label2, label4, etc}
        '''
        # Assume we have multiple issues (use items to present it)
        _items = {}
        items = random.randint(1, 100)
        for item in range(1, items):
            issues = random.choices(labels, k = random.randint(1, len(labels)))
            _items[item] = issues
        return _items