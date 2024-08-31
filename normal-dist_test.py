import matplotlib.pyplot as plt
import scipy.stats as stats

""" Do I need scipy? """

def check_normal_distribution(data):
  """
  Plots a histogram and performs a Shapiro-Wilk test to check for normality.

  Args:
    data: A list or NumPy array of numbers.
  """

  # Plot a histogram
  plt.hist(data, bins=10, density=True)
  plt.title("Histogram of Data")
  plt.xlabel("Value")
  plt.ylabel("Density")
  plt.show()

  # Perform Shapiro-Wilk test
  statistic, p_value = stats.shapiro(data)
  print("Shapiro-Wilk Test:")
  print("Statistic:", statistic)
  print("P-value:", p_value)

  # Interpret the results
  alpha = 0.05
  if p_value > alpha:
    print("Data appears to be normally distributed.")
  else:
    print("Data does not appear to be normally distributed.")

# Replace this with your array of 10 numbers
data = [2, 4, 5, 3, 6, 1, 7, 8, 9, 10]

check_normal_distribution(data)