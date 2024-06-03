import sys


class customerException(Exception):
    def __init__(self,error_message,error_details: sys):
        self.error_message = error_message
        _,_,exc__tb = error_details.exc_info()


    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error number [{2}]".format(
        self.file_name, self.lineno, str(self.error_name))


if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        raise customerException(e,sys)
