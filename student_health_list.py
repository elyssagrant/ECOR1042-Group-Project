# ECOR 1042 Lab 3 - Individual submission for student_health_list function


__author__ = "Elyssa Grant"

__team__ = "T-083"

#==========================================#
# Place your student_health_list function after this line


def student_health_list(datafile, healthiness: int) -> list:
    """
    Given the data sheet name and a value of how healthy the student is from 1 to 5, returns the files of all students with that level of health as a list of dictionaries, excluding the health value. If the health value is not in the file, returns an empty list

    Preconditions: data file named 'student-mat.csv'

    Examples:

    >>> student_health_list('student-mat.csv', 2)
    [ {'School': 'MS', 'Age': 20, 'StudyTime': 1.2, 'Failures': 1, 'Absences': 10,
     'G1': 9, 'G2': 11, 'G3': 7}, {another element}, … ]

     >>> student_health_list('student-mat.csv', -3)
     []

    """
    # importing modules
    import string

    # opening the file
    file = open(datafile, 'r')

    # creating a list of the keys for the dictionaries
    dictionary_keys = (file.readline()).strip().split(",")

    # Creating an empty list and dictionary
    all_relevant_students = []
    student = {}

    # looping over the entire file one line at a time
    for line in file.readlines():

        # Clearing line of whitespace and splitting the string into a list of individual words
        words = line.strip().split(",")

        # checking if the health value is equal to the specified value in order to get dictionary
        if int(words[4]) == healthiness:

            # looping over every piece of data to add it to the dictionary
            for i in range(len(words)):

                # changing the data to the appropriate value types
                if i != 0 and i != 2:
                    words[i] = int(words[i])

                elif i == 2:
                    words[i] = float(words[i])

                # adding the value to the temporary dictionary
                student[dictionary_keys[i]] = words[i]

            del student['Health']

            all_relevant_students.append(student.copy())

    file.close()

    return all_relevant_students
