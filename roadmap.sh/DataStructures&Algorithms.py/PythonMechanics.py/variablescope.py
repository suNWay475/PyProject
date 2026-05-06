x = 'global'
print(x)
def outer():
    x = 'enclosing'

    def inner():
        global x 
        x = 'local'
        print(x) 

    inner()

outer()
print(x)
