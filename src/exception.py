import sys
import logging
<<<<<<< HEAD
from src.logger import logging

=======
>>>>>>> bf92202217fcb1d9f34331dc4ad8cc8fa45e2a61

def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # execution info
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error Occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)

<<<<<<< HEAD
    def __str__(self):
        return self.error_message
    
=======

    def __str__(self):
        return self.error_message
    

>>>>>>> bf92202217fcb1d9f34331dc4ad8cc8fa45e2a61
