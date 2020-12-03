import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

def encodeFeature(feature, user_input):
    if feature == 'season':
        # Load season encoder    
        season_enc = open("season_ohe_encoder.pkl", "rb")
        season_enc = pickle.load(season_enc)
        season_value = user_input['season'].values
        season_value = season_value.reshape(1,1)
        season_value = season_enc.transform(season_value)
        season_df = pd.DataFrame(season_value)
        return season_df
    
    else:
        # Load weather encoder    
        weather_enc = open("weather_ohe_encoder.pkl", "rb")
        weather_enc = pickle.load(weather_enc)
        weather_value = user_input['weather'].values
        weather_value = weather_value.reshape(1,1)
        weather_value = weather_enc.transform(weather_value)
        weather_df = pd.DataFrame(weather_value)
        return weather_df

def scaleData(user_data):
    # Load saved scaler
    scaler = open("scaler.pkl", "rb")
    scaler = pickle.load(scaler)
    user_data = scaler.transform(user_data)
    return user_data


def process_data(date, time, day, weather, temperature, humidity, windspeed):
    '''
    Here I will prepare data in format accepted by our model.
    This will include :-
    1. Feature Extraction. (month and hour)
    2. One hot encoding.(season and weather)
    3. Scaling data
    4. Converting to dataframe.
    '''
   
    # Extract hour and month from date and time
    date, time = str(date), str(time)
    month = date.split('-')[1]
    hour = time.split(':')[0]
    
    # Map weather to numbers
    weather_dict = {
        "Clear/Few clouds" : 1,
        "Mist/Cloudy" : 2,
        "Light Rain/Light Snow/Scattered clouds" : 3,
        "Heavy Rain/Snowfall/Foggy/Thunderstorm" : 4
        }
    weather = weather_dict[weather]
    
    # Prepare 'holiday' and 'workingday' features
    if day == 'Holiday':
        holiday = 1
        workingday = 0
    elif day == 'Working day':
        holiday = 0
        workingday = 1
    else:
        holiday = 0
        workingday = 0
    
    # Deduce `season` from `month` feature
    if ((int(month) >= 1) & (int(month) <= 3)):
        season = 'Spring'
    elif ((int(month) > 3) & (int(month) <= 6)):
        season = 'Summer'
    elif ((int(month) > 6) & (int(month) <= 9)):
        season = 'Fall'
    else:
        season = 'Winter'
    
    # Map season to numbers
    season_dict = {
        "Spring" : 1,
        "Summer" : 2,
        "Fall" : 3,
        "Winter" : 4
        }
    season = season_dict[season]
    
     # Prepare user input dataframe using user input values
    user_input_df = pd.DataFrame({'hour': [hour],
                               'month' :[month],
                               'holiday' : [holiday],
                               'workingday' : [workingday],
                               'temp' : [temperature],
                               'humidity' : [humidity],
                               'windspeed' : [windspeed],
                               'season' : [season],
                               'weather' : [weather]
                               })
    
    
    '''
    Prepare Season Dataframe which we be appended with original user input df. We will:
        1. Encode season feature.
        2. Rename columns to match with training data column names.
        3. Drop first feature to avoid dummy variable trap
        4. Finally, append season and weather df to original user df. 
    ''' 
    # One hot encode season
    season_df = encodeFeature('season', user_input_df)
    # Rename df columns
    seasons = ['spring', 'summer', 'fall', 'winter']
    season_df_cols = ['season_' + x for x in seasons]
    season_df.columns = season_df_cols
    # Drop first column
    season_df = season_df.iloc[:, 1:]
    
    
    # One hot encode weather
    weather_df = encodeFeature('weather', user_input_df)
    # Rename df columns
    weathers = ['clear', 'mist', 'light_rain', 'heavy_rain']
    weather_df_cols = ['weather_' + x for x in weathers]
    weather_df.columns = weather_df_cols
    # Drop first column
    weather_df = weather_df.iloc[:, 1:]
    
    
    # Combine season and weather dataframe to original dataframe and drop season and weather features
    frames = [user_input_df, season_df, weather_df]
    user_data = pd.concat(frames, axis=1)
    del user_data['season']
    del user_data['weather']
    
    # Scale data
    scaled_user_data = scaleData(user_data)
        
    # Get predicted results
    prediction = predictRentals(scaled_user_data)
    
    return prediction
        
    
def predictRentals(user_data):
    # Load model
    savedmodel = open('model_approach_1.pkl', 'rb')
    model = pickle.load(savedmodel)
    savedmodel.close()
    
    prediction = int(model.predict(user_data))
    
    return prediction