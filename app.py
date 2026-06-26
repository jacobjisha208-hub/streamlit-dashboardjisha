import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt

st.title("Care Load Dashboard")

df=pd.read_excel(r"C:\Users\jijin\Downloads\HHS_Unaccompanied_Alien_Children_Program20878(3).xlsx",header=1)

df.columns=["Year","Total System Load"]
df=df.dropna()
df=df[df["Year"] != "Row Labels"]
df=df[df["Year"] != "Grand Total"]
df["Total System Load"] = pd.to_numeric(df["Total System Load"], errors="coerce")
df= df.dropna()

st.subheader("Total System Load by Year")
st.write(df)

fig, ax =plt.subplots()
ax.bar(df["Year"].astype(str),df["Total System Load"], color="steelblue")
ax.set_title("Total System Load by Year")
ax.set_ylabel("Total Load")
st.pyplot(fig)