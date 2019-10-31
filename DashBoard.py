# Code Written by : Dimassi Wael

#############################################################
# Import Dash
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
#############################################################

#############################################################
# Import Libraries
import pandas as pd
import datetime as dt
import os
import base64
#############################################################

#############################################################
# Set the App settings
app = dash.Dash()
app.config['suppress_callback_exceptions']=True

#############################################################
# Set the Layout for the Mapbox map
mapbox_access_token = 'pk.eyJ1Ijoid2FlbGRpbSIsImEiOiJjanl5NTd2OG0wMzZvM25xOTN6dDNlbXNoIn0.kQTGy0b4q8EXaZBBhZx0-Q'
layout1 = dict(
    autosize=True,
    automargin=True,
    margin=dict(
        l=30,
        r=30,
        b=20,
        t=40
    ),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    legend=dict(text='opo',font=dict(size=19), orientation='h'),
    title='Distribution of Conflict incidences ',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        style="light",
        center=dict(
            lon=-14.05,
            lat=15.54
        ),
        zoom=5,
    )
)
##############################################################
# Set the layout for the mapbox map 2
layout2 = dict(
    mapbox_style="stamen-terrain",
    autosize=True,
    colorscale="Blues",
    automargin=True,
    margin=dict(
        l=30,
        r=30,
        b=20,
        t=40
    ),
    hovermode="closest",
    plot_bgcolor="7f8d0a",
    paper_bgcolor="#F9F9F9",
    coloraxis = "#000000",
    colorbar = dict(bordercolor = "#000000", bgcolor="rgba(0,0,255,150)", tickfont = dict(color="White")),
    legend=dict(font=dict(size=19), orientation='h'),
    title='Conflict Incidents Density Map',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        colorscale="Blues",
        style="light",
        center=dict(
            lon=-14.05,
            lat=15.54
        ),
        zoom=5,
    )
)
########################################################################
months = ["January",
          "Febuary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]
########################################################################
                            #Read_Data_ACLED#
########################################################################
df = pd.read_csv('Data/newAcledData.csv')
df['year'] = df['year'].astype(int)
year_options =[]
for year in df['year'].unique():
    year_options.append({'label':str(year),'value':year})

County_Location_df = df[['country','location']]
County_Location_df = pd.DataFrame(County_Location_df)
dictLocation = {k: g["location"].unique().tolist() for k,g in County_Location_df.groupby("country")}

########################################################################
                            #Read_Data_FoodInsec#
########################################################################
data = pd.read_csv('Data/FoodInsecurity.csv')
data['Year'] = data['Year'].astype(int)
item_options_data =[]
for item in data['Item'].unique():
    item_options_data.append({'label':str(item),'value':item})

########################################################################
                            #Read_Data_FoodInsec#
########################################################################
data_temp = pd.read_csv('Data/Temp.csv')
########################################################################
                            #Read_Data_Water#
########################################################################
# Data : June and July 2019
dt_june = pd.read_csv('Data/water_June.csv')
dt_april = pd.read_csv('Data/water_April.csv')

dt_june['lat'] = pd.to_numeric(dt_june['lat'])
dt_june['lon'] = pd.to_numeric(dt_june['lon'])

dt_april['lat'] = pd.to_numeric(dt_april['lat'])
dt_april['lon'] = pd.to_numeric(dt_april['lon'])
########################################################################
                            #Styles#
########################################################################
notation_style = {
  'display': 'inline',
  'width': '100px',
  'height': '100px',
  #'padding': '5px',
  'fontWeight': 'bold',
  'border': '1px solid blue',
  'background-color': 'yellow'
}

tabs_styles = {
    'height': '5px',
    'width' : '1px',
    'width': '5%',
    'float': 'left',
    'fontWeight': 'bold',
    'color' : '#ffffff',
    #'color' : '#01B8AA',
    'margin-left': '10px',
    #'margin-top' : '5px'
    'line-height': '1.0',
    'text-align' : 'center'
}
tab_style = {
    'height': '55px',
    'width' : '200px',
    'borderBottom': '1px solid #01B8AA',
    #'padding': '10px',
    'fontWeight': 'bold',
    'line-height': '1.0',
    #'backgroundColor': '#111111'
    #'backgroundColor': '#01B8AA',
    'backgroundColor': '#ffffff',
    'margin-left': '10px',
    'text-align' : 'center'
}
main_tab_style = {
    'height': '50px',
    'width' : '250px',
    'borderBottom': '1px solid #01B8AA',
    #'padding': '10px',
    'fontWeight': 'bold',
    'color': 'white',
    'line-height': '1.0',
    #'backgroundColor': '#111111'
    'backgroundColor': '#00502c',
    'margin-left': '0px'
}

tab_selected_style = {
    'height': '50px',
    'width' : '250px',
    'fontWeight': 'bold',
    'borderTop': '3px solid #FFC000',
    'borderBottom': '1px solid #FFC000',
    'backgroundColor': '#FFC000',
    'color': 'white',
    #'padding': '10px',
    'line-height': '1.0',
    'margin-left': '10px',
    'text-align' : 'center',
    'justify-content' : 'center',
    'align-items' : 'center'
}

colorVal = [
        "#F4EC15",
        "#DAF017",
        "#BBEC19",
        "#9DE81B",
        "#80E41D",
        "#66E01F",
        "#4CDC20",
        "#34D822",
        "#24D249",
        "#25D042",
        "#26CC58",
        "#28C86D",
        "#29C481",
        "#2AC093",
        "#2BBCA4",
        "#2BB5B8",
        "#2C99B4",
        "#2D7EB0",
        "#2D65AC",
        "#2E4EA4",
        "#2E38A4",
        "#3B2FA0",
        "#4E2F9C",
        "#603099",
    ]
########################################################################
                            #App#
########################################################################
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = \
    html.Div([

    html.Div([html.Img(src='/assets/logo.png' ),]),
        html.H1('Exploring the interconnection between climate change, migration, conflict and natural resource management',
                style={'textAlign': 'center',
                       'margin': '48px 0',
                       'fontFamily': 'system-ui',
                       'background-color': '#FFFFFF'}),
    html.H3('Demo Version 1',
            style={'textAlign': 'center',
                   'margin': '48px 0',
                   'fontFamily': 'system-ui',
                   'background-color': '#FFFFFF'}),
        html.Div([
            dcc.Tabs(id="tabs", value='1',
                     vertical=True,
                     parent_style={'flex-direction': 'column',
                                   '-webkit-flex-direction': 'column',
                                   '-ms-flex-direction': 'column',
                                   'display': 'flex'},
                     children=[
                               dcc.Tab(label='Factors in details',value='1', style=main_tab_style, selected_style=main_tab_style),
                               dcc.Tab(label='Conflicts', value='1', style=tab_style, selected_style=tab_selected_style),
                               dcc.Tab(label='Agriculture and Food Security', value='2', style=tab_style, selected_style=tab_selected_style),
                               dcc.Tab(label='Temperature', value='3', style=tab_style, selected_style=tab_selected_style),
                               dcc.Tab(label='Water Availability', value='4', style=tab_style, selected_style=tab_selected_style),


                               dcc.Tab(label='Explore Change Maps', value='6', style=main_tab_style, selected_style=main_tab_style),
                               dcc.Tab(label='Time Series of Vegetation Indices', value='6', style=tab_style, selected_style=tab_selected_style),
                               dcc.Tab(label='Vegetation Timelapse', value='5', style=tab_style, selected_style=tab_selected_style),
                               dcc.Tab(label='Land Cover Land Use', value='7', style=tab_style, selected_style=tab_selected_style),
                               dcc.Tab(label='Population Dynamics', value='8', style=tab_style, selected_style=tab_selected_style),
                               dcc.Tab(label='Land Surface Temperature ', value='9', style=tab_style, selected_style=tab_selected_style),
                               dcc.Tab(label='Statistical Analysis', value='10', style=main_tab_style, selected_style=main_tab_style)])],
            style={'width': '5%',
                   'float': 'left','margin-left': '0px'}),
        html.Div(id='tab-out',
                 style={'width': '80%', 'float': 'right'})])


########################################################################
                            #Tabs#
########################################################################

@app.callback(Output('tab-out', 'children'),
            [Input('tabs', 'value')])
def tab_content(tabs_value):
    """return s.th. based on tabs_value"""
    if tabs_value == '1':
        children = html.Div([
                 #html.Div(
                #     [

                html.Div([
                html.Div([html.H1('Conflict Incidences and Fatality ',
                        style={'textAlign': 'center',
                                'display': 'inline-block',
                               'margin': '5px 0',
                               'fontFamily': 'system-ui'}),
                                html.Abbr("\uD83D\uDEC8", title="The Armed Conflict Location & Event Data Project (ACLED) \n https://data.humdata.org/ ")], className = "spann"),
                    dcc.Dropdown(id="selected_Country",options=[
                    {'label': 'Senegal', 'value': 'Senegal'},
                    {'label': 'Mali', 'value': 'Mali'},
                    {'label': 'Mauritania', 'value': 'Mauritania'},
                    {'label': 'Nigeria', 'value': 'Nigeria'}],
                placeholder="Senegal",value='Senegal'),
                dcc.Dropdown(id='year-picker',options= year_options , value=df['year'].min()),
                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.P("No. of Conflict Events"),
                                                        html.H6(
                                                            id="events_text",
                                                            className="info_text"
                                                        )
                                                    ],
                                                    id="wells",
                                                    className="pretty_container"
                                                ),
                                                html.Div(
                                                    [
                                                        html.P("No. of Conflict Incidents leading to fatalities"),
                                                        html.H6(
                                                            id="FatalityText",
                                                            className="info_text"
                                                        )
                                                    ],
                                                    id="wells",
                                                    className="pretty_container"
                                                ),
                                                html.Div(
                                                    [
                                                        html.P("No of Conflict incidents without fatalities"),
                                                        html.H6(
                                                            id="noFatalityText",
                                                            className="info_text"
                                                        )
                                                    ],
                                                    id="wells",
                                                    className="pretty_container"
                                                ),
                                            ],
                                            id="infoContainer",
                                            className="row"
                                        ),

                                    ],
                                    """id="rightCol",
                                    className="eight columns" """)],id="wells",
                                    className="pretty_container"),


                        html.Div([
                        html.Div([ html.H1('Fatality over years',
                                style={'textAlign': 'center',
                                       'margin': '5px 0',
                                       'display': 'inline-block',
                                       'fontFamily': 'system-ui'}),
                                       html.Abbr("\uD83D\uDEC8", title="The Armed Conflict Location & Event Data Project (ACLED) \n https://data.humdata.org/")], className = "spann"),
                                       dcc.Dropdown(id="selected-value", multi=True, value=["Senegal"],

                        options=[{"label": "Senegal", "value": "Senegal"},
                                 {"label": "Mali", "value": "Mali"},
                                 {"label": "Nigeria", "value": "Nigeria"},
                                 {"label": "Mauritania", "value": "Mauritania"}]),
                                 dcc.Graph(id="my-graph"),
                                 dcc.RangeSlider(id="year-range", min=1997, max=2019, step=1, value=[1998, 2000],
                                    marks={"1997": str(1997), "1998": str(1998), "1999": str(1999),
                                           "2000": str(2000), "2001": str(2001), "2002": str(2002),
                                           "2003": str(2003), "2004": str(2004), "2005": str(2005),
                                           "2006": str(2006), "2007": str(2007),"2008": str(2008),
                                           "2009": str(2009), "2010": str(2010),"2011": str(2011),
                                           "2012": str(2012), "2013": str(2013),"2014": str(2014),
                                           "2015": str(2015), "2016": str(2016),"2017": str(2017),
                                           "2018": str(2018), "2019": str(2019)})],
                                           className="pretty_container"),

                         #dcc.Graph(id='scatter_graph'),
                         html.Div([

                         dcc.Graph(id='pie_chart'),
                         dcc.Graph(id='DistributionMap'),
                         dcc.Graph(id='heatmap'),
                         html.Div([html.H1('Monthly distribution events of conflict incidences',
                                 style={'textAlign': 'center',
                                        'margin': '5px 0',
                                        'display': 'inline-block',
                                        'fontFamily': 'system-ui'}),
                                        html.Abbr("\uD83D\uDEC8", title="The Armed Conflict Location & Event Data Project (ACLED) \n https://data.humdata.org/")], className = "spann"),
                        dcc.Graph(id='histogram'),
                        ],className="pretty_container" ),
                        html.Div([
                        html.Div([html.H1('Events and fatalities per districts',
                                style={'textAlign': 'center',
                                       'margin': '5px 0',
                                       'display': 'inline-block',
                                       'fontFamily': 'system-ui'}),
                                       html.Abbr("\uD83D\uDEC8", title="The Armed Conflict Location & Event Data Project (ACLED) \n https://data.humdata.org/")], className = "spann"),
                         dcc.Dropdown(id='country_selector', value="Senegal", multi=False, options=[{"label": "Senegal", "value": "Senegal"},
                                  {"label": "Mali", "value": "Mali"},
                                  {"label": "Nigeria", "value": "Nigeria"},
                                  {"label": "Mauritania", "value": "Mauritania"}]), # options=[{'label': k, 'value': k} for k in dictLocation.keys()]),
                         dcc.Dropdown(id='district_selector', value="Dakar"),
                         dcc.Graph(id='Location_Events')], id="wells",
                         className="pretty_container")
                #     ]
                 #),
            ])

    elif tabs_value == '2':
        children = html.Div([
            html.Div([
                html.Div([ html.H1('Food Insecurity Indicator',
                        style={'textAlign': 'center',
                               'margin': '5px 0',
                               'display': 'inline-block',
                               'fontFamily': 'system-ui'}),
                               html.Abbr("\uD83D\uDEC8", title="Food Insecurity Data 2002-2015 \n https://data.humdata.org/")], className = "spann"),
                dcc.Dropdown(id='Food_country_selector', value="Senegal", multi=False, options=[{"label": "Senegal", "value": "Senegal"},
                         {"label": "Mali", "value": "Mali"},
                         {"label": "Nigeria", "value": "Nigeria"},
                         {"label": "Mauritania", "value": "Mauritania"}]),
                dcc.Dropdown(id='Food_Item_Picker', options= item_options_data, value = 'Average dietary energy supply adequacy (percent) (3-year average)' )], id="wells",
                        className="pretty_container"),

            html.Div([
            dcc.Graph(id='Histogramm_FoodInsecurity')
            ])





        ])

    elif tabs_value == '3':
        children = html.Div([
                            html.Div([html.H1('Temperature visualization',
                                    style={'textAlign': 'center',
                                           'margin': '5px 0',
                                           'display': 'inline-block',
                                           'fontFamily': 'system-ui'}),
                                        html.Abbr("\uD83D\uDEC8", title="Google Earth Engine")], className = "spann"),
                                           dcc.Dropdown(id='Water_country_selector', value="Senegal", multi=False, options=[{"label": "Senegal", "value": "Senegal"},
                                                    {"label": "Mali", "value": "Mali"},
                                                    {"label": "Nigeria", "value": "Nigeria"},
                                                    {"label": "Mauritania", "value": "Mauritania"}]),
                            dcc.Graph(id='Temp')],className="pretty_container")


    elif tabs_value == '4':
        children = html.Div([html.Div([html.H1('Water Resources ',
                            style={'textAlign': 'center',
                                   'margin': '5px 0',
                                   'display': 'inline-block',
                                   'fontFamily': 'system-ui'}),
                                html.Abbr("\uD83D\uDEC8", title=" GeoWater Ressources \n https://data.humdata.org/")], className = "spann"),

                                dcc.Dropdown(id='Water_selector', value="1", multi=False, options=[{"label": "June-July 2019", "value": "1"},
                             {"label": "April-May 2019", "value": "2"}]),
                             dcc.Graph(id='WaterPie')],id="wells",
                            className="pretty_container")


    elif tabs_value == '5':
        children = [  html.Iframe(src= f'https://waeldimassi.users.earthengine.app/view/timeseries-animation', style=dict(border=5), width="100%", height="800" ) ]

    elif tabs_value == '6':
        children = [  html.Iframe(src= f'https://waeldimassi.users.earthengine.app/view/timeseries-pixel', style=dict(border=5), width="100%", height="800" ) ]

    elif tabs_value == '7':
        children = [  html.Iframe(src= f'https://ahmedmoussa.users.earthengine.app/view/dashlandcover', style=dict(border=5), width="100%", height="800" ) ]
    elif tabs_value =='8':
        children = [  html.Iframe(src= f'https://waeldimassi.users.earthengine.app/view/clusterclassification', style=dict(border=5), width="100%", height="800" ) ]
    elif tabs_value =='9':
        children = [  html.Iframe(src= f'https://waeldimassi.users.earthengine.app/view/populationsenegal', style=dict(border=5), width="100%", height="800" ) ]
    else:
        children = [
         html.Div([
            html.Div([

            html.Div(html.H3('Study Lakes in Senegal with SentinelHub Images',
                    style={'textAlign': 'center',
                           'margin': '0px 0',
                           'fontFamily': 'system-ui',
                           'background-color': '#FFC000'}),className="pretty_container",style={ 'background-color' : '#FFC000', 'color': 'black'}),
            html.Div(html.Img(src='/assets/SatelliteImage.png',style={
                'height': '75%',
                'width': '75%'
            }), style={'textAlign': 'center'}),]),
            html.Div(html.P('This section will serve as an example of our approach to studying the evolution of water levels in Senegal during a given time interval, including the use of SentinelHub as a satellite images provider to take and download snapshots of specific lakes on a monthly basis. Using the NDVI would be a great asset for the detection pipeline. The API will provide a rolling archive of multi-spectral data, with full resolution preview and time-lapse functionality.'),className="pretty_container",style={ 'background-color' : '#FFFFFF', 'color': 'black'}),

            html.Div(html.H3('Detecting Water Level in each Image',
                    style={'textAlign': 'center',
                           'margin': '4px 0',
                           'fontFamily': 'system-ui',
                           'background-color': '#FFC000'}),className="pretty_container",style={ 'background-color' : '#FFC000', 'color': 'black'}),
            html.Div(html.Img(src='/assets/SavedSatelite.png',style={
                'height': '75%',
                'width': '75%'
            } ), style={'textAlign': 'center'}),
            html.Div(html.P('Use computer vision algorithms to define geometries of the water bodies in each remote sensing image. We start visualising the first few true-color images of the lake in the given time series  — and can see below that some images contain clouds, which poses a challenge to accurate water level detection.'),className="pretty_container",style={ 'background-color' : '#FFFFFF', 'color': 'black'}),

            html.Div(html.H3('Extract Water Level as a Time series',
                    style={'textAlign': 'center',
                           'margin': '4px 0',
                           'fontFamily': 'system-ui',
                           'background-color': '#FFC000'}),className="pretty_container",style={ 'background-color' : '#FFC000', 'color': 'black'}),
            html.Div(html.Img(src='/assets/CloudImage.png' ,style={
                'height': '75%',
                'width': '75%'
            }), style={'textAlign': 'center'}),
            html.Div(html.P('A lot of fluctuations in water levels are detected after applying the algorithms. At the same time, cloud coverage is plotted and shares the same dates as the water level outliers. This represents a shortcoming for the work.'),className="pretty_container",style={ 'background-color' : '#FFFFFF', 'color': 'black'}),

            html.Div(html.H3('Treat Data and Eliminate the Bias',
                    style={'textAlign': 'center',
                           'margin': '4px 0',
                           'fontFamily': 'system-ui',
                           'background-color': '#FFC000'}),className="pretty_container",style={ 'background-color' : '#FFC000', 'color': 'black'}),
            html.Div(html.Img(src='/assets/NoCloudImage.png' ,style={
                'height': '75%',
                'width': '75%'
            }), style={'textAlign': 'center'}),
            html.Div(html.P('The challenge in this phase is to compensate sufficiently for the error caused by cloud interference in the images. Mixing both inputs in a smart algorithm can help reduce the bias.'),className="pretty_container",style={ 'background-color' : '#FFFFFF', 'color': 'black'}),

            html.Div(html.H3('Prediction with SARIMA',
                    style={'textAlign': 'center',
                           'margin': '4px 0',
                           'fontFamily': 'system-ui',
                           'background-color': '#FFC000'}),className="pretty_container",style={ 'background-color' : '#FFC000', 'color': 'black'}),
            html.Div(html.Img(src='/assets/Arima.png' ,style={
                'height': '75%',
                'width': '75%'
            }), style={'textAlign': 'center'}),
            html.Div(html.P('Seasonal Autoregressive Integrated Moving Average (SARIMA, or Seasonal ARIMA), is an extension of ARIMA that explicitly supports univariate time series data with a seasonal component. In this case, SARIMA is the best statistical tool for time series prediction.'),className="pretty_container",style={ 'background-color' : '#FFFFFF', 'color': 'black'}),

            html.Div(html.H3('Train Machine Learning Model: RNN-LSTM',
                    style={'textAlign': 'center',
                           'margin': '4px 0',
                           'fontFamily': 'system-ui',
                           'background-color': '#FFC000'}),className="pretty_container",style={ 'background-color' : '#FFC000', 'color': 'black'}),
            html.Div(html.Img(src='/assets/Lstm.png' ,style={
                'height': '75%',
                'width': '75%'
            }), style={'textAlign': 'center'}),
            html.Div(html.P('Long short-term memory (LSTM) is an artificial recurrent neural network (RNN) architecture used in the field of deep learning. LSTM networks are well-suited to classifying, processing, and making predictions with time series data, since there can be lags of unknown duration between important events in a time series.'),className="pretty_container",style={ 'background-color' : '#FFFFFF', 'color': 'black'})
            ]

                           ,className="pretty_container",style={ 'background-color' : '#FFFFFF'}) ]


    return children



