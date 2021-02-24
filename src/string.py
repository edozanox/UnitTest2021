from tests import main_class_test
import string

global class StringSanitizer(main_class_test):
{   
    def sanitize_string(self):
        firstString = "STRINGA DI PROVA"
        theSanitizedString = firstString.replace(" ", "-")
        return theSanitizedString
    
    def upper_string(self):
        magicString = "Ciao Come Va 123?"
        sanitizedString = magicString.capitalize()
        return sanitizedString


}
