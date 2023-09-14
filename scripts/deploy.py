import torch

model_filepath = '../artifacts/model.pt'
model = torch.load(model_filepath, map_location=torch.device('cpu'))

with open(model_filepath, 'w') as f:
    print(model, file=f)

