""" Zhenhao Zhang hw11"""


import random
import time
import matplotlib.pyplot as plt


### given code ####
# SELECTION SORT (INSERTION SORT)
def selectionSort(lst):
    for mark in range(len(lst) - 1):
        idx = mark
        while idx > -1 and lst[idx] > lst[idx + 1]:
            # swap elements at idx and idx +1
            lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
            idx = idx - 1


# MERGE SORT
def split(lst):
    evens = []
    odds = []
    isEven = True
    for e in lst:
        if isEven:
            evens.append(e)
        else:
            odds.append(e)
        isEven = not isEven  # flips True and False
    return (evens, odds)


def merge(sorted1, sorted2):
    result = []
    index1 = 0
    index2 = 0
    while index1 < len(sorted1) and index2 < len(sorted2):
        if sorted1[index1] <= sorted2[index2]:
            result.append(sorted1[index1])
            index1 = index1 + 1
        else:
            result.append(sorted2[index2])
            index2 = index2 + 1
    if index1 < len(sorted1):
        result.extend(sorted1[index1:])
    elif index2 < len(sorted2):
        result.extend(sorted2[index2:])
    return result


def mSort(lst):
    if lst == []:
        return []
    elif len(lst) == 1:
        return lst
    else:
        (half1, half2) = split(lst)
        return merge(mSort(half1), mSort(half2))


# QUICK SORT
def partition(pivot, lst):
    (less, same, more) = ([], [], [])
    for e in lst:
        if e < pivot:
            less.append(e)
        elif e > pivot:
            more.append(e)
        else:
            same.append(e)
    return (less, same, more)


def quickSort(lst):
    if lst == []:
        return []
    elif len(lst) == 1:
        return lst
    else:
        pivot = lst[0]
        (less, same, more) = partition(pivot, lst)
        return quickSort(less) + same + quickSort(more)

### given code ####


# Measure and record the running time of each sorting algorithm for each list size.
# Use the time module in Python for this purpose (import time).
def measure_sorting_time(initial_sorting_function, Ram_lst):
    Sort_times = []
    for i, j in Ram_lst.items():

        beginning_time = time.time()
        initial_sorting_function(j.copy())
        finishing_time = time.time()
        Sort_times.append(finishing_time - beginning_time)

    return Sort_times




def main():
    Random_list = {}
    input_conditions = [10, 100, 1000, 5000, 8000]


    # 生成随机数
    for i in input_conditions:
        random_numbers = []

        for j in range(i):

            random_numbers.append(random.randint(1, 1000))

        Random_list[i] = random_numbers

    Selection_sort_times = measure_sorting_time(selectionSort, Random_list)
    Merge_sort_times = measure_sorting_time(mSort, Random_list)
    Quick_sort_times = measure_sorting_time(quickSort, Random_list)

    # Sample data
    #      x = [1, 2, 3, 4, 5]
    #      y = [2, 4, 6, 8, 10]
    #      z = [3, 5, 7, 9, 11]
    #      # Create a simple line plot
    #      plt.plot(x, y,  label=’y’)
    #      plt.plot(x, z,  label=’z’)
    #      # Add labels to the plot
    #      plt.xlabel(’X-axis’)
    #      plt.ylabel(’Y-axis’)
    #      # Add legend to the plot
    #      plt.legend()
    #      # Add a title to the plot
    #      plt.title(’Simple Plot in Python’)
    #      # Display the plot
    #      plt.show()

    plt.plot(input_conditions, Selection_sort_times, label='Selection Sort')
    plt.plot(input_conditions, Merge_sort_times, label='Merge Sort')
    plt.plot(input_conditions, Quick_sort_times, label='Quick Sort')


    plt.ylim(-0.05, 1.0)

    plt.xlabel("List Size")
    plt.ylabel("Running Time (seconds)")
    plt.legend()
    plt.title("Running Time of Sorting Algorithms")
    # plt.savefig("Sorting Time of Sorting Algorithms.png")
    plt.show()





if __name__ == "__main__":
    main()

































