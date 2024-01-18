import random
from collections import Counter

from itertools import permutations
from time import time

import matplotlib.pyplot as plt


a_city = complex


def distance_tour(a_tour):
    return sum(distance_points(a_tour[i - 1], a_tour[i]) for i in range(len(a_tour)))


def distance_points(first, second):
    return abs(first - second)


def generate_cities(number_of_cities):
    seed = 111
    width = 500
    height = 300
    # random.seed((number_of_cities, seed))
    return frozenset(a_city(random.randint(1, width), random.randint(1, height)) for c in range(number_of_cities))


def brute_force(cities):
    return shortest_tour(permutations(cities))


def shortest_tour(tours):
    return min(tours, key=distance_tour)


# Visualization

def visualize_tour(tour, style = 'bo-'):
    if len(tour) > 1000:
        plt.figure(figsize=(15, 10))
    start = tour[0:1]
    visualize_segment(tour + start, style)
    visualize_segment(start, 'rD')


def visualize_segment(segment, style='bo-'):
    plt.plot([X(c) for c in segment], [Y(c) for c in segment], style, clip_on=False)
    plt.axis('scaled')
    plt.axis('off')
    plt.show()


def X(city):
    return city.real


def Y(city):
    return city.imag


# TSP (Traveling Sales Person) function

def tsp(algorithm, cities):
    print('processing...')
    t0 = time()
    tour = algorithm(cities)
    t1 = time()

    # Every city appears exactly once in tour
    assert Counter(tour) == Counter(cities)
    visualize_tour(tour)
    print("{}: {} cities => tour length {:.0f} (in {:.3f} sec)".format(name(algorithm), len(tour), distance_tour(tour), t1 - t0))


def name(algorithm):
    print(f'name ----> {algorithm.__name__}')
    return algorithm.__name__.replace('_tsp', '')


# Greedy Algorithm for TSP

def greedy_algorithm(cities, start = None):
    city = start or first(cities)
    tour = [city]
    unvisited = set(cities - {city})
    while unvisited:
        city = nearest_neighbor(city, unvisited)
        tour.append(city)
        unvisited.remove(city)
    return tour


def first(collection):
    return next(iter(collection))


def nearest_neighbor(city_a, cities):
    return min(cities, key=lambda city: distance_points(city, city_a))


if __name__ == '__main__':
    # tsp(brute_force, generate_cities(10))

    # Now, let's use greedy_algorithm to create a tour for 2,000 cities
    tsp(greedy_algorithm, generate_cities(2000))
