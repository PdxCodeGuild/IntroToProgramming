#!/usr/bin/env python
import random
import time


def merge_sort(l):
    # put sorted elements into results
    results = []

    # if we only have one element to sort,
    # it is already sorted
    if len(l) < 2:
        return l

    # find the middle of the list
    mid = int(len(l) / 2)

    # sort all elements preceeding the index of mid
    left = merge_sort(l[:mid])

    # sort all element proceeding from the index of mid
    right = merge_sort(l[mid:])

    # create counters to act as list indices
    i = 0
    j = 0

    # until both sub lists are sorted we will loop
    while i < len(left) and j < len(right):

        # main comparison logic to compare elements
        #
        # is the element from the left set bigger than
        # the element from the right?
        # if yes, then the right element is smaller and
        # in our sorting should preceed the left element
        if left[i] > right[j]:
            results.append(right[j])

            # increment our counter
            j += 1

        # if no, then the left element is smalle and
        # in our sorting, should preceed the right element
        else:
            results.append(left[i])

            # increment our counter
            i += 1
    
    # put the remaining sorted sub lists into results
    results += left[i:]
    results += right[j:]

    return results


def populate(num):
    # a list to store our random numbers
    l = []
    
    # range(num) creates a list from 0 to num
    # e.g. range(4) == [0,1,2,3]
    # 
    # loop through range(num) and on each iteration
    # put a random integer between 0 and num
    for i in range(num):
        l.append(random.randint(0, num))

    return l


def main():
    print('--- populating list ---')
    time.sleep(2)

    sort_this = populate()

    print(sort_this)
    proceed = raw_input('ready? ')
    if not proceed:
        exit(0)

    print('--- sorting ---')
    time.sleep(2)

    merge_sorted_list = merge_sort(sort_this)

    print('--- done sorting ---')
    time.sleep(2)
    print(merge_sorted_list)


if __name__ == '__main__':
    main()
