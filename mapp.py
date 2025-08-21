import requests
import folium
import json
lat,lon=12.9716, 77.5946
url="https://nominatim.openstreetmap.org/search"
stuff={
    "q":"hospital",
    "viewbox":f"{lon-1},{lat+1},{lon+1},{lat-1}",
    "bounded":1,
    "format":"json"

}
headers={
    "User-Agent":"MyPythonApp/1.0 (aryan.kumar011104@gmail.com)"
}
response=requests.get(url,params=stuff,headers=headers)
data=response.json()
m=folium.Map(location=[lat,lon],zoom_start=12)
for places in data:
    folium.Marker([float(places["lat"]),float(places["lon"])],popup=places["display_name"]).add_to(m)
m.save("marer.html")