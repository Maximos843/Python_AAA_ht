from string import punctuation
from typing import Union


class CountVectorizer:
    """
    Class that performs functions of CountVectorizer to convert text corpus in matrix

    Methods:
        fit_transform(corpus: list[str]):
            Build the matrix with count for each element of corpus number of unique elements

        preprocess_corpus(corpus: list[str]):
            Preprocess text corpus to lower case and remove punctuation

        get_features_names():
            Return list of feature names
    """

    def __init__(self):
        self.matrix = []
        self.feature_names = []

    def fit_transform(self, corpus: list[str]) -> list[list[Union[int, float]]]:
        """
        Build the matrix with count for each element of corpus number of unique elements

        Args:
            corpus (list[str]): text corpus

        Returns:
            list[list[int]]: Result matrix
        """
        n = len(corpus)
        corpus = self.preprocess_corpus(corpus)
        for elem in corpus:
            for word in elem.split():
                if word not in self.feature_names:
                    self.feature_names.append(word)
        self.matrix = [{i: 0 for i in self.feature_names} for _ in range(n)]
        for index, elem in enumerate(corpus):
            for word in elem.split():
                self.matrix[index][word] += 1
            self.matrix[index] = list(self.matrix[index].values())
        return self.matrix

    def get_features_names(self) -> list[list[int]]:
        """
        Return list of feature names

        Returns:
            list[list[int]]: list of features
        """
        return self.feature_names

    def preprocess_corpus(self, corpus: list[str]) -> list[str]:
        """
        Preprocess text corpus to lower case and remove punctuation

        Args:
            corpus (list[str]): text corpus

        Returs:
            list[str]: preprocessed text corpus
        """
        preprocess_corpus = []
        translator = str.maketrans('', '', punctuation)
        for elem in corpus:
            elem = elem.lower()
            elem = elem.translate(translator)
            preprocess_corpus.append(elem)
        return preprocess_corpus


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_features_names())
    print(count_matrix)
