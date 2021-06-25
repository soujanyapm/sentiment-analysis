#================Using dash module to build the UI========================#

# Importing the libraries

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc



# Declaring Global variables
print("hello")
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP,'https://use.fontawesome.com/releases/v5.8.1/css/all.css'],suppress_callback_exceptions=True) # creating object of Dash
project_name = "Sentiment Analysis with Insights"
app.title = project_name
server = app.server


# Defining My functions


    



