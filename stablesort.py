#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import array


def stable_sort_by_column(arr, column_index, element_index=None):
    u"""
    stable matrix sorting using column key.
    input:
        arr: numpy 2D or (3D) array.
             If arr is 3D,
             we assume most inner array as stable element like tuple.
        column_index: column index of key of stable sort.
        element_index: If input arr is 3D,
                       sorting key is lambda element: element[element_index]
    """
    arr = array(arr)
    return array(sorted(arr, key=lambda x: x[column_index][element_index]))


def stable_sort_by_row(arr, row_index, element_index=None):
    u"""
    stable matrix sorting using row key.
    imput:
        arr: numpy 2D or (3D) array.
             If arr is 3D,
             we assume most inner array as stable element like tuple.
        row_index: row index of key of stable sort.
        element_index: If input arr is 3D,
                       sorting key is lambda element: element[element_index]
    """
    arr = array(arr)
    return array(sorted(arr.T, key=lambda x: x[row_index][element_index])).T

if __name__ == "__main__":
    a = array([[4, 1, 4, 2, 1, 3],
               [7, 3, 2, 0, 5, 0],
               [2, 3, 6, 0, 6, 7],
               [6, 4, 5, 7, 5, 1],
               [3, 1, 6, 6, 2, 4],
               [6, 0, 5, 5, 5, 1]])

    b = array([[("a", 1), ("b", 6), ("c", 5), ("p", 0), ("u", 0)],
              [("i", 3), ("d", 4), ("q", 2), ("e", 7), ("y", 9)],
              [("s", 2), ("x", 0), ("z", 5), ("b", 6), ("m", 8)],
              [("r", 6), ("g", 1), ("k", 2), ("f", 4), ("m", 0)],
              [("h", 0), ("n", 2), ("l", 8), ("e", 5), ("c", 3)]])

    print "input array"
    print a
    print ""

    print "stable sort by last column"
    print "stable_sort_by_column(a, -1)"
    print stable_sort_by_column(a, -1)
    print ""

    print "stable sort by last row"
    print "stable_sort_by_row(a, -1)"
    print stable_sort_by_row(a, -1)
    print "\n"

    print "input array (3D)"
    print """[[("a", 1), ("b", 6), ("c", 5), ("p", 0), ("u", 0)],
 [("i", 3), ("d", 4), ("q", 2), ("e", 7), ("y", 9)],
 [("s", 2), ("x", 0), ("z", 5), ("b", 6), ("m", 8)],
 [("r", 6), ("g", 1), ("k", 2), ("f", 4), ("m", 0)],
 [("h", 0), ("n", 2), ("l", 8), ("e", 5), ("c", 3)]]"""
    print ""

    print "3D array stable sort by last column"
    print "stable_sort_by_column(b, -1, key=lambda x: x[1])"
    print stable_sort_by_column(b, -1, element_index=1)
    print ""

    print "3D array stable sort by last row"
    print "stable_sort_by_row(b, -1, element_index=1)"
    print stable_sort_by_row(b, -1, element_index=1)
    print ""
