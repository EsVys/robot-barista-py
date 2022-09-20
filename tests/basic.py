import pytest
import sys
sys.path.append("..")

from sre_constants import SUCCESS
from unicodedata import name

import modules.bouncer as bouncer
import modules.greet as greet


def test_fail_bouncer_age_validation():
    name = 'John'
    with pytest.raises(SystemExit):
        bouncer.age_validation(6, name)

def test_success_bouncer_age_validation():
    bouncer.age_validation(16, name)

def test_success_bouncer_validate_input_age(monkeypatch):
    input = 20
    name = 'John'
    monkeypatch.setattr('builtins.input', lambda _: input)
    age = bouncer.validate_input_age(name)
    assert age == input

def test_success_evil_status_no_ben(monkeypatch):
    input = 'no'
    name = 'Ben'
    monkeypatch.setattr('builtins.input', lambda _: input)
    bouncer.evil_status(name)

def test_success_evil_status_no_Pat(monkeypatch):
    input = 'no'
    name = 'Pat'
    monkeypatch.setattr('builtins.input', lambda _: input)
    bouncer.evil_status(name)

def test_success_evil_status_yes_deeds_yes(monkeypatch):
    name = 'Ben'
    evilst = 'yes'
    good_deeds = 2
    monkeypatch.setattr('builtins.input', lambda _: next())
    result = bouncer.evil_status(name)




###

def test_greet_no_name(monkeypatch):
    greeting = 'Hello!'
    input = ''
    monkeypatch.setattr('builtins.input', lambda _: input)
    result = greet.greet(greeting)
    assert result == 'Darling'