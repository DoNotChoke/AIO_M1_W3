import torch
import torch.nn as nn
data = torch.Tensor([1, 2, 3])  # need to work with tensor data-type
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)


class MySoftMax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        data_exp = torch.exp(data)
        s = data_exp.sum(0, keepdim=True)
        ans = data_exp / s
        return ans


my_softmax = MySoftMax()
output = my_softmax(data)
print(output)


class StableSoftMax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        data_max = torch.max(data, dim=0, keepdim=True)
        data_exp = torch.exp(data - data_max.values)
        s = data_exp.sum(0, keepdim=True)
        return data_exp/s


stable_softmax = StableSoftMax()
output = stable_softmax(data)
print(output)
