# TOPSIS Python Package

This package implements the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) method using a command line interface.

It ranks alternatives based on multiple criteria using weights and impacts.

## Installation

Install directly from PyPI:

pip install topsis-eva-102317129


## Command Line Usage

topsis <InputDataFile> <Weights> <Impacts> <OutputFile>

Example:

topsis data.csv "1,1,1,1,2" "+,+,+,-,+" result.csv


## Parameters

Weights:
Comma separated numeric values
Count must match number of criteria columns

Impacts:
+ means beneficial criterion (higher is better)
- means cost criterion (lower is better)


## Output

The program generates a CSV file containing:

• Original data
• Topsis Score
• Rank 

