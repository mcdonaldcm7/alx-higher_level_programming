#!/usr/bin/python3
"""
Definition for a function that finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """Finds and returns a peak in a list of unsorted integers"""
    if not list_of_integers:
        return (None)
    mid = int(len(list_of_integers) / 2);
    peak = list_of_integers[mid]
    if (mid > 1 and list_of_integers[mid -1] > peak):
        peak = list_of_integers[mid - 1]
    if ((mid + 1) < len(list_of_integers) and
        list_of_integers[mid + 1] > peak):
        peak = list_of_integers[mid + 1]
    return (peak)
