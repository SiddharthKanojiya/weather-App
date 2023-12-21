from django.shortcuts import render
import json 
# urllib.request to make a request to api 
import urllib.request 
  
# Create your views here.
def index(request):
    if request.method == 'POST': 
        city = request.POST.get('city')
        cc = request.POST.get('cc') 
        statecode = request.POST.get('statecode') 
        lon = request.POST.get('longitude') 
        lat = request.POST.get('latitude')
        """print("problem") 
        print(type(city),cc,statecode,lon,lat)"""
        if city:
            #print("ok")
            if cc and statecode:
                #print("done")
                source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q={},{},{}&APPID=2cad20d973f861a98b4a1f8fe0ec00c5'.format(city,statecode,cc)).read() 
            else:
                source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=2cad20d973f861a98b4a1f8fe0ec00c5'.format(city)).read() 
        else:
            source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID=2cad20d973f861a98b4a1f8fe0ec00c5'.format(lat,lon)).read() 
            print(lat,lon)

        
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API 
        #https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=2cad20d973f861a98b4a1f8fe0ec00c5
  
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
        print(source)
        # data for variable list_of_data 
        """"country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), """
        context = { 
            "url":str('http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID=2cad20d973f861a98b4a1f8fe0ec00c5'.format(lat,lon)),
            "name":str(list_of_data['name']),  
            "latitude":str(list_of_data['coord']['lat']),
            "longitude":str(list_of_data['coord']['lon']),
           
            "weathermain":str(list_of_data['weather'][0]['main']),
            "weatherdesc":str(list_of_data['weather'][0]['description']),

            "maintemp":str(list_of_data['main']['temp']),
            "tempmin":str(list_of_data['main']['temp_min']),
            "tempmax":str(list_of_data['main']['temp_max']),
            "pressure":str(list_of_data['main']['pressure']),
            "humidity":str(list_of_data['main']['humidity']),
            
            #"sealvl":str(list_of_data['main']['sea_level']),
            #"groundlvl":str(list_of_data['main']['grnd_level']),
            "visibility":str(list_of_data['visibility']),
            "windspeed":str(list_of_data['wind']['speed']),
            "winddeg":str(list_of_data['wind']['deg']),
            "windgust":str(list_of_data['wind']['gust']),
            "clouds":str(list_of_data['clouds']['all']),
            #"rain":str(list_of_data['rain']['1h']),
            #"snow":str(list_of_data['snow']['1h']),
            "dt":str(list_of_data['dt']),
            #"sysmsg":str(list_of_data['sys']['message']),
            "country":str(list_of_data['sys']['country']),
            "sunrise":str(list_of_data['sys']['sunrise']),
            "sunset":str(list_of_data['sys']['sunset']),
            "timezone":str(list_of_data['timezone']),
            
        } 
        if 'sea_level' in list_of_data['main']:
            context["sealvl"]=str(list_of_data['main']['sea_level'])
            
        if 'grnd_level' in list_of_data['main']:
            context["groundlvl"]=str(list_of_data['main']['grnd_level'])
        if 'rain' in list_of_data and '1h' in list_of_data['rain']:
            context["rain"]=str(list_of_data['rain']['1h'])
        if 'snow' in list_of_data and '1h' in list_of_data['snow']:
            context["snow"]=str(list_of_data['snow']['1h'])
        
        print(context) 
    else: 
        context ={} 
    #return render(request, "main/index.html", data)
    return render(request,"weatherapp/index.html",context=context)

def forecast(request):
    if request.method == 'POST': 
        city = request.POST.get('city')
        cc = request.POST.get('cc') 
        statecode = request.POST.get('statecode') 
        lon = request.POST.get('longitude') 
        lat = request.POST.get('latitude')
        """print("problem") 
        print(type(city),cc,statecode,lon,lat)"""
        if city:
            #print("ok")
            if cc and statecode:
                #print("done")
                source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/forecast?q={},{},{}&APPID=2cad20d973f861a98b4a1f8fe0ec00c5'.format(city,statecode,cc)).read() 
            else:
                source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/forecast?q={}&APPID=2cad20d973f861a98b4a1f8fe0ec00c5'.format(city)).read() 
        else:
            source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&APPID=2cad20d973f861a98b4a1f8fe0ec00c5'.format(lat,lon)).read() 
            print(lat,lon)

        
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API 
        #https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=2cad20d973f861a98b4a1f8fe0ec00c5
  
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
        #print(source)
        # data for variable list_of_data 
        """"country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), """
        predict=[]
        for data in list_of_data['list']:
            d={
                "maintemp":str(data['main']['temp']),
                "tempmin":str(data['main']['temp_min']),
                "tempmax":str(data['main']['temp_max']),
                "pressure":str(data['main']['pressure']),
                "humidity":str(data['main']['humidity']),
                "sea_level":str(data['main']['sea_level']),
                "grnd_level":str(data['main']['grnd_level']),
                "weathermain":str(data['weather'][0]['main']),
                "weatherdesc":str(data['weather'][0]['description']),
                "clouds":str(data['clouds']['all']),
                "visibility":str(data['visibility']),
                "windspeed":str(data['wind']['speed']),
                "winddeg":str(data['wind']['deg']),
                "windgust":str(data['wind']['gust']),
                "date":str(data['dt_txt'])
            }
            predict.append(d)
            
            
            
        context={"ans":predict}
        #print(context) 
    else: 
        context ={} 
    #return render(request, "main/index.html", data)
    return render(request,"weatherapp/forecast.html",context=context)