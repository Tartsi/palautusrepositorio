from matchers import *


class QueryBuilder:

    def __init__(self):
        self._matchers = All()

    def build(self):
        return self._matchers

    def playsIn(self, team):
        self._matchers = And(self._matchers, PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self._matchers = And(self._matchers, HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._matchers = And(self._matchers, HasFewerThan(value, attr))
        return self
