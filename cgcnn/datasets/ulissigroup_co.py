import torch
from torch_geometric.data import InMemoryDataset


class UlissigroupCO(InMemoryDataset):
    def __init__(self, root, transform=None, pre_transform=None):
        super(UlissigroupCO, self).__init__(root, transform, pre_transform)
        self.data, self.slices = torch.load(self.processed_paths[0])

    @property
    def processed_file_names(self):
        return "data.pt"

    def _download(self):
        pass

    def _process(self):
        pass