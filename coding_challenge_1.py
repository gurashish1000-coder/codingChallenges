#!/usr/bin/python
import csv


# Finds the first corporate bond and calls the calculate_yield_spread to find the closest govt bond.
def process(data):
    # Making a copy.
    for row in data:
        bond_type = row['bond']
        result = ''.join([i for i in bond_type if not i.isdigit()])
        if result == 'C':
            calculate_yield_spread(row, data)


# Calculates the spread to benchmark by finding the closest benchmark bond for each
# corporate bond and then subtracting govt bond yield from corp bond yield.
def calculate_yield_spread(corp_row, data):
    spread_to_benchmark = 0.0
    corp_term = get_term(corp_row['term'])
    diff_term = corp_term
    corp_yield = get_yield(corp_row['yield'])
    bond = corp_row["bond"]
    for row in data:
        benchmark = row['bond']
        result = ''.join([i for i in benchmark if not i.isdigit()])
        govt_term = get_term(row['term'])
        govt_yield = get_yield(row['yield'])
        if result == 'G':
            # Finding the closest possible govt bond for corporate bond
            new = abs(govt_term - corp_term)
            if new < diff_term:
                diff_term = new
                benchmark_type = row['bond']
                num = corp_yield - govt_yield
                spread_to_benchmark = str("%.2f" % round(num, 2)) + '%'
        else:
            continue
    print('{0}, {1}, {2}'.format(bond, benchmark_type, spread_to_benchmark))


# gets the float value of term
def get_term(string):
    return float(''.join([i for i in string if not i.isalpha()]))


# gets the float value of yield
def get_yield(string):
    return float(string.replace("%", ""))


"""
Given a list of corporate and government bonds, finds a benchmark bond for each corporate bond and 
calculates the spread to benchmark.
"""
if __name__ == '__main__':
    # csv file name
    filename = input("Enter the name of the csv file: ")
    with open(filename) as file:
        reader = csv.DictReader(file)
        data = list(reader)
        print('bond,benchmark,spread_to_benchmark')
        process(data)
