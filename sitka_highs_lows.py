import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, value in enumerate(header_row):
        print(index, value)

    dates, highs, lows = [], [], []
    for row in reader:
        high = int(row[5])
        low = int(row[6])
        date = datetime.strptime(row[2], '%Y-%m-%d')
        highs.append(high)
        dates.append(date)
        lows.append(low)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures 2018", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)

plt.show()
