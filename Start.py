class Start():
    
    age = 0
    string = ''
    
    def __init__(self, object_age=1, version='start'):
        self.object_age = object_age
        self.version = version
        
    def mult(self):        
        Start.age = Start.age + 1
        Start.string = '!!!'

