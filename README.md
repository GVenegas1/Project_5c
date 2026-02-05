# project-5c

This may look intimidating at first glance, but just follow the steps and you'll be fine :)

For this project, you will import the **time** and **random** modules.  You will also install the **matplotlib** package and import from it the **pyplot** module.

* Copy the code for bubble sort from the exploration and modify it to time how long it takes to sort the list. To get the current time, call time.perf_counter(). Do this at the beginning and end of the function, then subtract the begin time from the end time to get the elapsed time in seconds, and then return that time as the return value of the function. Name the function **bubble_time**.
* Do the same thing with insertion sort and name the function **insertion_time**.

* Write a function called **sort_times_for_random_list** that takes one parameter: the length of list to randomly generate and then sort (using both sorting algorithms). It should return a tuple of two times - how long it took bubble sort and how long it took insertion sort. 
  * First it should randomly generate a list of n numbers, where n is the value of the parameter
  * The random numbers should all be integers in the range 1 <= r <= n
  * For example, if the parameter is 1000, then the list should contain 1000 random integers, where each integer is >= 1 and <= 1000.
  * To generate the random numbers, you will use random.randint(a, b), which returns a random integer N such that a <= N <= b.  It's fine for values to appear in the list multiple times
  * Then the function should make a separate copy of your list of random numbers, which you can do like this: list_2 = list(list_1). Making a separate copy of the list is necessary because if you call one sort function on the list to record how long it takes, the list will now be sorted, which would affect how long the other sort function takes
  * Next the function should call bubble_time() to sort one copy of the list and call insertion_time to sort the other copy of the list. Lastly, it should return the two returned times as a tuple (first the time for bubble sort and then the time for insertion sort)

* Write a function called **compare_sorts** that takes no parameters and generates a graph comparing the times for bubble sort on different length lists versus the times for insertion sort on those same lists
  * First it will need to create a list of times for bubble sort and a list of times for insertion sort. To get those times, it will call sort_times_for_random_list() with each of the following list lengths: 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, and 10000.
  * HINT: because sorting all those lists can take a while, you might want to start with smaller list lengths for your initial debugging, like 100, 200, 300, 400, 500
  * Below is an example of code to produce a graph comparing two series of data points - **you will need to modify it to graph your timing data**

```
  from matplotlib import pyplot
  pyplot.plot([1, 2, 3, 4, 10], [1, 4, 9, 16, 100], 'ro--', linewidth=2, label='series 1')
  pyplot.plot([1, 2, 3, 4, 10], [1, 3, 7, 20, 150], 'go--', linewidth=2, label='series 2')
  pyplot.xlabel("the x label")
  pyplot.ylabel("the y label")
  pyplot.legend(loc='upper left')
  pyplot.show()
```
* Breakdown of graph example:
  * Each of the calls to the plot function plots a line
  * The call to the show function displays the graph
  * In the calls to the plot function, the first list is the list of x-coordinates (the lengths, which are the same for both curves you're plotting).  The second list is the list of y-coordinates (the list of times for a particular algorithm)
  * The 'ro--' tells it to use red circles connected by a dashed line and 'go--' is the same except green instead of red
  * The linewidth parameter is self-explanatory
  * The label parameter assigns the label to be used for that line in the legend. The legend() function sets where on the graph the legend should be displayed
  * The xlabel() and ylabel() functions set the labels for the x- and y-axes. For your graph, the x-axis is the length of list being sorted, and the y-axis is the time in seconds
  * **Your graph must include a legend and labels for the axes.**

* You'll still submit this project in Gradescope, but there won't be any automatic tests. Since the TAs will need to run your code to check the graph, please include a **main() function** that calls your compare_sorts() function to generate the graph.

Your graph should look similar to this:

![sort graph example](sort_graph_example.png)

Note: Keep in mind that the time it takes an algorithm to sort a list depends on the list. If you wanted your graph to be more robust, you would generate, say, 100 different random lists of each length and average their sort times together to get each data point.  However, that would take significantly longer to run, and therefore for the TAs to grade, so for this assignment, stick to one list of each size.

Your file must be named: **sort_timer.py**
