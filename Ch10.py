# Chapter 10: Working with Data

from collections import Counter
import random
from Ch4 import *
from Ch5 import *
from Ch6 import *
from Ch7 import *
import math
import matplotlib.pyplot as plt

isMain = __name__ == "__main__"

# One Dimensional Exploratory Analysis

def toFName(title):
    return title.replace(" ", "") + ".pdf"

def bucketize(point, bucket_size):
    """floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
    """buckets the points and counts how many in each bucket"""
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points, bucket_size, title=""):
    plt.figure()
    hist = make_histogram(points, bucket_size)
    plt.bar(hist.keys(), hist.values(), width=bucket_size)
    plt.title(title)
    plt.show()


if isMain:
    random.seed(0)

    # Uniform between -100 and 100
    uniform = [200 * random.random() - 100 for _ in range(10000)]

    # normal distribution with mean 0, std 57
    normal = [57 * Ch6.inverse_normal_cdf(random.random())
              for _ in range(10000)]

    # Plot both histograms
    plot_histogram(uniform, 10, "Uniform Histogram")
    plot_histogram(normal, 10, "Normal Histogram")


# TWO Dimensions

# lets makes some random normal 2D data

def random_normal():
    """returns a random draw from a standard normal dist"""
    return Ch6.inverse_normal_cdf(random.random())


if isMain:
    xs = [random_normal() for _ in range(1000)]
    ys1 = [ x + random_normal() / 2 for x in xs]
    ys2 = [-x + random_normal() / 2 for x in xs]
    
    # ys1 and ys2 would have a very similar histogram, but they have a
    # very joint distribution with xs
    plt.figure()
    plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
    plt.scatter(xs, ys2, marker='.', color='blue', label='ys2')
    plt.xlabel('xs')
    plt.ylabel('ys')
    plt.legend(loc=9)
    title = "Very Different Joint Distributions"
    plt.title(title)
    plt.show()

    print(Ch5.correlation(xs, ys1))
    print(Ch5.correlation(xs, ys2))


## Many Dimensions 

# With more than 2D, visualization is difficult
# We can switch to correlation matrices instead

def correlation_matrix(data):
    """
        returns the num_columns x num_columns matrix whose (i, j)th entry is
        is the correlation between columns i and j of the input data
    """
    _, num_columns = shape(data)
    
    def matrix_entry(i, j):
        return Ch5.correlation(Ch4.get_col(data, i), correlation(Ch4.get_col(data, j)))
    
    return make_matrix(num_columns, num_columns, matrix_entry)