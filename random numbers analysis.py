import numpy as np
import matplotlib.pyplot as plt

def analyze_random_numbers(num_samples, min_val, max_val):
    # Generate random numbers
    random_data = np.random.randint(min_val, max_val + 1, num_samples)
    
    # Calculate basic statistics
    mean_value = np.mean(random_data)
    median_value = np.median(random_data)
    std_deviation = np.std(random_data)
    
    # Plot a histogram of the random data
    plt.hist(random_data, bins=20, edgecolor='black')
    plt.xlabel('Random Numbers')
    plt.ylabel('Frequency')
    plt.title('Histogram of Random Numbers')
    plt.show()
    
    # Print the analysis results
    print(f"Number of samples: {num_samples}")
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")
    print(f"Mean: {mean_value:.2f}")
    print(f"Median: {median_value}")
    print(f"Standard Deviation: {std_deviation:.2f}")

# Test the function
num_samples = 100
min_val = 50
max_val = 100
analyze_random_numbers(num_samples, min_val, max_val)