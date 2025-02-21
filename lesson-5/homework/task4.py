universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(univers):
    return [i[1][1] for i in enumerate(univers)], [i[1][2] for i in enumerate(univers)]

def mean(values):
    s = sum(values)
    return s / len(values)

def median(values):
    sort = sorted(values)
    size = len(values)
    if size % 2 == 0:
        return (sort[size/2 - 1] + sort[size/2])/2
    else:
        return sort[int((size - 1)/2)]

e = enrollment_stats(universities)
print("*"*30)
print(f"Total students: {sum(e[0])}")
print(f"Total tuition: $ {sum(e[1])}\n")  

print(f"Student mean: {round(mean(e[0]), 2)}")
print(f"Student median: {median(e[0])}\n")

print(f"Tuition mean: $ {round(mean(e[1]), 2)}")
print(f"Tuition median: $ {median(e[1])}")
print("*"*30)
    