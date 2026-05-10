import matplotlib.pyplot as plt

# Input arrays
x = list(map(int, input("Enter first array values: ").split()))
y = list(map(int, input("Enter second array values: ").split()))

# Line Chart
plt.plot(x, y)
plt.title("Line Chart")
plt.show()

# Bar Chart
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()

# Pie Chart
plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# Scatter Chart
plt.scatter(x, y)
plt.title("Scatter Chart")
plt.show()

# Histogram
plt.hist(y)
plt.title("Histogram")
plt.show()