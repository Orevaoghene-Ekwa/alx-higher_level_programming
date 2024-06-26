#!/usr/bin/python3


def element_at(my_list, idx):
    """
    Returns an element from a list at given index
    """
    list_len = len(my_list)
    if idx < 0 or idx >= list_len:
        return

    return(my_list[idx])
