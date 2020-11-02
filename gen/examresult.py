import random
class ExamResult:
    _instance = None
    # Singleton purpose 
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self._labels = []
        self._gen_labels()
    
    def _gen_labels(self):
        '''
            Generate label collections which use to associate with item
        '''
        for num in range(0, 10):
            random_num = random.randint(1000000, 9999999)
            self._labels.append(random_num)
    
    def get_labels(self):
        return self._labels
    
    
    def gen_items(self):
        '''
            Generate items with the given count
            Item data structure should be more complex in Product env
            In this case, I only need to use label collection, hence the data structure like this:
            "item1": {label1, label2, label4, etc}
        '''
        dict = {}
        # Assume we have multiple issues (use items to present it)
        items = random.randint(1, 100)
        for item in range(1, items):
            issues = random.choices(self._labels, k = random.randint(1, len(self._labels)))
            dict[item] = issues
        
        return dict