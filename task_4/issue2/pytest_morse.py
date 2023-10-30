import pytest
from morse import decode


@pytest.mark.parametrize(
    "morse_code, result",
    [
        ("--.- ..- .. -", "QUIT"),
        ("", ""),
        ("... --- ...", "SOS"),
        ("..--- .....", "25"),
    ],
)
def test_decode_morse(morse_code, result):
    """Tests for morse decode function"""
    assert decode(morse_code) == result
