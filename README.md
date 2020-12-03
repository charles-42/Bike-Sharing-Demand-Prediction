# 🚴 Bike Sharing Demand Prediction 🚴

Try out the project here -- https://bike-demand-prediction.herokuapp.com/
<br>
*(Please wait for 10-12 seconds for app to load initially)*

![](https://knowledge.wharton.upenn.edu/wp-content/uploads/2017/09/092817_chinabikeshare.jpg)

A Kaggle competition turned project, this project is divided into 3 parts :

1. Exploratory Data Analysis - [check here](https://nbviewer.jupyter.org/github/SarthakRana/Bike-Sharing-Demand-Prediction/blob/master/bike_sharing_EDA_Part1.ipynb)<br>
2. Data Preparation - [check here](https://nbviewer.jupyter.org/github/SarthakRana/Bike-Sharing-Demand-Prediction/blob/master/bike_sharing_data_preparation_Part2.ipynb)<br>
3. Modelling - [check here](https://nbviewer.jupyter.org/github/SarthakRana/Bike-Sharing-Demand-Prediction/blob/master/bike_sharing_modelling_Part3.ipynb)<br>

Bike sharing systems are a means of renting bicycles where the process of obtaining membership, rental, and bike return is automated via a network of kiosk locations 
throughout a city. Using these systems, people are able rent a bike from a one location and return it to a different place on an as-needed basis.

## 1. Prerequisites

You need to have the following dependecies before running the project:

- pandas `pip install pandas`
- numpy `pip install numpy`
- scipy `pip install scipy`
- scikit learn `pip install scikit-learn`
- streamlit `pip install streamlit`
- matplotlib `pip install matplotlib`
- seaborn `pip install seaborn`
-

## 2. Installing

Use the package manager to install __Bike Sharing Demand Prediction__ project

You can clone the repo :
```
gitclone https://github.com/SarthakRana/Bike-Sharing-Demand-Prediction.git
```

GitHub CLI :
```
gh repo clone SarthakRana/Bike-Sharing-Demand-Prediction
```

You can also download the ZIP of this project and place on your working directory.

## 3. Usage

### 3.1 Web App

1. Install all dependencies mentioned in __Prerequisites__.
2. Open CLI/prompt and make sure Streamlit is installed by running the command `streamlit --version`. You should see something like this : `Streamlit, version 0.67.1`.
3. Do this for all other dependencies as well just to make sure everything is in right place and you are good to go.
4. Go to your working directory(where you have placed the .py file and other components) and open CLI/prompt there.
5. Type in the following command and press Enter :<br>
   `streamlit run app.py`<br>
   Please wait for 5-10 seconds for command to run.
6. A browser widow should open up with the app running.
7. Enjoy :)

### 3.2 Project

1. Install all dependencies mentioned in __Prerequisites__.
2. Place the contents of project folder in your working directory.
3. Simply open Jupyter Notebooks/Jupyter Lab and run the .ipynb files.
4. All project related files like models, scalers and encoders will be saved in the same directory as you run the files.

## 4. Deployment

For deployment on Heroku, we need to make 3 extra files.

### 4.1 Procfile

Create a procfile and copy the below code :
```
web: sh setup.sh && streamlit run app.py
```
### 4.2 requirements.txt

Run the below command to prepare the requirements.txt

```
pip freeze > requirements.txt
```

NOTE : I personally don't use the freeeze command as it creates some version conflicts while deploying on Heroku. I prefer writing doing the required packages name in the txt file. Heroku automatically makes use of the latest package version available while deploying.

### 4.3 setup.sh

Create a file `setup.sh` and copy the below code:

```
mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

### 4.4 Full deployment

NOTE : To deploy on Heroku, you can either use Heroku CLI or Heroku Dashboard.
You can follow the rest of the steps from here : https://www.youtube.com/watch?v=IWWu9M-aisA

## 5. Roadmap

See the open issues for a list of proposed features (and known issues)(if any).
If your issue is not listed in the already open issues, you can open up a new one.

## 6. Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

  1. Fork the Project.
  2. Create your Feature Branch.
  3. Commit your Changes.
  4. Push to the Branch.
  5. Open a Pull Request.

## 7. Authors

NOTE : Your name will be added here if I merge your pull request.

Sarthak Rana (https://www.linkedin.com/in/sarthakrana/)
