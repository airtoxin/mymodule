#!/usr/bin/env python
# -*- coding: utf-8 -*-


def slide_window_iterator(iterable, windowsize):
    u"""
    slide_window_iterator("ABCDE", 3) --> ABC BCD CDE
    """
    pool = []
    for element in iterable:
        pool.append(element)
        if len(pool) == windowsize:
            yield tuple(pool)
        elif len(pool) > windowsize:
            pool = pool[1:]
            yield tuple(pool)
