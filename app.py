# -----------------------
# Imports
# -----------------------
import os
import random
import html
import re
import sqlite3
import urllib.parse
from xml.etree import ElementTree

import pandas as pd
import folium
import requests
import altair as alt
import streamlit as st

# Optional Streamlit extensions
try:
    from streamlit_folium import st_folium
except ImportError:
    st.error("⚠️ Missing package: streamlit_folium. Add it to requirements.txt")

try:
    from streamlit_autorefresh import st_autorefresh
except ImportError:
    st.warning("⚠️ Missing package: streamlit_autorefresh. Some features may not work.")

# -----------------------
# Streamlit Page Configuration
# -----------------------
st.set_page_config(
    page_title="Wegovy Sampark — Streamlit Prototype",
    layout="wide"
)
