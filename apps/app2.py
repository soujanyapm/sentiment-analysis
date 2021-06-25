#================Using dash module to build the UI========================#

# Importing the libraries
import pickle
import pandas as pd
import webbrowser

import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

from app import app

# Declaring Global variables

df = pd.read_csv('./assets/predictions.csv')

scrapped_reviews = pd.read_csv('./assets/scrapped_reviews_final.csv')

print(len(scrapped_reviews['reviews'].values))

#print((scrapped_reviews['reviews'].sample(n=100,random_state=1).values))

fig = px.pie(df, "predictions", color='predictions',
             color_discrete_map={'Positive':'#00b7e3','Negative':'#ff7a59'},width=580, height=350)
#6bfec4
fig.update_layout({
'plot_bgcolor': '#1b2a47',
'paper_bgcolor': '#1b2a47',
'font_color':"#8f98a0"

})

file = open('./assets/frequent_words.txt','r')

text = file.read()

# Defining My functions
def load_model():
    global scrappedReviews
    scrappedReviews = pd.read_csv('./assets/scrappedReviews.csv')
    
    global pickle_model
    file = open("./assets/pickle_model.pkl",'rb')
    pickle_model = pickle.load(file)
    
    global vocab
    file = open("./assets/features.pkl",'rb')
    vocab = pickle.load(file)
    
def check_review(reviewText):

    #reviewText has to be vectorised, that vectorizer is not saved yet
    #load the vectorize and call transform and then pass that to model preidctor
    #load it later

    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error="replace",vocabulary=vocab)
    vectorised_review = transformer.fit_transform(loaded_vec.fit_transform([reviewText]))


    # Add code to test the sentiment of using both the model
    # 0 == negative   1 == positive
    
    return pickle_model.predict(vectorised_review)    
    
# to automatically open the browser
def open_browser():
    pass
    #webbrowser.open_new('http://127.0.0.1:8050/')
    
def create_app_ui():
    main_layout = html.Div(
        [
            html.Div(
              children=[       
            html.Div(
    
    children=[
         html.I(className="fas fa-chart-line icon-style"),
        html.Span( children='Sentilysis',className='main-heading'),
    ],style={'background-color':'#152036'}
)
           
            ],
            
            
        ),
            
        html.Div([  

      dbc.Row(
            [
                dbc.Col(html.Div(
                    [
                
                    dcc.Graph(figure=fig)
                    ],className="pie-chart-div"
                    ), md=5),
                
                
                dbc.Col(html.Div(
                    [
                         dcc.Dropdown(
                          id='review-dropdown',
                            options=[
                               {'label': x, 'value': x} for x in (scrapped_reviews['reviews'].sample(n=100,random_state=1).values)
                            ],
                            value=None,
                            placeholder='Select a review...',
                            
    
                            
    ),
                  html.Div(id='dd-output-container')
                        ]
                    
                    ), className="reviews-dropdown-div" , md=6),
                
            ],justify="center",
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(
                    [
                   
                        
                 html.Img(src=app.get_asset_url('wordscloud.png'),className='wordscloud-img',style={'width':400,'height':275,'margin-top':50,'margin-left':87})
                        
                    ],className="wordscloud-div"
                    ), md=5),
                dbc.Col(html.Div(
                    [
                         dcc.Textarea(
             id='textarea_review',
             placeholder = "Enter the review here.....",
             className="review-textarea"
             ),
                         
                      html.Div(   
                     [ dbc.Button(
             children='Find Review',
             id='button_review',
             color='dark',
             className='find-review-btn'
             )], style={'text-align':'center'}),
         
         html.Div(id='result')
                        
                        
                        ]
                    
                    ), className='review-textarea-div', md=6),
  
            ],justify='center'
        ),
        
       
         ],className='main-div'),  
            ]
        )
    return main_layout

    
@app.callback(
    Output('result','children'),
    [
      Input('button_review','n_clicks')
     ],
    [
     State('textarea_review','value')
     
     ]
    
    )    
def update_app_ui(n_clicks,textarea_value):
    
    print('Data Type of',str(type(n_clicks)))
    print('Value=', str(n_clicks))
    
    print('Data Type of',str(type(textarea_value)))
    print('Value=', str(textarea_value))
    
    if(n_clicks > 0):
    
        response = check_review(textarea_value)
        
        if(response[0]==0):
            return html.H3('Negative',style={'color':'#f45353','font-size':'30px','text-align':'center','padding-top':'15px'})
        elif(response[0]==1):
            return html.H3('Positive',style={'color':'#17e0a8','font-size':'30px','text-align':'center','padding-top':'15px'}) 
        else:
            return 'Unknown'
            
        
    
    
@app.callback(
    Output('dd-output-container', 'children'),
    [Input('review-dropdown', 'value')])
def update_output(value):
        response = check_review(value)
        
        if(response[0]==0):
            return html.Div('Negative',style={'color':'#f45353','font-size':'30px'})
        elif(response[0]==1):
            return html.Div('Positive',style={'color':'#17e0a8','font-size':'30px'})   
          
    
   
    

# Main Function to control the Flow of your Project
def main():
    print("Start of your project")
    load_model()
    open_browser()

    global scrappedReviews
    
    layout = create_app_ui()
    
    return layout
     
    



