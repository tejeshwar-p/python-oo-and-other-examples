# *variable_params are also called args (arguments) can be given like - *args
# **kwargs are called keyword arguments
def example_method_1(mandatory_param, default_param="Default"
                     , *variable_params, **kwargs):
    print(f"""
            mandatory_param = {mandatory_param} 
            default_param={default_param}
            *variable_param={variable_params}
            **kwargs={kwargs}
            """)

# TypeError: example_method_1() missing 1 required positional argument: 'mandatory_param'
# example_method_1()


example_method_1(15)
example_method_1(mandatory_param=15)  # named parameter
example_method_1(25, 45)  # python does not care about type
example_method_1(25, "Some String")
example_method_1(25, "String1", "String 2", "String 3")
example_method_1(25, "String1", "String 2", "String 3", "String 4", "String 5")



