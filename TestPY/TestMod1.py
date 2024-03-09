def tm1_function():
    print("module function")

class TestMod1C:
    def tmc_function(self):
        print("module class function")
    tmc_var_str = "four"
    tmc_var_int = 4
    tmc_var_float = 4.0
    def tmc_func_returnself(self):
        return self

tm1_var_classtest = TestMod1C()
tm1_var_classtest2 = TestMod1C()