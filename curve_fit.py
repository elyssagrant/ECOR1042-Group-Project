# ECOR 1042 Lab 6 - Individual submission for curve_fit function

__author__ = "Elyssa Grant"

__team__ = "T-83"

#==========================================#
# Place your curve_fit function after this line


def curve_fit(dict_list: list[dict], compare: str, poly: int) -> str:
    """
    Given a list of dictionaries, a value to sort by and a polynomial value, the function will do linear regression or interpolation to determine the line of best fit and return a string equation of best fit.

    Preconditions: All dictionaries contain G_Avg, all dictionaries have the same keys, the key to be compared with holds an integer or float value.

    Examples:

    >>>curve_fit([{"G_Avg": 4, "Health": 4}, {"G_Avg": 8, "Health": 3}, {"G_Avg": 6.7, "Health": 4}], "Health", 1)
    '-2.65 x + 15.95'

    >>>curve_fit([{"StudyTime": 1.0, "G_Avg": 3}, {"StudyTime": 2.0, "G_Avg": 5}, {"StudyTime": 3.0, "G_Avg": 8}, {"StudyTime": 4.0, "G_Avg": 9}], "StudyTime", 4)
    '-0.5x^3 + 3.5x^2 + -5x + 5'

    >>>curve_fit([{"G_Avg": 9.3, "StudyTime": 2.5, "Failures": 1}, {"G_Avg": 6.4, "StudyTime": 2.5, "Failures": 0}, {"G_Avg": 8.5, "StudyTime": 2, "Failures": 1}, {"G_Avg": 9.0, "StudyTime": 1.3, "Failures": 0}, {"G_Avg": 6.7, "StudyTime": 2.5, "Failures": 2}], "Failures", 2)
    '-1.7x^2 + 2.9x + 7.7'
    """
    import numpy as np

    # declaring variables
    attribute_list = []

    average_dict = {}

    minimum = dict_list[0][compare]

    maximum = dict_list[0][compare]

    # looping over the list and creating a list of tuples containing only the important data
    for i in range(len(dict_list)):
        attribute_list += [(dict_list[i][compare], dict_list[i]["G_Avg"])]

        # determining the minimum and maximum values the dictonaries have for the comparable data
        if dict_list[i][compare] < minimum:
            minimum = dict_list[i][compare]
        elif dict_list[i][compare] > maximum:
            maximum = dict_list[i][compare]

    # looping across the range of values the comparable value
    for value in range(int(minimum), int(maximum + 1)):

        # creating a new key in the dictionary of compare values
        average_dict[value] = 0

        # resetting the counter to zero
        counter = 0

        # looping across the list of tuples
        for i in range(len(attribute_list)):

            # checking each time if the compare value is the value we want to deal with right now
            if attribute_list[i][0] == value:

                # adding the G_Avg values
                average_dict[value] = (
                    average_dict[value] + attribute_list[i][1])

                # counting how many G_Avg values we have added together
                counter += 1

        # making sure there's no runtime error by dividing by zero
        if counter != 0:

            # finding the average G_Avg for the compared value
            average_dict[value] = average_dict[value] / counter
        else:
            # if there was no values of the comparable, removes the key from the dictionary
            average_dict.pop(value, None)

    # turning the dictionary keys into a useable list
    x = list(average_dict.keys())

    # turning the dictionary values into a useable list
    y = list(average_dict.values())

    return_string = ""

    # checking if use linear regression or interpolation
    if len(x) > poly:
        # linear regression
        coeffs = np.polyfit(x, y, poly)

        # creating return string to give back
        for l in range(poly - 1):
            return_string += str(coeffs[l]) + "x^" + str((poly - l)) + "+"

    else:
        # linear interpolation
        coeffs = np.polyfit(x, y, len(x) - 1)

        # creating return string
        for l in range(len(x) - 2):
            return_string += str(coeffs[l]) + \
                "x^" + str((len(x) - 1 - l)) + "+"

    # adding the constant onto the end of the string
    return_string += str(coeffs[-2]) + "x+" + str(coeffs[-1])

    return return_string