########################################################################
                            #Count_Information#
########################################################################
@app.callback(Output('events_text','children'),[Input('selected_Country', 'value'),Input('year-picker','value')])
def update_events_count(selected, year):
    dfff = df[df.country == (selected)]
    dfff = dfff[dfff.year == (year)]
    return dfff.size

@app.callback(Output('FatalityText','children'),[Input('selected_Country', 'value'),Input('year-picker','value')])
def update_Fatalities_count(selected, year):
    dfff = df[df.country == (selected)]
    dfff = dfff[dfff.year == (year)]
    return dfff[dfff['fatalities']==0].size

@app.callback(Output('noFatalityText','children'),[Input('selected_Country', 'value'),Input('year-picker','value')])
def update_NoFatalities_count(selected, year):
    dfff = df[df.country == (selected)]
    dfff = dfff[dfff.year == (year)]
    return dfff[dfff['fatalities']>0].size


########################################################################
                            #Line_Charts#
########################################################################
@app.callback(
    Output('my-graph', 'figure'),
    [Input('selected-value', 'value'), Input('year-range', 'value')])
def update_figure(selected, year):
    text = {"Senegal": "Senegal", "Mali": "Mali",
            "Nigeria": "Nigeria", "Mauritania": "Mauritania"}
    dff = df[(df["year"] >= year[0]) & (df["year"] <= year[1])]
    trace = []

    dfff = dff[dff.country.isin(selected)]
    #print(dfff.country.unique())
    for cou in dfff.country.unique():
        #dfff = dfff.groupby('date', as_index=False)['fatalities'].sum()
        trace.append(go.Scatter(x=dfff["data"][dfff.country==cou], y=dfff["fatalities"][dfff.country==cou], name=text[cou], mode='lines',
                        marker={'size': 8, "opacity": 0.6, "line": {'width': 0.5}}, ))

    """for type in selected:
        dff= dff[dff["country"]==type]
        trace.append(go.Scatter(x=dff["data"], y=dff["fatalities"], name=text[type], mode='lines',
                                marker={'size': 8, "opacity": 0.6, "line": {'width': 0.5}}, ))
    """
    df_total = dfff.groupby('data',as_index=False)['fatalities'].sum()
    trace.append(go.Scatter(x=df_total.data, y=df_total.fatalities, name="Total", mode='lines',
                    marker={'size': 8, "opacity": 0.6, "line": {'width': 0.5}}, ))
    return {"data": trace,
            "layout": go.Layout(colorway=['#fdae61', '#abd9e9', '#2c7bb6','#66ff66','#ff66cc'],
                                yaxis={"title": "Fatalilities"}, xaxis={"title": "Data"})}
