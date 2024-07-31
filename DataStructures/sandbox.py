
def increment_and_print():
    print(currentLabel) 
    
def function():
    currentLabel = 0
    def increment_and_print():
        print(currentLabel) 
    increment_and_print()

function()