from flask import Flask, request, render_template
import requests

app = Flask(__name__)
  
@app.route('/', methods =["GET", "POST"])
def index(): 
    weatherData = ''
    error = 0
    cityName = ''
    if request.method == "POST":       
        cityName = request.form.get("cityName")  
        if cityName:
            weatherApiKey = '2638e6daeb0617d64fe3082444b1b336'
            url = "https://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid=" + weatherApiKey
            weatherData = requests.get(url).json()
        else:
            error = 1    
    return render_template('index.html', data = weatherData, cityName = cityName, error = error)
if __name__ == "__main__":
    app.run()