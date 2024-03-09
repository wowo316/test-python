import TestMod1 as M1

def bowling(name="This is"):
    print(name+" bowling")
    return "cheese"
def exception_add(a, b):    
    c = a+b
    if c < 4:
        return
    print(c)
    # If the result of a+b is less than 4, it will return nothing, otherwise it prints c. Test with exception_add down there
def moreorlessthanfive(a):
    if a<5:
        return "less"
    if a>5:
        return "more"
    if a == 5:
        return "equal"
def test_while(a=0):
    while a>0:
        print(a)
        a=a-1
    if a==0:
        print("finish")
def advancedTestWhile(name="",a=1,isadd=True,limit=10):
    if isadd==True:
        while a <= limit:
            print(name+f" {a}")
            a=a+1
    else:
        while a >= limit:
            print(name+f" {a}")
            a=a-1

testList = [1, 2, "four", "cheese pizza", 314.15, True]

print(M1.tm1_var_classtest.tmc_func_returnself())