import random

# Define the function to be integrated
def f(x):
    # dkhag
    return x**2

def monte_carlo(num_points = 100000):
    # Define the interval [a, b]
    a = 0
    b = 3
    f_min = 0
    f_max = 9
    area_rec = (b-a)*(f_max-f_min)
    # Initialize a counter for points below the curve
    points_below = 0

    # Generate random points and count points below the curve
    for i in range(num_points):
        x = random.uniform(a,b)
        y = random.uniform(f_min,f_max)

        if y < f(x):
            points_below += 1
            
    # Calculate the estimated integral
    integral_estimate = (points_below/num_points) * area_rec
    return integral_estimate

    
if __name__ == "__main__":
    # Number of random points to generate
    num_points = int(input('Number of random points to generate: '))
    integral_estimate = monte_carlo(num_points)
    print("Estimated Integral:", integral_estimate)

