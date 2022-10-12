import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import random
import time
from math import ceil
import timeit
import pickle
import ipywidgets as widgets
from lolviz import *


def find_in_list(object_list, book_name):
    """
    Find the book_name entry linearly in the object list tuples.
    Parameters:
        object_list: list[tup[str,str]]
        book_name: str
    Returns:
        Return value is the
        ('Book-Title','Book-Author') tuple from the object_list
    """
    book_name = book_name.lower()
    for entry in object_list:
        if book_name == entry[0]:
            return entry
    return (0, 0)


def empty_hashtable(buckets):
    """
    Function takes number of buckets and returns a list of buckets size empty list
    Parameters:
        buckets: int
    Returns:
        Return value is list of empty lists.
        ReturnValue: list[list[]]
    """
    lol = []
    for i in range(buckets):
        lol.append([])
    return lol


def hash_function(key):
    """
    Function takes a key value and returns a hash code value for that key.
    Parameters:
        key: str
    Returns:
        ReturnValue: int
        Return value is the hash code of the function
    """
    h = 0
    key = key.lower()
    for a in key:
        h = ((h * ord(a))) % 2147 + ord(a)
        # Dividing to stop the hash code from going excessively
        # and arbritrary large
        # Dividing by a prime to evenly space the hash code distributions
        # Interesting fact: 2147483647 is the 8th Mersenne Prime.
        # hash code is returned
    return h


def populate_hashtable(tups, required_ht):
    """
    Function takes a list of tuples (of two strings, books and authors),
    and buckets to populate a hashtable
    Parameters:
        list_of_tups: list[tup[str,str]]
        buckets: int
    ReturnValue:
        required_ht: list[list[str,str]]
    ReturnValue is the populated hashtable of list of lists
    """
    buckets=len(required_ht)
    book = tups[0]
    author = tups[1]
    hashcode_book = hash_function(book)
    bucket_book = hashcode_book % buckets
    required_ht[bucket_book].append(tups)
    return required_ht


def populate_hashtable_linear_probe(tups, required_ht):
    """
    Function takes a list of tuples (of two strings, books and authors),
    and buckets to populate a hashtable
    Parameters:
        list_of_tups: list[tup[str,str]]
        buckets: int
    ReturnValue:
        required_ht: list[list[str,str]]
    ReturnValue is the populated hashtable of list of lists
    """
    buckets=len(required_ht)
    book = tups[0]
    author = tups[1]
    hashcode_book = hash_function(book)
    bucket_book = hashcode_book % buckets
    if required_ht[bucket_book]==[]:
        required_ht[bucket_book].append(tups)
    else:
        idx=bucket_book+1
        tmp_tbl=required_ht[idx:]+required_ht[:idx]
        for next_free in range(len(required_ht)):
            if tmp_tbl[next_free]==[]:
                tmp_tbl[next_free].append(tups)
                required_ht=tmp_tbl[-(idx):]+tmp_tbl[:-(idx)]
                break
    return required_ht


def find_in_hashtable(given_ht, value_to_find):
    """
    Function takes the hashtable and value_to_find as paramter inputs
    to look for the value_to_find in the hash
    table, return the tuple if it finds it, else return (-1,-1)
    Parameters:
        given_ht: list[list[str,str]]
        value_to_find: str
    ReturnValue:
        entry: (str,str)
            : (-1,-1) if entry in hashtable is not found
    """
    hashcode_tofind = hash_function(value_to_find)
    buckets_ht = len(given_ht)
    bucket_tofind = hashcode_tofind % buckets_ht
    for entry in given_ht[bucket_tofind]:
        if entry[0] == value_to_find:
            return entry
    return (-1, -1)


def hash_plot(bin_size):
    """
    Plotting function used to display time
    complexity of hashtable using ipywidgets
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    x = list_size
    y = [hashtable_search_time[i][bin_size] for i in list_size]
    ax.plot(x, y)
    hash_title = 'Hashtable Search with {} bins'.format(bin_size)
    ax.set_title(hash_title)
    ax.set_ylim(0, max_time)
    ax.set_xlabel('Length of List')
    ax.set_ylabel('Run Time (μs)')
    plt.show()

    
def displayBuckets(buckets):
    """
    Display the entries in Buckets
    """
    return objviz(buckets)

