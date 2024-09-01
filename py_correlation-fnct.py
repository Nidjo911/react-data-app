import numpy as np

def correlation_function(x, y):
    """
    Calculates the correlation function between two arrays.

    Args:
        x: The first array.
        y: The second array.

    Returns:
        The correlation function value.
    """

    # Check if arrays have the same length
    if len(x) != len(y):
        raise ValueError("Arrays must have the same length.")

    # Calculate the mean of each array
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # Calculate the numerator of the correlation formula
    numerator = np.sum((x - mean_x) * (y - mean_y))

    # Calculate the denominator of the correlation formula
    denominator = np.sqrt(np.sum((x - mean_x) ** 2) * np.sum((y - mean_y) ** 2))

    # Calculate the correlation coefficient
    correlation = numerator / denominator

    return correlation

# Example usage
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

correlation_value = correlation_function(x, y)
print("Correlation coefficient:", correlation_value)