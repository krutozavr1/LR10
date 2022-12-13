#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = {"b", "d", "f", "g", "l", "u"}
    b = {"d", "f", "e", "m", "n", "z"}
    c = {"h", "i", "r", "x", "y"}
    d = {"a", "e", "f", "k", "r", "s", "x"}

    x = (a.union(b)).intersection(c)
    y = (a.intersection(b)).union(c.difference((d)))

    print(x)
    print(y)
