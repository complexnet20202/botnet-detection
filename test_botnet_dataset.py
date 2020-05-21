from botdet.data.dataset_botnet import BotnetDataset
from networkx.classes import function as fn

if __name__ == '__main__':
    dataset = BotnetDataset(name='p2p', split='train', graph_format='nx', in_memory=False)
    print(dataset)
    print(len(dataset))
    print(fn.info(dataset[0]))
    breakpoint()
