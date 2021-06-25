#================Using dash module to build the UI========================#

import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px

from app import app



# Defining My functions

    

    
# to automatically open the browser

    
def layout():
    return html.Div(
            [    
            html.Div([  
                
                html.Div(
              children=[       
            html.Div(
    
    children=[
         html.I(className="fas fa-chart-line icon-style"),
        html.Span( children='Sentilysis',className='main-heading',style={'color':'white'}),
    ]
)    
            ],
            
            
        ),
                      dbc.Row(
            [
                dbc.Col(html.Div(
              [
                 
                      html.H5("Sentiment Analysis",style={"color":"rgb(255 122 89)","padding-bottom":"12px"}),
                      html.H1(children=["Understand the sentiment of your", html.Span( children='Customers',className='main-heading',style={'color':'rgb(255 122 89)'}),],style={"padding-bottom":"11px"}),
                      html.P("Performs sentiment analysis and extract meaning from product and service review in form of text",style={"padding-bottom":"23px"}),
                        dcc.Link(  dbc.Button(
             children='Get Started',
             className='get-started-btn'
             ), href='/analysis'),
                    
                    
                  ]
            
            
        ),className="content" ,md=5),
                
                dbc.Col(html.Div(
                    [
                html.Img(src="https://res.cloudinary.com/duqtkbkps/image/upload/v1621941809/sentiment-analysys-brandmentions_jnv89b.png",style={"width":'112vh','padding-top':'62px'})
                   
                    ],className=""
                    ), md=6),
                
                
            ],justify="center",
        ),
             
             ],className='homepage-main-div'),  
                ]
            )

    






