import random


def uniform(size: int = 10, lower_bound: float = 0.0, upper_bound: float = 1.0) -> list:
    if lower_bound == None:
        raise TypeError("Expected lower bound, did not receive one")

    if upper_bound == None:
        raise TypeError("Expected upper bound, did not receive one")

    if abs(lower_bound - upper_bound) < 0.0001:
        raise ValueError('Lower and upper bounds approximately equal')

    if lower_bound > upper_bound:
        lower_bound, upper_bound = upper_bound, lower_bound
    
    return [random.uniform(lower_bound, upper_bound) for i in range(size)]

def normal(size: int = 10, mu: float = 0.0, sigma: float = 1.0) -> list:
    if mu == None:
        raise TypeError("Expected lower bound, did not receive one")

    if sigma == None:
        raise TypeError("Expected upper bound, did not receive one")

    return [random.gauss(mu, sigma) for i in range(size)]

def exponential(size: int =10, lam: float =1.0) -> list:
    if lam <= 0.0:
        raise TypeError('Lambda parameter must be positive')
    
    return [random.expovariate(lam) for i in range(size)]
