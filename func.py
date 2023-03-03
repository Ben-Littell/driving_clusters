import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as stats


def guess_centroid(list1, list2):
    plt.scatter(list1, list2)
    plt.show()
    guess = input('Input Centroid Locations: ')
    guess = eval(guess)  # if written as coordinate points gives tuple or tuple of tuples
    # print(type(guess[0][1]))
    return guess


def distance(l1, l2, centroids=None):
    if centroids is None:
        centroids = guess_centroid(l1, l2)
    # creates dictionary
    new_dict = {}
    for val in centroids:
        new_dict[val] = []
    # print(new_dict)
    # assign to centroids
    for i in range(len(l1)):
        dist_l = []
        for c in centroids:
            dist_l.append(((c[0]-l1[i])**2) + ((c[1]-l2[i])**2))
        new_dict[centroids[dist_l.index(min(dist_l))]].append(i)
    # to make fully recursive try making a plot function then call that in a loop with a plt.show() at the end
    # have the function be looped through depending on the number of centroids
    for v in centroids:
        x = [l1[k] for k in new_dict[v]]
        y = [l2[k] for k in new_dict[v]]
        plt.scatter(x, y)
        plt.plot([v[0]], [v[1]], 'k', marker='D')
    # print(len(c1)+len(c2))
    # plt.scatter(c1x, c1y)
    # plt.scatter(c2x, c2y)
    plt.show()
    return new_dict


def new_centroid(l1, l2, dict):
    c = []
    for v in dict:
        cx = stats.mean([l1[k] for k in dict[v]])
        cy = stats.mean([l2[k] for k in dict[v]])
        c.append((cx, cy))
    return c


def main(l1, l2, centroids=None, rep=4):
    for n in range(rep):
        d1 = distance(l1, l2, centroids)
        centroids = new_centroid(l1, l2, d1)
    # print(centroids)
    # d2 = distance(l1, l2, centroids)
    # centroids = new_centroid(l1, l2, d2)
    # d3 = distance(l1, l2, centroids)
    # centroids = new_centroid(l1, l2, d3)
    # d4 = distance(l1, l2, centroids)



