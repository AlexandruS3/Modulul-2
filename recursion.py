############ HW2=1 ##########################
def square(value):
    result = value * value
    return result

def square1(value):
    result = value ** 2
    return result

def square2(value):
    result = pow(value,2)
    return result

# 2. alternative solution (args - IN, OUT)
def square3(value):
    res = value[0] * value[0]
    value.pop(0)
    value.insert(0,  res)

n = [10]
square3(n)
print(n)



############ HW2 ##########################

def generalMark(value):
    res = 0
    for i in value.values():
        res += i / len(value)
    
    s = {"gen":res}
    value.update(s)
    
    

v = {
    "sem_1": 9.0,
    "sem_2": 8.0,
    "exam" : 9.0,
}

generalMark(v)
print(v)


############ HW3 ##########################

def increaseInt(n):
    if n == 10:
        print(n)  
        return n
    else:
        result = increaseInt(n+1)
        print(n) 
        return result
    
nn = 8
increaseInt(nn)
#print(nn)