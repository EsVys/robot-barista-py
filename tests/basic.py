import pytest
import sys
sys.path.append("..")

import modules.bouncer as bouncer
import modules.greet as greet


def test_fail_bouncer_age_validation(monkeypatch):
    name = 'John'
    monkeypatch.setattr('builtins.input', lambda _: 'no')
    result = bouncer.age_validation(6, name)
    assert result == False

def test_success_bouncer_age_validation():
    name = 'John'
    result = bouncer.age_validation(16, name)
    assert result == True

def test_success_bouncer_validate_input_age(monkeypatch):
    input = 20
    name = 'John'
    monkeypatch.setattr('builtins.input', lambda _: input)
    result = bouncer.validate_input_age(name)
    assert result == True

def test_success_evil_status_no_ben(monkeypatch):
    input = 'no'
    name = 'Ben'
    monkeypatch.setattr('builtins.input', lambda _: input)
    result = bouncer.evil_status(name)
    assert result == True

def test_success_evil_status_no_Pat(monkeypatch):
    input = 'no'
    name = 'Pat'
    monkeypatch.setattr('builtins.input', lambda _: input)
    result = bouncer.evil_status(name)
    assert result == True

def test_success_greet_no_name(monkeypatch):
    greeting = 'Hello!'
    input = ''
    monkeypatch.setattr('builtins.input', lambda _: input)
    result = greet.greet(greeting)
    assert result == 'Honey'


#not working - function evil.status has two inputs Either rewrite the function or find a solution for the test.
#def test_success_evil_status_yes_deeds_yes(monkeypatch):
#    evilst = 'yes'
#    good_deeds = 2
#    monkeypatch.setattr('builtins.input', lambda _: next())
#    result = bouncer.evil_status(name)
#    assert result == 'All right, you can have a coffee.'