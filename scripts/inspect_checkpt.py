import pickle
import torch

with open("../artifacts/model.pt", "rb") as f:
    try:
        checkpoint_data = pickle.load(f)
        print(checkpoint_data)
    except pickle.UnpicklingError as e:
        print("Invalid pickle file:", e)

