import math
#small data set
data = [3, 13, 19, 24,29]

def mean(dataset):
    return sum(x for x in dataset)/ len(dataset)

def mod(dataset):
    return max(set(dataset), key=dataset.count)

def median(dataset):
    dataset = sorted(dataset)
    n = len(dataset)

    if n % 2 == 0:
        return (dataset[n // 2 - 1] + dataset[n // 2]) / 2
    else:
        return dataset[n // 2]

def standerd_deviation(dataset):
    avg = mean(dataset)
    return math.sqrt(sum((x-avg)**2 for x in data)/len(dataset)-1)


varience = standerd_deviation(data)**2
print(varience)
print(median(data))