########################################################################
                            #scatter_graph#
########################################################################
@app.callback(Output('scatter_graph', 'figure'),[Input('year-picker','value')])
def update_scatter_figure(selected_year):
    filtered_df = df[df['year']==selected_year]
    traces = []
    for continent_name in filtered_df['country'].unique():
        df_by_continent = filtered_df[filtered_df['country']==continent_name]
        traces.append(go.Scatter(
            x = df_by_continent['fatalities'],
            y = df_by_continent['event_type'],
            mode = 'markers',
            opacity=0.7,
            marker = {'size' : 15},
            name= continent_name
        ))
    return {'data': traces , 'layout':go.Layout(title='My Plot', xaxis={'title':'fatalities Count'},yaxis={'title':'Event type'})}

########################################################################
                            #PieChart#
########################################################################
@app.callback(
dash.dependencies.Output("pie_chart", "figure"),
[Input('selected_Country', 'value'),Input('year-picker','value')])
def update_graph(country,selected_year):
    dff = df[df.country == country]
    y = dff[dff["year"] == selected_year]["event_type"].value_counts()
    return {
        "data": [go.Pie(labels=df["event_type"].unique().tolist(), values=y,hole=0.3,
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='value'),],
        "layout": go.Layout(title=f"Events Reported per year", margin={"l": 100, "r": 300, },
                            legend={"x": 1, "y": 0.7})}
