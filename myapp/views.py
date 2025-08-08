from django.shortcuts import render
import requests


def home(request):
    """
    Renders the home page with weather data.

    This view fetches weather data from the OpenWeatherMap API and
    passes it to the HTML template for display.
    
    NOTE: You need to replace 'YOUR_API_KEY' with a valid key and
    the 'city' variable with your desired location.
    """
    api_key = '17b97b0a814a847d66ee215677cccf43' # Replace with your actual API key
    city = 'London' # Replace with a city name you want to monitor
    
    # Construct the API request URL
    # We use f-strings for a clean way to embed variables
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    weather_data = None
    error_message = None
    
    try:
        # Make the HTTP GET request to the API
        response = requests.get(api_url)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        
        # Parse the JSON response
        data = response.json()
        
        # Check if the API call was successful
        if data.get('cod') == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            error_message = f"Error fetching weather data: {data.get('message', 'Unknown error')}"
            
    except requests.exceptions.RequestException as e:
        error_message = f"An error occurred: {e}"
    except (KeyError, IndexError) as e:
        error_message = f"Error parsing API response: Invalid data format. {e}"

    # Prepare the context dictionary to pass to the template
    context = {
        'weather': weather_data,
        'error': error_message,
    }
    
    # Render the HTML template with the context data
    return render(request, 'index.html', context)