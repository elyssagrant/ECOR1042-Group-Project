# ECOR 1042 Lab 5 - Individual submission for sort_students_g_avg_insertion function

__author__ = "Elyssa Grant"

__team__ = "T-83"

#==========================================#
# Place your sort_students_g_avg_insertion function after this line


def sort_students_g_avg_insertion(dict_list: list[dict], asc_desc: str):
    """
    Given a list of dictionaries and a string saying whether they are to be sorted in ascending or descending order, sorts the dictionaries according to the G_Avg key value

    Preconditions: asc_desc is "A" or "D", dict_list contains at least one dictionary

    Examples:

    >>>sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}], "D")
    [{"G_Avg": 9.1, "School":"MS"}, {"G_Avg":7.2, "School":"GP"}]

    >>> sort_students_g_avg_insertion([{"School":"GP"},{"School":"MS"}], "D")
    "G_Avg" key is not present
    [{"School":"GP"},{"School":"MS"}]

    >>> sort_students_g_avg_insertion([{"School":"GP", 'G_Avg': 9.5},{"School":"MS", 'G_Avg': 5.5}, {"School":"MB", 'G_Avg': 6.7}], "A")
    [{"School":"MS", 'G_Avg': 5.5}, {"School":"MB", 'G_Avg': 6.7}, {"School":"GP", 'G_Avg': 9.5}]
    """

    # checking to ensure the list contains the value we're trying to sort by

    if "G_Avg" not in dict_list[0].keys():
        print('"G_Avg" key is not present')

        return dict_list

    else:

        # Doing the insertion sort in ascending order
        if asc_desc == "A":

            for i in range(1, len(dict_list)):

                key = dict_list[i]

                j = i - 1

                while j >= 0 and key['G_Avg'] < dict_list[j]['G_Avg']:

                    dict_list[j + 1] = dict_list[j]

                    j -= 1

                dict_list[j + 1] = key

        # insertion sort in descending order
        else:
            for i in range(1, len(dict_list)):

                key = dict_list[i]

                j = i - 1

                while j >= 0 and key['G_Avg'] > dict_list[j]['G_Avg']:

                    dict_list[j + 1] = dict_list[j]

                    j -= 1

                dict_list[j + 1] = key

    return dict_list


