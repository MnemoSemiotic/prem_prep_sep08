from math import e, pi, sqrt

def normal_pdf(x, mu, sigma):
    return 1 / sqrt(2 * pi * sigma**2) * e**((- (x - mu)**2) / 2 * sigma**2)