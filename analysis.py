from botdet.data.dataset_botnet import BotnetDataset

import plotly.express as px
import networkx as nx
from networkx.classes.function import info

import random

data = BotnetDataset(
  name='p2p',
  split='train',
  graph_format='nx',
  in_memory=False
)

bots = [n for n, attr in data[0].nodes(data=True) if attr['is_bot'] == 1]
botnet = data[0].subgraph(bots)
print(info(botnet))

seg = range(10)

#print(data[0].graph['num_evils'])

px.line(
  x=seg, 
  y=[data[i].graph['num_evils'] for i in seg],
  labels={'x':'tiempo', 'y':'número de bots'}
).show()

