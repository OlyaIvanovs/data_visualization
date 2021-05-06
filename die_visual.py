from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die()

results = []

for die_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []

max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

xaxis_config = {'title': 'Result', 'dtick': 1}
yaxis_config = {'title': 'Frequecy of result'}

my_layout = Layout(title='Result of rolling two D6 1000 times',
                   xaxis=xaxis_config, yaxis=yaxis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
