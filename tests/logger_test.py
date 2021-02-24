import unittest
import sys
import os
sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)]) 
from logger import logger 

class LoggerTest(unittest.TestCase):
    
    def empty_string_is_not_valid(self):
        msg = ""
        self.assertFalse(logger.MyLogger.checkAndPushOrDelete(msg))
        
    
    def none_string_is_not_valid(self):
        msg = None
        self.assertFalse(logger.MyLogger.checkAndPushOrDelete(msg))
                

    def correct_string_is_valid(self):
        arrayTestMessage = ["Test1 log message", "Test2 log message", "Test3 log message"]
        for x in arrayTestMessage:
            self.assertTrue(logger.MyLogger.checkAndPushOrDelete(x))
    


if __name__ == '__main__':
    unittest.main()


