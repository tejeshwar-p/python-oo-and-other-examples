def example_method_1(mandatory_param, default_param="Default"
                     , *variable_params, **kwargs):
    print(f"""
            mandatory_param = {mandatory_param}, type = {type(mandatory_param)}
            default_param={default_param}, type = {type(default_param)}
            *variable_params={variable_params}, type = {type(variable_params)}
            **kwargs={kwargs}, type = {type(kwargs)}
            """)


num_list_1 = [1, 2, 3, 4]
print(num_list_1)
example_method_1(num_list_1[0], num_list_1[1], num_list_1[2], num_list_1[3])

num_list_2 = [1, 2, 3, 4, 5, 6]
print(num_list_2)
example_method_1(*num_list_2)  # This is called unpacking

some_dict = {'a': '1', 'b': '2', 'c': 3}
example_method_1(*num_list_2, **some_dict)


