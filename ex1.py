import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Streamlit Dashboard with Plotly")

# Data
data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 15, 25]
}

df = pd.DataFrame(data)

# Force category order (THIS fixes the missing A issue)
fig = px.bar(
    df,
    x="Category",
    y="Values",
    title="Sample Bar Chart",
    category_orders={"Category": ["A", "B", "C", "D"]}
)

st.plotly_chart(fig, use_container_width=True)
