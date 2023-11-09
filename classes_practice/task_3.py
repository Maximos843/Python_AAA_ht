import math


def idf_transform(count_matrix: list[list[int]]) -> list[float]:
    """
    Build the inverse document frequency matrix for count matrix with formula:
    ln((the total number of documents + 1) / (documents with the word + 1)) + 1

    Args:
        count_matrix (list[list[int]]): prepared count matrix

    Returns:
        list[float]: Result matrix
    """
    idf_matrix = []
    n = len(count_matrix)
    for i in range(len(count_matrix[0])):
        count_elem_in_docs = 0
        for vector in count_matrix:
            if vector[i] != 0:
                count_elem_in_docs += 1
        idf_matrix.append(round(math.log((n + 1) / (count_elem_in_docs + 1)) + 1, 1))
    return idf_matrix


if __name__ == '__main__':
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    idf_matrix = idf_transform(count_matrix)
    print(idf_matrix)
