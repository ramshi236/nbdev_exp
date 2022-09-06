# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/010_some_utility_functions.ipynb (unless otherwise specified).

__all__ = ['save_model_simple']

# Cell
import torch


# Cell

#export
def save_model_simple(py_model: torch.nn.Module):
    torch.save(py_model.state_dict(), "shmira_sd.h5")
    torch.save(py_model.state_dict(), "shmira_sd.pt")
    torch.save(py_model, "shmira.h5")
    torch.save(py_model, "shmira.pt")
