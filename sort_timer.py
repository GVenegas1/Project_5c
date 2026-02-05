#Author: Gabriel Venegas
#Github username: Gvenegas1
#Date: February 4, 2026
#Description: This program compares Bubble Sort and Insertion Sort speeds.
# It uses random lists and plots the results on a graph.

import time
import random
from matplotlib import pyplot


def bubble_time(list_to_sort):
    """Times how long bubble sort takes to sort a list"""

    #Start the stopwatch
    start_time = time.perf_counter()

    list_length = len(list_to_sort)

    #Loop through the list to move larger numbers to the end
    for outer_index in range(list_length):
        for inner_index in range(0, list_length - outer_index - 1):

            #Swap numbers if they are in the wrong order
            if list_to_sort[inner_index] > list_to_sort[inner_index + 1]:
                temporary_value = list_to_sort[inner_index]
                list_to_sort[inner_index] = list_to_sort[inner_index + 1]
                list_to_sort[inner_index + 1] = temporary_value

    #Return how much time passed
    return time.perf_counter() - start_time


def insertion_time(list_to_sort):
    """Times how long insertion sort takes to sort a list"""

    #Start the stopwatch
    start_time = time.perf_counter()

    #Process the list from the second item to the end
    for current_index in range(1, len(list_to_sort)):
        value_to_sort = list_to_sort[current_index]
        position = current_index - 1

        #Shift items to the right to find the correct spot
        while position >= 0 and value_to_sort < list_to_sort[position]:
            list_to_sort[position + 1] = list_to_sort[position]
            position = position - 1

        list_to_sort[position + 1] = value_to_sort

    #Return how much time passed
    return time.perf_counter() - start_time


def sort_times_for_random_list(list_size):
    """Makes a random list and returns a tuple of both sort times."""

    #Fill a list with random numbers
    numbers_list = []
    for count in range(list_size):
        random_number = random.randint(1, list_size)
        numbers_list.append(random_number)

    #Make a real copy so both sorts start with the same messy data
    #This ensures the race is fair
    copy_for_insertion = list(numbers_list)

    #Run the timers for both sorting methods
    bubble_result = bubble_time(numbers_list)
    insertion_result = insertion_time(copy_for_insertion)

    #Return the times as a tuple (a fixed pair)
    return (bubble_result, insertion_result)


def compare_sorts():
    """Gets timing data for different sizes and draws the graph."""

    #List lengths, need to test (from 1000 to 10000)
    test_lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    #Big lists to store all our results for the graph
    bubble_data = []
    insertion_data = []

    print("Beginning the sort comparison. Please wait!")

    for size in test_lengths:
        #Catch the results into descriptive names
        bubble_result, insertion_result = sort_times_for_random_list(size)

        #Add the results to our data lists
        bubble_data.append(bubble_result)
        insertion_data.append(insertion_result)
        print("Done timing list size:",size)

    #The graph: 'ro' is red circles, 'go' is green circles
    pyplot.plot(test_lengths,bubble_data, 'ro--',linewidth=2, label='Bubble Sort')
    pyplot.plot(test_lengths, insertion_data, 'go--',linewidth=2, label='Insertion Sort')

    #Add axis labels, title, and the legend
    pyplot.xlabel("Length of List")
    pyplot.ylabel("Time in Seconds")
    pyplot.title("Bubble Sort vs. Insertion Sort Speed")
    pyplot.legend(loc='upper left')

    # Show the final graph
    pyplot.show()


def main():
    """Main function to start the program."""
    compare_sorts()

