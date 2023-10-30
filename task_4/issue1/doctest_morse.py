from morse import LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    Encodes a string according to the Morse code table

    >>> encode('SOS')
    '... --- ...'
    >>> encode('LID')
    '.-.. .. -..'
    >>> encode('sos')
    Traceback (most recent call last):
    KeyError: 's'
    >>> encode(65)
    Traceback (most recent call last):
    TypeError: 'int' object is not iterable

    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)