#######################################################################
                            #MapBox#
#######################################################################
@app.callback(Output('DistributionMap', 'figure'),[Input('year-picker','value')])
def make_main_figure(selected_year):
    #dff = df(df, well_statuses, well_types, year_slider)
    df1 = df[df['year']==selected_year]
    traces = []
    for dff in df1.groupby('year'):
        trace = dict(
            type='scattermapbox',
            lon=dff[1]['longitude'],
            lat=dff[1]['latitude'],
            ids = dff[1]['location'],
            #text="rrrr",
            textposition = "middle center",

            title ='title',
            #hovertemplate ="district: %{dff[1]['location']}",
            #hoverinfo = 'text + name',
            customdata=dff[1]['fatalities'],
            name= 'Event',#dff[1]['location'],
            legend= 'Event',
            legendgroup ='fofo',

            showlegend = True,
            #color_continuous_scale=px.colors.cyclical.IceFire,
            marker=dict(
                size=12,
                opacity=0.6,
            ),
            text = dff[1]['location'],
            hoverinfo = "lat+lat+text",
            hovertemplate = "District: %{text} <br>Fatalities: %{customdata}",
            #hovertext = "all", #dff[1]['location']+dff[1]['fatalities'],
        )
        traces.append(trace)
    figure = dict(data=traces, layout=layout1)
    return figure
