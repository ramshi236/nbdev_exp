# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/011_my_first_pipline.ipynb (unless otherwise specified).

__all__ = ['get_dataset', 'get_train_data_loader', 'GNN']

# Cell
import torch
import torch_geometric
from torch_geometric.data import HeteroData
from torch_geometric.datasets import OGB_MAG
from torch_geometric.utils import add_self_loops, degree
from torch_geometric.nn import SAGEConv, to_hetero
import hiddenlayer as hl
from torchsummary import summary

from pathlib import Path

# Cell
def get_dataset():
    root =str((Path.cwd().parent / "data").absolute())
    transform = torch_geometric.transforms.ToUndirected()  # Add reverse edge types.

    dataset = OGB_MAG(root=root, preprocess='metapath2vec', transform=transform)
    return dataset

def get_train_data_loader():
    dataset = get_dataset()
    data = dataset[0]
    train_loader = torch_geometric.loader.NeighborLoader(
        data,
        # Sample 15 neighbors for each node and each edge type for 2 iterations:
        num_neighbors=[15] * 1,
        # Use a batch size of 128 for sampling training nodes of type "paper":
        batch_size=1,
        input_nodes=('paper', data['paper'].train_mask),
    )
    return train_loader

class GNN(torch.nn.Module):
    def __init__(self, hidden_channels, out_channels,
                 ):
        super().__init__()
        self.conv1 = SAGEConv((-1, -1), hidden_channels)  #.jittable()
        self.conv2 = SAGEConv((-1, -1), out_channels)  #.jittable()

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index).relu()
        x = self.conv2(x, edge_index)
        return x



# Cell
from nbdev.export import notebook2script; notebook2script()
#
# notebook2script()