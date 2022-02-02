# -*- coding: utf-8 -*-

"""
Sorting functions module for experience assignment

Note: Author
      [Dpt Informatique - FST - Univ. Lille](http://portail.fil.univ-lille1.fr)
      2018, january
"""

import copy

def merge (t1,t2, cmp):
    """
    Given two sorted lists, creates a fresh sorted list.

    Args:
      t1 (list): A list of objects
      t2 (list): A list of objects
      cmp (function): A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b

    Note: Complexity
          Time complexity of merge is $O(n_1+n_2)$ with
          $n_1$ and $n_2$ resp. the length of `t1` and `t2`

    
    Returns:
      list: A fresh list, sorted.
    
    Examples:
      >>> def cmp (x,y): 
      ...    if x == y:
      ...       return 0
      ...    elif x < y:
      ...       return -1
      ...    else:
      ...       return 1
      >>> t1 = [0,2,5,6]
      >>> t2 = [1,3,4]
      >>> merge(t1,t2,cmp)
      [0, 1, 2, 3, 4, 5, 6]
    """
    n1 = len(t1)
    n2 = len(t2)
    t = [0 for i in range(n1+n2)]
    i = j = k = 0
    while i < n1 and j < n2:
        if cmp(t1[i],t2[j]) < 0:
            t[k] = t1[i]
            i = i + 1
        else:
            t[k] = t2[j]
            j = j + 1
        k = k + 1
    while i < n1:
        t[k] = t1[i]
        i = i + 1
        k = k + 1
    while j < n2:
        t[k] = t2[j]
        j = j + 1
        k = k + 1
    return t

def merge_sort (t,cmp):
    """
    A sorting function implementing the merge sort algorithm.
    
    Args:
      t (list): A list of integers
      cmp (function): A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b

    Note: Complexity
          Time complexity of merge sort is $\Theta(n\log n)$ with
          $n$ the length of `t`.

    Returns:
      list: A fresh list, sorted.

    Examples:
      >>> import marker
      >>> def cmp (x,y): 
      ...    return x.cmp(y)
      >>> t = marker.Marker.markers(10)
      >>> merge_sort(t,cmp)
      [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9]

    """
    n = len(t)
    if n <= 1:
        # cas de base
        return copy.deepcopy(t)
    else:
        # cas general
        t1 = merge_sort((t[0:((n-1)//2+1)]),cmp)
        t2 = merge_sort((t[((n-1)//2+1):n]),cmp)
        return merge(t1,t2,cmp)
    
if __name__ == "__main__":
    import doctest
    test_results = doctest.testmod()
    import marker
    import test
    t = marker.Marker.markers(100)
    print(t)
    print(merge_sort(t,test.compare))
    exit(test_results[0])