"""
    fig = px.scatter_mapbox(df1, lat=df1[1]['latitude'], lon=df1[1]['longitude'],color=df1[1]['fatalities'], size=df1[1]['fatalities'],
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
    return fig
    #choropleth MAp
"""
"""
    dr = df.groupby(['iso','year'],as_index = False).sum()
    figure = px.choropleth(dr, locations='iso', color="fatalities", hover_name="Unnamed: 0", animation_frame="year", range_color=[0,30], scope='africa',)
    return figure
"""
########################################################################
                            #DensityMap#
########################################################################
@app.callback(Output('heatmap', 'figure'),[Input('year-picker','value')])
def make_main_figure(selected_year):
    #dff = df(df, well_statuses, well_types, year_slider)
    df1 = df[df['year']==selected_year]
    traces = []
    home_lat = df1['latitude']
    home_lon = df1['longitude']

    data = [go.Densitymapbox(lat = home_lat, lon = home_lon,
                         z = df1['fatalities'], colorscale= [[0, 'rgb(255,255,255)'], [1, 'rgb(182,182,4)']]), #"peach"),
                         ]

    figure = dict(data=data, layout=layout2)
    return figure
########################################################################
                            #Histogramm#
########################################################################
@app.callback(
    Output("histogram", "figure"),
    [Input('year-picker','value')],
)
def update_histogram(selected_year):
    dff = df[df['year']==selected_year]

    fatalities_count = dff[['fatalities','month']].groupby('month', as_index=False).sum()
    #monthPicked = fatalities_count.index.tolist()

    layout = go.Layout(
        #legend=dict(font=dict(size=19), orientation='h'),
        title='Distribution Map',
        bargap=0.01,
        bargroupgap=0,
        barmode="group",
        margin=go.layout.Margin(l=10, r=0, t=0, b=50),
        #marker= dict(colorscale = [[0, 'rgb(255,255,255)'], [1, 'rgb(182,182,4)']]),
        #marker_color='lightslategrey',
        #colorscale = "peach",
        showlegend=True,
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        dragmode="select",
        font=dict(color="black"),
        xaxis=dict(
            range=[-0.5, 12],
            showgrid=False,
            nticks=25,
            fixedrange=True,

        ),
        yaxis=dict(
            range=[0, fatalities_count.fatalities.max()],
            showticklabels=False,
            showgrid=False,
            fixedrange=True,
            rangemode="nonnegative",
            zeroline=False,
        )
    )

    return go.Figure(
        data=[
            go.Bar(x= months , y=fatalities_count.fatalities, marker=dict(color='#2d4fc2'), hoverinfo="y"),
            go.Scatter(
                opacity=1,
                x=months,
                y=fatalities_count.fatalities,
                hoverinfo="none",
                mode="markers",
                marker=dict(color="rgb(0, 134, 244, 0)", symbol="square", size=12),
                visible=False,
                ),
        ],
        layout=layout,
    )
