from math import e, pi, sqrt

def normal_pdf(x, mu, sigma):
    return (1 / sqrt(2*pi*sigma**2) * e**((-(1/2)*((x-mu)**2 / sigma**2))))


def normal_cdf(x=0, mu=0, sigma=2):
    vals = []
    
    for num in range(-10000, int(x*1000)):
        vals.append(num*0.001)

    print(vals)

print(normal_cdf())