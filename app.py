# -*- coding:utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns
import scikit-learn as sk
import plotly as go

def main():

    st.markdown('# Hello World')
    st.write(np.__version__)
    st.write(pd.__version__)
    st.write(matplotlib.__version__)
    st.write(sns.__version__)
    st.write(sk.__version__)
    st.write(go.__version__)
    st.write(np.__version__)

if __name__ == '__main__':
    main()