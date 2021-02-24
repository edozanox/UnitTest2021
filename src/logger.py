global class MyLogger():
    
    def __init__(self, message):
        global allLogStrings = []
        self.message = message
        strIsValid: bool = stringIsValid(message)        
        
    
    def checkAndPushOrDelete(message):
        if message != None or message != "":
            allLogStrings.insert(message)
            return True
        else:
            return False

        