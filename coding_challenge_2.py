#!/usr/bin/python

import csv

# This method finds the corporate bonds field and calls functions to look for bounds.
def process(data):
    for row in data:
        bond_type = row['bond']
        corporate_yield = get_yield(row['yield'])
        corporate_term = get_term(row['term'])
        # Removes the numerals from the bond value
        result = ''.join([i for i in bond_type if not i.isdigit()])
        if result == 'C':
            up_bound, up_bound_value = upper_bound(row, data)
            low_bound, low_bound_value = lower_bound(row, data)
            # Calculate spread_to_curve
            result = corporate_yield - spread_calculator(up_bound, up_bound_value, low_bound,
                                                         low_bound_value,
                                                         corporate_term)
            print(bond_type + ', ' + str("%.2f" % round(result, 2)))


# gets the float value of term
def get_term(string):
    return float(''.join([i for i in string if not i.isalpha()]))


# gets the float value of yield
def get_yield(string):
    return float(string.replace("%", ""))


# This method is for counting the lowest upper government bound of a given corporate bound.
def upper_bound(corp_row, data):
    up_bound = 0.0
    up_bound_value = 0.0
    corp_term = get_term(corp_row['term'])
    diff = corp_term
    for row in data:
        govt_term = get_term(row['term'])
        govt_bond_type = row['bond']
        # Removes the numerals from the bond string
        result = ''.join([i for i in govt_bond_type if not i.isdigit()])
        if result == 'G':
            # Look for smallest upper_bound
            if govt_term > corp_term:
                num = govt_term - corp_term
                if num < diff:
                    diff = num
                    up_bound = govt_term
                    up_bound_value = get_yield(row['yield'])

    return up_bound, up_bound_value


# This method is for counting the highest lower government bound of a given corporate bound.
def lower_bound(corp_row, data):
    low_bound = 0.0
    low_bound_value = 0.0
    corp_term = get_term(corp_row['term'])
    diff = corp_term
    for row in data:
        govt_term = get_term(row['term'])
        govt_bond_type = row['bond']
        # removes the numerals from the bond string
        result = ''.join([i for i in govt_bond_type if not i.isdigit()])
        if result == 'G':
            # Look for biggest lower bound
            if corp_term > govt_term:
                num = corp_term - govt_term
                if num < diff:
                    diff = num
                    low_bound = govt_term
                    low_bound_value = get_yield(row['yield'])

    return low_bound, low_bound_value


# This method is for calculating the linear interpolation
def spread_calculator(upper_bound, upper_bound_value, lower_bound, lower_bound_value, x):
    y = ((upper_bound - x) * lower_bound_value) + ((x - lower_bound) * upper_bound_value)
    result = y / (upper_bound - lower_bound)
    return result


"""
calculate the spread to the government bond curve. 
Since the corporate bond term is not same as its benchmark term, 
we use linear interpolation to determine the spread to the curve.
"""
if __name__ == '__main__':
    # csv file name
    filename = input("Enter the name of the csv file: ")
    with open(filename) as file:
        reader = csv.DictReader(file)
        data = list(reader)
        print('bond,spread_to_curve')
        process(data)
