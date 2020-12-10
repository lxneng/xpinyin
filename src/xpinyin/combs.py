from typing import List


def _get_comb_indexes(num_options_list: List[int], n=None) -> List[List[int]]:
    """
    Given a list with the number of possible options per place, returns a list of numbers representing combinations.
    The combinations are created via additions to a multi-radix number, from left to right
    (i.e. from smaller to larger numbers).

    e.g. [2, 2, 1] -> [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0]]
    i.e. we have 2 options (0, 1) for the first and second places and one option (0) for the third.

    :param num_options_list: a list with the number of options per place
    :param n: The maximal number of requested combinations. If None, all possible combinations will be returned
    """
    # calculate the maximal number of possible combinations
    n_max = 1
    for j in num_options_list:
        n_max *= j
    n = min(n, n_max) if n is not None else n_max
    if n == 0:
        raise ValueError("Can't create combinations with 0-length lists")

    n_items = len(num_options_list)
    curr = [0] * n_items
    combs = [list.copy(curr)]
    i = n_items - 1
    count = 1
    while count < n:
        curr[i] = (curr[i] + 1) % num_options_list[i]
        if curr[i] != 0:
            combs.append(list.copy(curr))
            count += 1
            i = n_items - 1  # reset to right-most digit
        else:
            i -= 1  # try previous (left) digit

    return combs


def get_combs(options: List[List[str]], splitter: str = '', n: int = None) -> List[str]:
    """
    Given a list of options per place, returns up to n combinations
    e.g.: [['a'], ['1' ,'2'], ['@']] -> [a1@, a2@]
    For instance, ['1' ,'2'] is the group defining the options for the second place

    :param options: a list with a list of options for each group.
    :param splitter: a string to separate the groups
    :param n: The maximal number of requested combinations. If None, all possible combinations will be returned
    """
    combs = []
    comb_numbers = [len(o) for o in options]
    combs_indexes = _get_comb_indexes(comb_numbers, n)

    for c in combs_indexes:  # e.g. [0,2,1]
        comb = []
        for i in range(len(c)):
            comb.append(options[i][c[i]])
        combs.append(splitter.join(comb))

    return combs
