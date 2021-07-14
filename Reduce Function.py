# Removed boilerplate
product = lambda a: (lambda t: (t.numerator, t.denominator))(reduce(lambda x, y: x * y, a))