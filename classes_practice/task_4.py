import math


class TfidfTransformer:
    """
    Class that performs functions of TfidfTransformer to convert count matrix
    to tf-idf representation

    Methods:
        tf_transform(corpus: list[list[int]]):
            Build term frequency matrix

        idf_transform(corpus: list[list[int]]):
            Build inverse document frequency matrix

        fit_transform(list[list[int]]):
            Return tf-idf matrix
    """

    def __init__(self):
        self.matrix = []

    def tf_transform(self, count_matrix: list[list[int]]) -> list[list[float]]:
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

    def idf_transform(self, count_matrix: list[list[int]]) -> list[float]:
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

    def fit_transform(self, count_matrix: list[list[int]]) -> list[list[float]]:
        """
        Build tf-idf matrix with formula: tf * idf

        Args:
            count_matrix (list[list[int]]): prepared count matrix

        Returns:
            list[list[float]]: Result matrix
        """
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        result_matrix = []
        for doc in tf:
            result_matrix.append([round(t * i, 3) for t, i in zip(doc, idf)])
        return result_matrix


if __name__ == '__main__':
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(tfidf_matrix)
