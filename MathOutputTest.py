def add_numbers(a , b):
    return a + b
     

if __name__=="__main__":
    function_pass =  add_numbers(10,10)
    function_failed =  add_numbers(10,10)

    assert function_pass == 20,"Test passed expected 20"
    assert function_failed == 30,"Test failed expected 20"
    print(function_pass)
    print(function_failed)