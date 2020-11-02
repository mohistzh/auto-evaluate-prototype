class ExamResult:
    _instance = None
    
    # Singleton purpose 
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        pass
    
    def gen_labels():
        '''
            Generate label collections which use to associate with item
        '''
        pass

    def gen_items(count):
        '''
            Generate items with the given count
            Item data structure should be more complex in Product env
            In this case, I only need to use label collection, hence the data structure like this:
            "item1": {label1, label2, label4, etc}
        '''
        pass


