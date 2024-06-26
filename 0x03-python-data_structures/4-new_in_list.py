#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    replace and elment in a list
    without modifying the original
    """
    list_len = len(my_list)

    if type(my_list) is list:

        if idx < 0 or idx >= list_len:
            return (my_list)
        f_list = my_list.copy()
        f_list[idx] = element
        return(f_list)
