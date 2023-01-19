# 6. Python Program for Number of elements with odd factors in a given range

# Only those numbers, which are perfect Squares have an odd number of factors

start,end = map(int,input('Enter start and end numbers space separated: ').split())

num_of_elements = int(end ** 0.5) - int((start) ** 0.5)
# start-1 is taken as both are included but if start is perfect square it may give 1 less number
print('Number of elements with odd factors is: ',(num_of_elements))

# 4 100
# Number of elements with odd factors is:  8