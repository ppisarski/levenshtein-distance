import numpy as np


def levenshtein_ratio_and_distance(s, t, ratio=False):
    """
    Calculates levenshtein distance between two strings.
    If ratio = True, computes the levenshtein distance ratio of similarity between two strings
    For all i and j, distance[i,j] will contain the Levenshtein distance
    between the first i characters of s and the first j characters of t
    """
    rows = len(s) + 1
    cols = len(t) + 1
    distance = np.zeros((rows, cols), dtype=int)

    # Populate the distance matrix with the indices of each character of both strings
    for i in range(1, rows):
        for k in range(1, cols):
            distance[i][0] = i
            distance[0][k] = k

    # Compute the cost of deletions, insertions and/or substitutions
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row - 1] == t[col - 1]:
                cost = 0  # If the characters are the same in a given position [i,j] then the cost is 0
            else:
                # Align the results with those of the Python Levenshtein package.
                # If we calculate ratio, the cost of a substitution is 2.
                # If we calculate distance, the cost of a substitution is 1.
                if ratio is True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row - 1][col] + 1,  # Cost of deletions
                                     distance[row][col - 1] + 1,  # Cost of insertions
                                     distance[row - 1][col - 1] + cost)  # Cost of substitutions
    if ratio is True:
        # Computation of the Levenshtein Distance Ratio
        return "Levenshtein distance ratio is {:.2%}.".format(((len(s) + len(t)) - distance[row][col]) / (len(s) + len(t)))
    else:
        # Uncomment if you want to see the matrix showing how the algorithm computes the cost.
        # print(distance)
        # This is the minimum number of edits needed to convert string a to string b
        return "The strings are {} edits away.".format(distance[row][col])


def main():
    s1 = "John Mnemonic"
    s2 = "Johnny Mnemonic"
    print(levenshtein_ratio_and_distance(s1, s2))
    print(levenshtein_ratio_and_distance(s1, s2, ratio=True))


if __name__ == "__main__":
    main()
