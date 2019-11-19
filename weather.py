# importing the request and json module
import requests,json
# requesting the url
response=requests.get("https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1")
if response.status_code == 200:
    data=response.json()
    first_data=data['list']
    first_data=first_data[0]
    for key,values in first_data.items():
     print(key+": ",values,"\n");
# We have recieved the data now we can extract the data
elif response.status_code == 404:
    print('Not Found.')
