from django.shortcuts import render
from django.views.generic import TemplateView
import json
import requests

def home_view(request):
    template_name = 'lookup/home.html'
    if request.method == 'POST':
        zip_code = request.POST.get('q')
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zip_code+"&distance=5&API_KEY=1B339235-1EE3-4B1D-BABF-65B64CAA7C09")

        try:
            api = json.loads(api_request.content)
            if api[0]["Category"]["Name"] == 'Good':
                description = "Good (0 - 50): <br>Air quality is considered satisfactory, and air pollution poses little or no risk."
                bg_color = "Good"

            elif api[0]["Category"]["Name"] == 'Moderate':
                description = "Moderate (51 - 100): <br>"
                bg_color = "Moderate"

            elif api[0]["Category"]["Name"] == 'Unhealthy for Sensitive Groups':
                description = "Unhealthy for Sensitive Groups (101 - 150): <br>Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
                bg_color = "Groups"

            elif api[0]["Category"]["Name"] == 'Unhealthy':
                description = "Unhealthy (151 - 200): <br>Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
                bg_color = "Unhealthy"

            elif api[0]["Category"]["Name"] == 'Very Unhealthy':
                description = "Very Unhealthy (201 - 300): <br>Health alert: everyone may experience more serious health effects."
                bg_color = "Very"

            elif api[0]["Category"]["Name"] == 'Hazardous':
                description = "Hazardous (301 - 500): <br>Health warnings of emergency conditions. The entire population is more likely to be affected."
                bg_color = "Hazardous"

            else:
                description= ""
                bg_color= ""

        except Exception as e :

            api = "error"
            description= ""
            bg_color= ""


        template_name = 'lookup/home.html'
        context = {'api':api,
                    "des":description,
                    'bg_color':bg_color}

        return render(request, template_name, context)

    else:
        return render(request, template_name)



class AboutView(TemplateView):
    template_name = 'lookup/about.html'
