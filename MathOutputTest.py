def add_numbers(a , b):
    return a + b
     
##
if __name__=="__main__":
    function_pass =  add_numbers(10,10)
    function_fail =  add_numbers(20,10)

    assert function_pass == 20,"Test passed expected 20"
    assert function_pass == 40,"Test failed expected 30 but got 40"

