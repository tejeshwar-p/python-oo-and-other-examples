def example_method_1(mandatory_param, default_param="Default"
                     , *variable_params, **kwargs):
    print(f"""
            mandatory_param = {mandatory_param}, type = {type(mandatory_param)}
            default_param={default_param}, type = {type(default_param)}
            *variable_params={variable_params}, type = {type(variable_params)}
            **kwargs={kwargs}, type = {type(kwargs)}
            """)


example_method_1(25, "String 1", "String 2", key1='a', key2='b')
example_method_1(25, "String 1", key1='a', key2='b')
# If all the parameters are named then the order does not matter
example_method_1(key1='a', key2='b', mandatory_param=25, default_param="String 1")

# We can not pass the positional arguments after passing the keyword arguments, in other words,
# we need to pass positional arguments first before passing the keyword arguments.
# https://stackoverflow.com/questions/69244318/how-to-pass-arguments-to-args-after-keyword-arguments


