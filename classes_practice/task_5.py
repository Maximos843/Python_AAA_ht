from task_1 import CountVectorizer
from task_4 import TfidfTransformer


class TfidfVectorizer(CountVectorizer):
    """
    Class that performs functions of TfidfVectorizer to convert text corpus
    to tf-idf representation

    Methods:
        fit_transform(list[str]):
            Return tf-idf matrix
    """

    def __init__(self):
        self.feature_names = []
        self.tfidf = TfidfTransformer()

    def fit_transform(self, corpus: list[str]) -> list[list[float]]:
        """
        Convert text corpus to tf-idf matrix

        Args:
            corpus (list[str]): text corpus

        Returns:
            list[list[float]]: tf-idf result matrix
        """
        count_matrix = super().fit_transform(corpus)
        result_matrix = self.tfidf.fit_transform(count_matrix)
        return result_matrix


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_features_names())
    print(tfidf_matrix)