########################################################################
                            #Country_District_Selector#
########################################################################
@app.callback(
    Output("district_selector", "options"),
    [Input('country_selector','value')],
)
def update_District_Selector_options(selected):
    #dff = df[df['country']==selected]
    #print(selected)
    return [{'label': i, 'value': i} for i in dictLocation[selected]]

@app.callback(
Output('district_selector','value'),
[Input('district_selector', 'options')]
)
def update_District_Selector_options(available_options):
    list = []
    #print(available_options[0]['value'])
    return available_options[0]['value']

########################################################################
                            #Location_Events#
########################################################################
@app.callback(
Output("Location_Events","figure"),
[Input('district_selector', 'value')]
)
def Update_district_selector(selected_Location):
    dff = df[df['location']==selected_Location]
    x = dff.data.unique()
    y = dff.fatalities

    fig = go.Figure()
    fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="Number of  Events",  marker=dict(color='#2d4fc2')))
    fig.add_trace(go.Histogram(histfunc="sum", y=y, x=x, name="Number of fatalities", marker=dict(color='#b6b604')))

    return fig

########################################################################
                            #Histogramm_FoodInsecurity#
########################################################################
@app.callback(
    Output("Histogramm_FoodInsecurity", "figure"),
    [Input('Food_country_selector','value'), Input('Food_Item_Picker', 'value')],
)
def update_histogram_food (selected_country, item):
    data_hist = data[data['Area']==selected_country]
    #print(selected_country , item)
    data_hist = data_hist[data_hist['Item']==item]
    #print(data_hist.Value.tolist()[1])
    #monthPicked = fatalities_count.index.tolist()

    layout = go.Layout(
        bargap=0.01,
        bargroupgap=0,
        barmode="group",
        margin=go.layout.Margin(l=10, r=0, t=0, b=50),
        showlegend=False,
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        dragmode="select",
        font=dict(color="white"),
        xaxis=dict(
            range=[0, 13],
            showgrid=False,
            nticks=20,
            fixedrange=True,

        ),
        yaxis=dict(
            range=[0, data_hist.Value.max()+5],
            showticklabels=False,
            showgrid=False,
            fixedrange=True,
            rangemode="nonnegative",
            zeroline=False,
        )
    )

    return go.Figure (go.Bar(x= data_hist.Year , y=data_hist.Value, marker=dict(color='#2d4fc2'), hoverinfo="y"))
    """return go.Figure(
        data=[
            go.Bar(x= data_hist.Year , y=data_hist.Value, marker=dict(color=colorVal), hoverinfo="y"),
            go.Scatter(
                opacity=1,
                x=data_hist.Year,
                y=data_hist.Value,
                hoverinfo="none",
                mode="markers",
                marker=dict(color="rgb(66, 134, 244, 0)", symbol="square", size=12),
                visible=True,
                ),
        ],
        layout=layout,
    )"""

