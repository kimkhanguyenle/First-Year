class Rational(object):
    def __init__(self, numer, denom):
        self._numer = numer
        self._denom = denom
    def numberator(self):
        return self._numer
    def denominator(self):
        return self._denom
    def __str__(self):
        return str(self._numer) + "/" + str(self._denom)



    def __add__(self, other):
        """Returns the sum of the numbers."""
        #Self is the left operand and other is the right operand
        newNumer = self._numer * other._denom + \
                   other._numer * self._denom
        newDenom = self._denom * other._denom
        return Rational(newNumer, newDenom)

    def __mul__(self, other):
        newNumer = self._numer * other._numer
        newDenom = self._denom * other._denom
        return Rational(newNumer, newDenom)
    def __lt__(self, other):
        """Compares two rational numbers, self and other, using <."""
        extremes = self.numer * other._denom
        means = other._numer * self._denom
        return extremes < means 
