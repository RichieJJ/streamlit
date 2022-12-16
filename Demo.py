import streamlit as st

import numpy as np
import pandas as pd

st.title('Proofpoint Demo')

st.write("Data Table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


st.write("Line Chart:")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# st.write("Plot a map")
# map_data = pd.DataFrame(
#    np.random.randn(100, 2) / [100, 100] + [39.919358,-105.1064319],
#    columns=['lat', 'lon'])

# st.map(map_data)
