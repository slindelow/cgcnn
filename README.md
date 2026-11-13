# CGCNN

A Crystal Graph Convolutional Neural Network in PyTorch that predicts a crystal property from atom and bond features. I implemented it by following the CaMML workshop notebook on graph networks, so the code follows the workshop's structure, helper functions and dataset.

`notebooks/01-cgcnn-practice.ipynb` contains the graph convolution, the full CGCNN, training and evaluation functions, a 40-epoch CPU run, prediction plots and experiments with convolution count and embedding size.

## Recorded results

The initial three-convolution model with 64 node features completed 40 epochs and reported test MAE `0.0958` on the log10 target scale. The convolution experiment had its lowest validation MAE at four layers (`0.0955`). The embedding experiment, with three convolutions fixed, had its lowest validation MAE at 128 features (`0.0958`). These are separate experiments, so the combination of four convolutions and 128 features has not been tested.

The embedding exercise initially followed the workshop's test-MAE comparison, and I then evaluated the saved models on validation data to choose the embedding size. These exploratory results use one random split and are not official five-fold Matbench benchmark scores.

The workshop describes the target as log10 VRH-average shear modulus, although its bundled filename is `bulk-modulus-dataset.json`, so check the target provenance before interpreting results as a particular physical property.

## Run it

From this repository folder, run these commands with [uv](https://docs.astral.sh/uv/).

```sh
uv sync --locked
uv run python scripts/download_reference.py
uv run jupyter lab
```

The download script fetches the CaMML notebook, its helper file and the dataset at a pinned commit into the ignored `reference/camml/` folder and checks each file against the hash in `docs/reference-manifest.json`.

## Credits

The model, helper code and dataset come from the CaMML workshop. Their materials are not redistributed here.

- [CaMML workshop notebook](https://workshop.camml.ac.uk/notebooks/cgcnn/graph-networks/)
- [CaMML source materials](https://gitlab.com/cam-ml/tutorials/-/tree/main/notebooks/04-cgcnn)
