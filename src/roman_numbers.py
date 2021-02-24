#from tests import roman_numbers_test

class RomanNumber():

    def __init__(self, string_nmbr):

        self.string_nmbr: str = string_nmbr
        isValid: bool = charsAreValid(string_nmbr)
        if not isValid:
            raise Exception
    
    
    def charsAreValid(self):             
        valid_chars = ['I', 'X', 'M', 'V', 'L', 'C', 'D']

        areValid: bool = False
        
        splitted_roman_num = self.string_nmbr.split()        

        for x in roman_num:
            if x not in valid_chars:
                areValid = False
                return areValid
            else:
                areValid = True
               
        return areValid
    
    
    