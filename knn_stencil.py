import math

'''
knn.py

Stencil Code for AI & Society.

Template borrowed from:
    https://tinyurl.com/yb5z6cvc
'''

import random
import math
import operator


def load_dataset(filename, split):
    '''
    Args:
        filename (str) = Path to the file.
        split (float) = Probability of adding an item to train.
        
    Returns:
        training_data (list)
        test_data (list)
    '''
    # Make data lists.
    training_data = []
    test_data = []

    # Loop through each row of the dataset.
    with open(filename, 'rb') as csvfile:
        all_lines = csvfile.readlines()
        for line in all_lines:
            data_point = [float(x) for x in line.split(",")[:4]]
            data_point.append(line.split(",")[-1].replace("\n", ""))

            # Add to the train or test.
            if random.random() < split:
                training_data.append(data_point)
            else:
                test_data.append(data_point)

    return training_data, test_data


def get_k_n_neighbors(test_vector, training_data, k=7):
    '''
    Args:
        vector (list)
        training_data (list)
        k (int)

    Returns:
        (list): Contains the k nearest neighbors to the given vector.
    '''
    total = []
    labels = []
    dist_list = []

    for i in range(len(training_data)):
        total.append(euclidean_distance(test_vector, training_data[i][:-1]))
        labels.append(training_data[i][-1])

    for a in range(len(total)):
        dist_list.append([labels, total[a]])

    # print(dist_list)

    return find_k_min(dist_list, k)

    # List:
    # dist_list = [label, distance]
    # return find_k_min(dist_list, k)


def find_k_min(train_data_w_distance, k):
    '''
    Args:
        train_data_w_distance (list)

    Returns:
        (list): Closest neighbors.
    '''
    train_data_w_distance.sort(key=operator.itemgetter(1))
    neighbors = []
    for i in range(k):
        neighbors.append(train_data_w_distance[i][0])

    return neighbors


def euclidean_distance(vector_one, vector_two):
    '''
    Args:
        vector_one (list)
        vector_two (list)

    Returns:
        (float)
    '''
    totalDistance = float(0)

    for i in range(len(vector_one)):
        totalDistance = totalDistance + (vector_one[i] - vector_two[i]) ** 2

    return totalDistance ** (0.5)


def classify(item, k_neighbors):
    '''
    Args:
        item (list)
        k_neighbors (list)

    Returns:
        (str): The flower type.
    '''
    k_labels = [item[-1] for item in k_neighbors]
    result = max(k_labels, key=k_labels.count)

    return result


def main():
    # Build data sets.
    training_data, test_data = load_dataset('flowers.csv', 0.66)
    print 'Train: ', len(training_data)
    print 'Test: ', len(test_data)

    # Loop over data and classify using K-NN.

    for item in test_data:
        neighbs = get_k_n_neighbors(item[:-1], training_data, k=7)
        result = classify(item[:-1], neighbs)

        print result, item[-1]
        ########################
        #### YOUR CODE HERE ####
        ########################

        # Print classifier accuracy on the test data.


if __name__ == "__main__":
    main()
