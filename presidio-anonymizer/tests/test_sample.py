import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    result = sample_run_anonymizer("My name is Bond.", 11, 15)
    assert result.text == "My name is BIP."
    assert result.items[0].start == 11
    assert result.items[0].end == 14
    pass