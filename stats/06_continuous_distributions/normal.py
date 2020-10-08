from math import e, pi, sqrt

def normal_pdf(x, mu, sigma):
    return (1 / sqrt(2*pi*sigma**2) * e**((-(1/2)*((x-mu)**2 / sigma**2))))

print(normal_pdf(x=1.96, mu=0, sigma=1))