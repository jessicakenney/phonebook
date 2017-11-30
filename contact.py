#!/usr/bin/python3.6

class Contact:

    #Contact attributes:
    # name
    # number
    # address
    # note
    def __init__(self, **kwargs):
        self.variables = kwargs

    def set_variable(self,k,v):
        self.variables[k] = v

    def get_variable(self,k):
        return self.variables.get(k,None)

    #if __name__ == "__main__": main()
