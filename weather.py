import requests,os,json,time,math
from datetime import datetime

def get_time():
    format_time = datetime.now()
    date = format_time.strftime('%d/%m/%Y')
    current_time = format_time.strftime('%H:%M:%S')
    return date,current_time

def return_main():
    times = 0
    print("\nYou will be directed to the main menu!")
    time.sleep(1)
    os.system('clear')
    for x in range(4):
        times += 1
        print("Returning to \u001b[33m\u001b[1mPlay2Day!\u001b[0m!\n\n" +"." * times)
        time.sleep(1)
        os.system('clear')

def info():
    regions = []
    lat = []
    lon = []
    locations = {}

    # place = 0

    # ip = f"https://ipapi.co/json/"
    # response = requests.get(ip)
    # place = response.json()

    api_key = "0ff25058ab7c4eb7943b6f129e7ce00c"
    ip = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}"
    response = requests.get(ip)
    place = response.json()


    current_city = place["city"]
    current_lat = float((place["latitude"]))
    current_lon = float(place["longitude"])
    # current_city = "Lelystad"
    # current_lat = 51.9627
    # current_lon = 6.2603

    weather = "https://data.buienradar.nl//2.0/feed/json"
    response1 = requests.get(weather)
    response_data = response1.json()

    for i in response_data['actual']['stationmeasurements']:
        if i["regio"] in regions:
            continue
        regions.append(i["regio"])
    
    for i in response_data['actual']['stationmeasurements']:
        lat.append(i["lat"])
        lon.append(i["lon"])
        
    for i in range(len(regions)):
        locations[regions[i]] = lat[i], lon[i]

    return response_data, regions, current_city, current_lat, current_lon, locations

def region_names():
    
    regions = info()[1]
    regions.sort()
    stations1 = []
    stations2 = []
    stations3 = []
    stations4 = []
    stations5 = []
    quarter_stations = int(len(regions)/4)
    
    os.system("clear")

    # print(f"{get_time()[0]} {get_time()[1]} \n")
    for i in range(0,quarter_stations):
        stations1.append(regions[i])
    for i in range(quarter_stations,quarter_stations*2):
        stations2.append(regions[i])
    for i in range(quarter_stations*2,quarter_stations*3):
        stations3.append(regions[i])
    for i in range(quarter_stations*3,len(regions)):
        if len(stations4) == len(stations3):
            stations5.append(regions[i])
            continue
        stations4.append(regions[i])
    rijen = []
    print("Every region you can choose from:")
    for a,b,c,d in zip (stations1,stations2,stations3,stations4):
        rijen.append(f"{a:20} | {b:20} | {c:20} | {d:20}")
    for i in range(len(stations5)):
        rijen[i] = (f"{rijen[i]}| {stations5[i]}")
    for i in rijen:
        print (i)
    
def choose_region():
    while True:
        regions = info()[1]
        choose = input("\nWhat region would you like to check the weather on?").capitalize()
        if choose in regions:
            break
        os.system("clear")
        region_names()
        print("\n\u001b[31mThis was not a valid answer\u001b[0m")
    return choose
    
def region_weather(region_chosen):

    all_data = info()[0]
    for i in all_data['actual']['stationmeasurements']:
        if region_chosen == i["regio"]:
            try:
                temperature = i['temperature']
                return temperature
            except ValueError:
                continue

""" #1 degree = 111 km NS, 68 km EW (the proportion is 0.61, the cosine of the latitude)
#https://www.mapsofworld.com/lat_long/netherlands-lat-long.html """
def euclidean_distance(lat1, lon1, lat2, lon2):

    lat_diff = lat2 - lat1
    lon_diff = lon2 - lon1
    
    lat_km = lat_diff * 111
    lon_km = lon_diff * 68

    return math.sqrt(lat_km**2 + lon_km**2)

