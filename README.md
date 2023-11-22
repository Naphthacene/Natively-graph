# Natively-graph

Quick and dirty code to plot some figures based on your stats from https://learnnatively.com

## Requirements

This code was tested on python 3.9 but should work for python >= 3.7

The code relies on the following libraries:
```
numpy
scipy
pandas
matplotlib
seaborn
```

You can install them by running 
```
$pip install -m requirements.txt
```

## Usage

First, you need to download your data from Natively.
When signed in, you can currently generate and download the file at https://learnnatively.com/account-settings/?form=data_download

Then, run the code with the file as an argument.
```
$python make_figs.py path_to_file/filename.csv
```
The code will generate a few figures in the same folder.

## Current figures

Books read per year

![hist_plot](https://github.com/Naphthacene/Natively-graph/assets/150095040/105417de-64ff-46b0-a4dd-39982e4b4844)

Aggregate book level over time

![min_max_plot](https://github.com/Naphthacene/Natively-graph/assets/150095040/d73b55bc-f7a1-483f-9f46-8213cf10eef5)


Level over time separated by book type, with linear regression

![with_regs](https://github.com/Naphthacene/Natively-graph/assets/150095040/1d47a5f7-1763-4e24-891e-49e95a44765a)

