# Agritech Project: Crop Monitoring System

This is a foundational Django web application designed to serve as a basic crop monitoring dashboard. The project demonstrates integration with a third-party API to fetch and display real-time weather data.

## Features

* **Weather API Integration**: Fetches current weather data from the OpenWeatherMap API.

* **Dynamic Frontend**: Displays weather information (city, temperature, conditions, icon) using a Django template.

* **Error Handling**: Includes basic error handling for API request failures and data parsing issues.

## Prerequisites

Ensure you have Python installed. The following libraries are required:

* `Django`

* `requests`

You can install them using `pip`:

pip install Django requests


## Configuration

1.  **OpenWeatherMap API Key**: Obtain a free API key from the [OpenWeatherMap website](https://openweathermap.org/api).

2.  **API Key Integration**: Open the `views.py` file and replace the placeholder with your actual API key. You can also modify the `city` variable to change the location.

api_key = 'YOUR_API_KEY' # Replace with your actual API key
city = 'London' # Replace with a city name you want to monitor


## Running the Project

1.  **Start the Development Server**: From the project's root directory, execute the following command:

 ```
 python manage.py runserver
 ```

2.  **View the Application**: Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Contributing

Pull requests and issues are welcome. For major changes, please open an issue first to discuss what you would like to change.
