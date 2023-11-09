def tf_transform(count_matrix: list[list[int]]) -> list[list[float]]:
    """
    Build the term frequency matrix for count matrix with formula:
    the number of repetitions of the word divided by the total number

    Args:
        count_matrix (list[list[int]]): prepared count matrix

    Returns:
        list[list[float]]: Result matrix
    """
    tf_matrix = []
    for vector in count_matrix:
        count = sum(vector)
        tf_matrix.append([round(element / count, 3) for element in vector])
    return tf_matrix


if __name__ == '__main__':
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    tf_matrix = tf_transform(count_matrix)
    print(tf_matrix)
