import streamlit as st
import pandas as pd
import numpy as np
import yagmail
import re

st.title("TOPSIS Web Service")

file = st.file_uploader("Upload CSV File", type=["csv"])
weights = st.text_input("Weights (comma separated)")
impacts = st.text_input("Impacts (+ or - comma separated)")
email = st.text_input("Email ID")


def topsis(df, w, im):
    if df.shape[1] < 3:
        return None, "Input file must contain three or more columns"

    try:
        x = df.iloc[:, 1:].astype(float).values
    except:
        return None, "Non numeric values found"

    if len(w) != x.shape[1] or len(im) != x.shape[1]:
        return None, "Weights and impacts mismatch"

    for i in im:
        if i not in ['+', '-']:
            return None, "Impacts must be + or -"

    w = np.array(w, dtype=float)

    x = x / np.sqrt((x**2).sum(axis=0))
    x = x * w

    p = np.zeros(x.shape[1])
    n = np.zeros(x.shape[1])

    for i in range(x.shape[1]):
        if im[i] == '+':
            p[i] = x[:, i].max()
            n[i] = x[:, i].min()
        else:
            p[i] = x[:, i].min()
            n[i] = x[:, i].max()

    sp = np.sqrt(((x - p)**2).sum(axis=1))
    sn = np.sqrt(((x - n)**2).sum(axis=1))
    s = sn / (sp + sn)

    df['Topsis Score'] = s
    df['Rank'] = s.argsort().argsort() + 1

    return df, None


if st.button("Submit"):

    if file is None:
        st.error("Upload a file")
        st.stop()

    email = email.strip()

    if email == "":
        st.error("Email required")
        st.stop()

    if "@" not in email or "." not in email.split("@")[-1]:
        st.error("Invalid email format")
        st.stop()

    w = [i.strip() for i in weights.split(',')]
    im = [i.strip() for i in impacts.split(',')]

    df = pd.read_csv(file)

    result, err = topsis(df, w, im)

    if err:
        st.error(err)
    else:
        result.to_csv("result.csv", index=False)

        try:
            yag = yagmail.SMTP("evxsingh@gmail.com", "mklhufimkqkyljdn")
            yag.send(email, "TOPSIS Result", "Attached is your result", attachments="result.csv")
            st.success("Result sent to email!")
        except Exception as e:
            st.error("Email sending failed. Check Gmail app password setup.")

        st.dataframe(result)