########################################################################
                            #Water Resources#
########################################################################
@app.callback(
    Output("WaterPie", "figure"),
    [Input('Water_selector','value')]
)
def update_water_graphs (selected_pays):

    df1 = []
    color = []
    if(selected_pays == "1"):
        df1 =  dt_june
        color = "blue"
    elif(selected_pays == "2"):
        df1 =  dt_april #df[df['year']==selected_year]
        color = "red"
    fig = px.scatter_mapbox(df1, lat="lon", lon="lat", hover_data=['Concentration','pasture_availability', 'water_availability', 'water_type'],
                        color_discrete_sequence=[color], zoom=5)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(hovermode="closest")
    fig.update_layout(plot_bgcolor="#F9F9F9")
    fig.update_layout(paper_bgcolor="#F9F9F9")

    return fig


########################################################################
                            #Temp#
########################################################################
@app.callback(Output('Temp','figure'),[Input('Water_country_selector','value')])
def Plot_Temp (country_selector):

    df = data_temp[data_temp['country']== country_selector]
    # Create figure
    #print(country_selector)
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=list(df.date), y=list(df.value)))
    # Set title
    fig.update_layout(
        title_text="Time series with range slider and selectors"
    )
    # Add range slider
    fig.update_layout(
        xaxis=go.layout.XAxis(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="YTD",
                         step="year",
                         stepmode="todate"),
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    return fig
########################################################################
if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
