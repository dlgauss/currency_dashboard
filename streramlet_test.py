import streamlit as st
from currencies import parseData
import pandas as pd
import plotly.express as px
from tests import data_from_db
st.title('Currency monitoring')

data_load_state = st.text('Loading data')
# data = parseData()
data =data_from_db()
data_load_state.text('Done')

col_one_list = data['Cumparare USD'].to_numpy()


select1 = st.sidebar.selectbox('Select', ['EUR', 'USD'], key='2')
if not st.sidebar.checkbox("Hide", True, key='3'):
    if select1 == 'EUR':
        fig = px.line(data, x="Date_Now", y="Cumparare USD")
        st.plotly_chart(fig)
# subset_data = data
# value_name = st.sidebar.multiselect('Denumirea Bancii', data.groupby('Denumirea Bancii').count().reset_index().tolio)
#
# if len(value_name) > 0:
#     subset_data = data[data['Denumirea Bancii'].isin(value_name)]
# st.table(data)
# #
# chart_data = pd.DataFrame(
#     list_data,
#     columns=['Test']
#
# )
# st.line_chart(chart_data)