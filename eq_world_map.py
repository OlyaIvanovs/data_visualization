import json
import sys

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

try:
    colorscale = sys.argv[1]
except IndexError:
    colorscale = 'Viridis'

filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
    lon = eq_dict['geometry']['coordinates'][0]
    lons.append(lon)
    lat = eq_dict['geometry']['coordinates'][1]
    lats.append(lat)
    title = eq_dict['properties']['title']
    hover_texts.append(title)

# Map the eartquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [4*mag for mag in mags],
        'color': mags,
        'colorscale': colorscale,
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout = Layout(title="Global Earthquakes")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')