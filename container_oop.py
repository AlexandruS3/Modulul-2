class Container:
    is_empty = False
    value    = 123


################ HW1 ########################

def setContainerValue(container,value):
    container.value = value
    container.is_empty = True


################ HW2 ########################



def unsetContainerValue(container):
    container.value = None
    container.is_empty = False

################ HW3 ########################


def printContainerValue(container):
    if container.is_empty == True:
        print ("Container is EMPTY ! ")
    if container.value != None:
        print (f"Container has {container.value} tons ")