def closest_location():

    current_lat = info()[3]
    current_lon = info()[4]
    locations = info()[5]
    min_distance = float('inf')

    for location, (lat, lon) in locations.items():
        distance = euclidean_distance(current_lat, current_lon, lat, lon)
        if distance < min_distance:
            min_distance = distance
            closest_region = location

    return closest_region, min_distance

def current_weather(closest_region):
    all_data = info()[0]
    for i in all_data['actual']['stationmeasurements']:
        if closest_region == i["regio"]:
            try:
                temperature = i['temperature']
                return temperature
            except ValueError:
                continue

def what_to_wear(city, temp):
    os.system("clear")
    print(f"\u001b[35mYou are in {city} right now and the temperature is {temp} degrees Celcius")
    if temp>40:
        print("Do not go outside today...\u001b[0m\n")
    elif 30<temp<40:
        print("Its burning hot today. Be prepaired to sweat if you go out today. You should definitely put on sunscreen!!\u001b[0m\n")
    elif 16<temp<30:
        print("Pretty good weather today. Ur good to wear a shirt!!\u001b[0m\n")
    elif 10<temp <16:
        print("It's going to be abit cold. It's reccomended to wear a jacket or zip hoodie!\u001b[0m\n")
    elif 0<temp<10:
        print("It's becomming pretty cold. Think it's time to wear that winter coat!\u001b[0m\n")
    else:
        print("Just stay cozy at home...\u001b[0m\n")

def main_weather():

    os.system("clear")
    while True:
        print(f"""{get_time()[0]} {get_time()[1]}
\u001b[35m  ________                                __  __                                 
 /_  __/ /_  ___     _      _____  ____ _/ /_/ /_  ___  _____   ____ _____  ____ 
  / / / __ \/ _ \   | | /| / / _ \/ __ `/ __/ __ \/ _ \/ ___/  / __ `/ __ \/ __ \\
 / / / / / /  __/   | |/ |/ /  __/ /_/ / /_/ / / /  __/ /     / /_/ / /_/ / /_/ /
/_/ /_/ /_/\___/    |__/|__/\___/\__,_/\__/_/ /_/\___/_/      \__,_/ .___/ .___/ 
                                                                  /_/   /_/ \u001b[0m
Welcome to '\u001b[45mThe weather app\u001b[0m'
              
(1) Get temperature in location closest to you
(2) Get temperature in chosen location
(3) What do I have to wear today?
(4) Get summary weather report
""")
        choice = input("What would you like to do (press q to quit)? ")
        os.system("clear")
        if choice == "q":
            return_main()
            return
        try:
            choice = int(choice)
        except ValueError:
            print("\u001b[31mThis was not a valid answer.\u001b[0m")
            continue
        if choice>4 or choice<1:
            print("\u001b[31mPlease give a corresponding number.\u001b[0m")
        if choice == 1:
            closest_region = closest_location()[0]
            min_distance = closest_location()[1]
            current_city = f"{info()[2]}"
            print(f"""\u001b[35mYou are now in the city: {current_city}.
The closest city is {closest_region} and is {min_distance:.2f} KM away.
The temperature in that city is {current_weather(closest_region)} degrees Celcius.\u001b[0m\n""")
        elif choice == 2:
            region_names()
            region_chosen = choose_region()
            os.system("clear")
            print(f"\u001b[35mThe temperature in {region_chosen} right now is {region_weather(region_chosen)} degrees Celcius.\u001b[0m\n")
        elif choice == 3:
            city = f"{info()[2]}"
            closest_region = closest_location()[0]
            temp = current_weather(closest_region)
            what_to_wear(city, temp)
        elif choice == 4:
            weatherreport = info()[0]["forecast"]["weatherreport"]
            date = weatherreport["published"]
            print(f"\u001b[35m This report was published on {date.split("T")[0]} at {date.split("T")[1]}\n {weatherreport["summary"]}\n\u001b[0m")

if __name__ == "__main__":
    main_weather()