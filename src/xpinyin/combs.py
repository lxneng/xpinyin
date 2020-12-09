from typing import List


def _get_comb_indexes(lengths: List[int], n=None) -> List[List[int]]:
    """
    Given a list with the number of possible options per place, returns a list of numbers representing combinations.
    The combinations are created via additions to a multi-radix number, from left to right
    (i.e. from smaller to larger numbers).

    @param n The maximal number of requested combinations.
    """
    # calculate the maximal number of possible combinations
    n_max = 1
    for j in lengths:
        n_max *= j

    n = min(n, n_max) if n is not None else n_max
    if n == 0:
        raise ValueError("Can't create combinations with 0-length lists")
    n_items = len(lengths)

    curr = [0] * n_items
    combs = [list.copy(curr)]
    i = n_items - 1
    count = 1
    while count < n:
        curr[i] = (curr[i] + 1) % lengths[i]
        if curr[i] != 0:
            combs.append(list.copy(curr))
            count += 1
            i = n_items - 1  # reset to right-most digit
        else:
            i -= 1  # try previous (left) digit

    return combs


def get_combs(options: List[List[str]], splitter='', n=None) -> List[str]:
    """
    Given a list of options, returns up to n combinations
    e.g.: [['a'], ['1' ,'2'], ['@']] -> [a1@, a2@]
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


def main():
    lengths = [1, 2, 1]
    print(_get_comb_indexes(lengths))
    print(get_combs([['a', 'b'], ['1', '2'], ['@', '#']]))


if __name__ == '__main__':
    main()
