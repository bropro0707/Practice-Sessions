import math
#small data set
results = [85, 90, 78, 92, 88, 79, 84, 95]

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

def standard_deviation(dataset):
    avg = mean(dataset)
    return math.sqrt(sum((x-avg)**2 for x in results)/len(dataset)-1)


print(standard_deviation(results))

