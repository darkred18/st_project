import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})

# create a grid options builder and set the column definitions
gob = GridOptionsBuilder.from_dataframe(df)
grid_options = gob.build()

column_defs = grid_options["columnDefs"]
columns_to_hide = ["col2"]

# update the column definitions to hide the specified columns
for col in column_defs:
    if col["headerName"] in columns_to_hide:
        col["hide"] = True

grid_return = AgGrid(df, grid_options)
new_df = grid_return["data"]
st.write(new_df)