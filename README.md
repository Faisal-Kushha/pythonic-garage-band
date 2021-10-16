# Lab: 04 - Classes, and Fixtures

Garage Band with OOP

# Description

A Python application using Object Oriented Programming.

# Requirements

python 3.9.7
black
flake
pytest

# Feature Tasks

- [x] Use Python classes to model a `Band` made up of different kinds of musicians.

- [x] Start with `Guitarist` , `Bassist` , and `Drummer` .

- [x] Make use of a `Musician` base class to handle common functionality which particular kinds of musicians will inherit.

### User Acceptance Tests

- [x] Unit tests will be supplied for this lab. Your job is to make them pass. Do **NOT** modify the supplied tests (except to enable for stretch goals.)

#### Band Tests

- [x] A `Band` instance should have a `name` attribute which is a string.
- [x] A `Band` instance should have a `members` attribute which is a list of instances that inherit from `Musician` base (or super) class.
- [x] A `Band` instance should have a `play_solos` method that asks each member musician to play a solo, in the order they were added to band.
- [x] A `Band` instance should have appropriate `__str__` and `__repr__` methods.
- [x] A `Band` should have a class method `to_list` which returns a list of previously created `Band` instances

#### Musician Subclass Tests

- [x] Each kind of `Musician` instance should have appropriate `__str__` and `__repr__` methods.
- [x] Each kind of `Musician` instance should have a `get_instrument` method that returns string.
- [x] Each kind of `Musician` instance should have a `play_solo` method that returns string.

# Get Started

```python
poetry install
poetry shell
pytest
```

# Developer

Faisal Kushha

I get some help from Jehad Abu Awwad

# Pull Request

https://github.com/Faisal-Kushha/pythonic-garage-band/pull/1
