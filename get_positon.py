import exifread
from geopy.geocoders import Nominatim
def format_lati_long(data):#list2float
    list_tmp=str(data).replace('[', '').replace(']', '').split(',')
    list=[ele.strip() for ele in list_tmp]
    data_sec = int(list[-1].split('/')[0]) /(int(list[-1].split('/')[1])*3600)# 秒的值
    data_minute = int(list[1])/60
    data_degree = int(list[0])
    result=data_degree + data_minute + data_sec
    #result = round(data_degree + data_minute + data_sec,6)
    return result

img=exifread.process_file(open('C:/Users/Chipeyown/Desktop/2.jpg','rb'))
time=img['Image DateTime']
print(time)

latitude=format_lati_long(str(img['GPS GPSLatitude']))
print(latitude)
lat_direction=img['GPS GPSLatitudeRef']

longitude=format_lati_long(str(img['GPS GPSLongitude']))
print(longitude)
long_direction=img['GPS GPSLongitudeRef']

#geopy get position:
geolocator = Nominatim()
position0 = geolocator.reverse('%s,%s'%(latitude,longitude))#字符格式才显示中国
print(position0.address)



#高德
import requests,json
api_key = 'f84cbb2dc078c087c6dc37b6ae74ab85'
url_get_position = 'https://restapi.amap.com/v3/geocode/regeo?output=JSON&location={}&key={}&radius=1000&extensions=base'
resp=requests.get(url_get_position.format(f'{longitude},{latitude}',api_key))
location_data = json.loads(resp.text)
address = location_data.get('regeocode').get('formatted_address')
print(address)
