# __name__ is a special variable which holds the name of the current module

print(__name__)
# this will return '__main__' if its a module we run using python interpreter or it will be name of the module '__name' if its not executed directly

# if want to execute certain code only if that is main module, then we write following code

if __name__ == "__main__":
    print('Executing main module')
