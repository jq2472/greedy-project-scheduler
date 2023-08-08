""" Jolin Qiu """

from dataclasses import dataclass
from pprint import pprint


@dataclass
class Project:
    """
    project_name: (str) name of the project
    length: (int) the time / weeks the project takes to complete
    revenue: (int) the amount of revenue gained from the project
    """
    project_name: str
    length: int
    revenue: int


def get_list(data):
    """ makes a list of orderable data, 'projects' (list)
    """
    projects = []
    with open(data) as f:
        next(f)
        for line in f:
            info = line.strip()
            project_name, length, revenue = info.split()
            # make project object
            projects.append(Project(project_name, int(length), int(revenue)))
    return projects


def insertion_sort(data):
    """ returns data: (list) project objects, in ascending order
    """
    for index in range(1, len(data)):
        # get value from list
        value = data[index]
        j = index
        # scan to left , shift all items > value up by one spot
        # stop at the 'edge' or when value >= data[j−1]
        while j > 0 and int(value.revenue/value.length) > data[j-1].revenue/data[j-1].length:
            data[j] = data[j-1]
            j = j - 1
            # insert value in slot j opened up by the while loop
            data[j] = value
    return data


def most_revenue(data, deadline):
    """ creates a list of the projects that would produce the most
    total revenue
    :param data: the list of project objects, already sorted.
    :param deadline: time period to complete the project """
    length = 0
    revenue = 0
    projects = []
    for i in data:
        if length + i.length <= deadline:
            projects.append(i.project_name)
            revenue += i.revenue
            length += i.length
    return projects, revenue, length


def sub_optimal():
    """ sub-optimal / non-optimal case in which the revenue-per-week
    criterion does not generate the most revenue per week for the given
    schedule:
    * data = projects.txt
    * deadline = 10

    DeathSpiral 5 20 => $4/wk
    TTP 4 16 => $4/wk
    Sparkle 2 8 => $4/wk
    Caribou 2 8 => $4/wk
    Beans 2 8 => $/wk
    Slay 2 8 => $4/wk
    Finale 2 8 => $/wk

    With the deadline being 10, the "optimal" revenue/week here would only cap at
    $36, AKA however the project schedule was initially formatted--due to the fact
    that 5 weeks + 4 weeks < 10 weeks, but + 2 weeks, would be > than 10 weeks. The
    loss of a week, when taking in the same amt. of revenue/week is all the more
    detrimental.
    Thus, the "lesser" revenue / week could occur more frequently, and
    would allow to MAX revenue to cap at 8 * 5 = $40. And $40 > $36.
    """


def main():
    """ prompts for file containing project information,
    prompts for deadline in weeks, and neatly prints the project
    data in selected order, order by revenue-per-week, scheduled projects,
    total revenue, and available weeks left.
    """
    data = input("Enter the project filename: ")
    deadline = int(input("Enter the length of the period (weeks): "))
    data = get_list(data)  # read file and get data

    # initial projects
    print("\ninitial projects:")
    for stat in data:
        print(stat.project_name, stat.length, stat.revenue)

    # projects organized by rev/week
    print("\nprojects organized by rev/week:")
    data = insertion_sort(data)  # sort data by rev/week
    for stat in data:
        print(stat.project_name, stat.length, stat.revenue)

    # scheduled only
    print("\nschedule:")
    projects, revenue, length = most_revenue(data, deadline)
    for i in range(len(projects)):
        pprint(projects[i])  # projects that fit the deadline w the most revenue

    # total revenue
    print("\n"+f"Total revenue: ${revenue}")

    # unscheduled weeks
    unused = deadline - length
    print("\nUnscheduled weeks: " + str(unused))


main()
