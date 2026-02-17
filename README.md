# TOPSIS Decision Support System

This repository implements the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) using three approaches:

-Part I — Command Line Python Program
-Part II — Python Package (Published on PyPI)
-Part III — Web Application (Streamlit Web Service)

The system ranks alternatives based on multiple criteria using weights and impacts.

## Part I — Command Line Implementation
A Python program that computes TOPSIS ranking from a CSV file using terminal arguments.

Usage
python topsis.py <InputFile> <Weights> <Impacts> <OutputFile>

## Part II — Python Package (PyPI)
Package Name
topsis-eva-102317129

Installation
pip install topsis-eva-102317129

topsis data.csv "1,1,1,1,1" "+,+,+,-,+" result.csv

PyPI Link
https://pypi.org/project/topsis-eva-102317129/

## Part III — Web Service (Streamlit)
A web interface allowing users to upload dataset and receive ranked results via email.

Run Application
streamlit run topsis_streamlit.py

Sends result CSV to emailt

