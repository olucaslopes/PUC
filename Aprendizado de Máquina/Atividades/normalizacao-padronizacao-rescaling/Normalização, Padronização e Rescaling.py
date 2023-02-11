# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 23:34:38 2022

@author: lucas
"""
#######################################################
## Suport functions
def mean(lst):
    """
    Returns the mean of an iterable of numerical values.
    """
    return sum(lst)/len(lst)

def stdev(lst):
    """
    Returns the standard deviation of an iterable of numerical values
    """
    m = mean(lst)
    variance = sum([(e-m)**2 for e in lst])/(len(lst)-1)
    return variance**0.5
#######################################################
# Normalização
def normalize(lst):
    """
    Takes an iterable of numerical values as
    input and returns a list of these values
    rescaled between 0 and 1 preserving the
    proportion of their differences.
    """
    return [(e-min(lst))/(max(lst)-min(lst)) for e in lst]

# Padronização
def standardize(lst):
    """
    Takes an iterable of numerical values as
    input and returns a list of these values
    standardized between 0 and 1 preserving the
    proportion of their differences.
    """
    m = mean(lst)
    std = stdev(lst)
    return [(e-m)/std for e in lst]

# Rescaling
def rescale(lst, a, b):
    """
    Takes an iterable of numerical values as
    input and two numbers, a and b 
    
    Returns a list of numerical values rescaled
    between a(lowest bound) and b(highest bound)
    preserving the proportion of their differences.

    """
    # Calculate right part of the equation
    div = [((e-min(lst))*(b-a))/(max(lst)-min(lst)) for e in lst]
    return [a+e for e in div]