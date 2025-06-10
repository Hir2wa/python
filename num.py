import matplotlib.pyplot as plt # type: ignore

# Data from the chart
labels = ["Start", "Support", "Current", "Resistance", "End"]
prices = [85.2500, 85.2600, 85.25842, 85.26418, 85.2700]

# Convert labels to numerical indices for fill_between
x_indices = range(len(labels))

# Plotting the price line
plt.plot(x_indices, prices, label="Price", color="green", marker="o")

# Shading the buy zone (around support at 85.2600)
plt.fill_between(x_indices[:2], [85.2600] * 2, color="green", alpha=0.1, label="Buy Zone")

# Shading the sell zone (around resistance at 85.26418)
plt.fill_between(x_indices[3:], [85.26418] * 2, color="red", alpha=0.1, label="Sell Zone")

# Set x-axis labels
plt.xticks(x_indices, labels)

# Adding labels and title
plt.xlabel("Time")
plt.ylabel("Price")
plt.title("EUR/RUB OTC Price Action")
plt.legend()
plt.grid(True)

# Show plot
plt.show()