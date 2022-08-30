

# Cell
import torch
import torch_geometric
from torch_geometric.data import HeteroData
from torch_geometric.datasets import OGB_MAG
from torch_geometric.utils import add_self_loops, degree
from torch_geometric.nn import SAGEConv, to_hetero
import hiddenlayer as hl
from torchsummary import summary

