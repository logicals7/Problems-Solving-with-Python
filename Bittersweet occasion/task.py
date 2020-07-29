# finish the function
def find_the_parent(child_):
    if issubclass(child_, Drinks):
        print('Drinks')
    elif issubclass(child_, Pastry):
        print('Pastry')
    elif issubclass(child_, Sweets):
        print('Sweets')