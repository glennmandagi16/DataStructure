def larger(data_ptr1, data_ptr2, compare_function):
    if compare_function(data_ptr1, data_ptr2) > 0:
        return data_ptr1
    else:
        return data_ptr2