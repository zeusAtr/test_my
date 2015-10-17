__author__ = 'Vlad'

def min_value(a):
    sorted_list = sorted(map(int,(filter(lambda x: str(x).isdigit(),a))))

    return sorted_list[:2]

print min_value([1,2,43,0,3,2,0.5,3,6,7663, "a", 123])