import unittest 
from src import main_class as mc


class StringSanitizerTest (unittest.TestCase):
{
    def DivisionByZero(self):
        with self.assertRaises(DivisionByZero) as ex:

    def ConcatVariousElements(self):
        return "METODO NON IMPLEMENTATO"


    def ToUpperCase(self):
        testStringTUC = mc.upper_string(self)
       self.assertEqual("CIAO COME VA 123?")
    
    def StringSanitizerTest(self):
        testStringSST = mc.sanitize_string(self)
        self.assertEqual("STRINGA-DI-PROVA")        

        


}