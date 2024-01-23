def argsort(input_list: list, key=None):
    """
    Sort the indices of the given list.

    Parameters
    ----------
    input_list : list
        List to sort.

    Returns
    -------
    list
        List of indices giving the sorted list.
    """
    if key == None:
        def key(x): return x[1]
    res = [i[0] for i in sorted(enumerate(input_list), key=key)]
    return res
