import matplotlib.pyplot as plt

input_values = range(1, 5000)
cubes = [x**3 for x in input_values]

plt.style.use('seaborn-darkgrid')

fig, ax = plt.subplots()
ax.scatter(input_values, cubes, c=cubes, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 5000, 0, 1100000])

# Set size of tick labels.
ax.tick_params(axis="both", labelsize=14)


plt.show()
