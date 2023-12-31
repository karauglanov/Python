import pandas as pd
import requests
from pathlib import Path

#Функция получения почасовых  и суточных данных температуры окружающей среды
#T2M - MERRA-2 Temperature at 2 Meters (C) 
#T2MDEW - MERRA-2 Dew/Frost Point at 2 Meters (C) 
#T2MWET - MERRA-2 Wet Bulb Temperature at 2 Meters (C)
def get_data(time_resolution, lon, lat, start, end):
    global output_dir
    if time_resolution == "daily":
        url = "https://power.larc.nasa.gov/api/temporal/daily/point"
        output_dir =  "./daily_data"
    elif time_resolution == "hourly":
        url = "https://power.larc.nasa.gov/api/temporal/hourly/point"
        output_dir = "./hourly_data"
        
    query_params = {
        "parameters": "T2M", #T2M,T2MDEW,T2MWET
        "community": "SB",
        "longitude": lon,
        "latitude": lat,
        "start": start,
        "end": end,
        "format": "json",
        "time-standard": "UTC"          
    }

    response = requests.get(url, params=query_params)                
    data_json = response.json()
       
    #Преобразование данных json в DataFrame
    records = data_json['properties']['parameter']
    df = pd.DataFrame.from_dict(records)
    return df


city = {"Мытищи": [2, 55.8994, 37.6682],
        "Красногорск": [3, 55.8112, 37.3866],
        "Алтуфьево": [4, 55.9154, 37.5727],
        "Химки": [5, 55.9037, 37.4154],
        "Сокольники": [6, 55.7858, 37.6656],
        "Ростов 1": [7, 47.2904, 39.8466],
        "Краснодар 1": [8, 45.0366, 39.0522],
        "Самара 1": [9, 53.2077, 50.1982],
        "Санкт-Петербург 1": [10, 59.9120, 30.4470],
        "Санкт-Петербург 2": [11, 60.0050, 30.3005],
        "Новосибирск 1": [12, 54.9645, 82.9364],
        "Самара 2": [13, 53.3262, 50.3083],
        "Ростов 2": [14, 47.3096, 39.7265],
        "Омск 1": [16, 54.9716, 73.2847],
        "Уфа 1": [17, 54.6710, 55.9283],
        "Тверь": [18, 56.8133,  35.8836],
        "Рязань": [19, 54.6214, 39.8030],
        "Лефортово": [20, 55.7473, 37.7063],            
        "Воронеж": [21, 51.7867, 39.2010],
        "Климовск": [22, 55.3877, 37.5490],
        "Красноярск 1": [23, 56.0498, 92.9023],
        "Волгоград": [24, 48.6375, 44.4363],
        "Екатеринбург": [25, 56.8021, 60.6496],
        "Рязанский": [26, 55.7291, 37.7346],
        "Казань 1": [27, 55.8177, 49.1302],
        "Ногинск": [28, 55.8303, 38.3982],
        "Новосибирск 2": [30, 55.0227, 82.9014],
        "Тюмень": [31, 57.1176, 65.5488],
        "Новая Рига": [32, 55.7999, 37.3003],
        "Уфа 2": [33, 54.7602, 56.0389],
        "Самара 3": [34, 53.1431, 50.1757],
        "Зеленоград": [35, 56.0007, 37.2523],
        "Барнаул 1": [36, 53.3503, 83.6321],
        "Красноярск 2": [37, 56.0202, 93.0094],
        "Челябинск": [38, 55.1454, 61.4534],
        "Набережные Челны": [39, 55.7117, 52.4028],
        "Шолохово": [40, 56.0459, 37.5433],
        "Санкт-Петербург 3": [41, 60.0556, 30.3890],
        "Санкт-Петербург 4": [42, 59.8428, 30.1786],
        "Каширское": [43, 55.5890, 37.7270],
        "Новокузнецк": [44, 53.7777, 87.1208],
        "Казань 2": [46, 55.7228, 49.1969],
        "Тула": [47, 54.1776, 37.6490],
        "Пенза": [48, 53.2226, 44.9506],
        "Люберцы": [49, 55.6647, 37.8834],
        "Киевское шоссе": [51, 55.6213, 37.3899],
        "Ярославль 2": [52, 57.5689, 39.8413],
        "Екатеринбург 2": [53, 56.8289, 60.5162],
        "Кемерово": [55, 55.3496, 86.1755],
        "Юдино": [56, 55.6559, 37.1829],
        "Саратов": [57, 51.5898, 46.1291],
        "Ярославль 1": [58, 57.6378,39.9682],
        "Кострома": [59, 57.7428, 41.0197],
        "Пушкино": [65, 56.0154, 37.8847],
        "Новосибирск 3": [67, 55.1065, 82.9292],
        "Иркутск": [68, 52.2951, 104.2528],
        "Ставрополь": [69, 44.9848, 41.9685],
        "Волжский": [70, 48.8134, 44.7264],
        "Ульяновск": [71, 54.2908, 48.2685],
        "Курск": [73, 51.6982, 36.1559],
        "Оренбург": [74, 51.7772, 55.1986],
        "Владивосток": [75, 43.3563, 132.0741],
        "Киров": [77, 58.6129, 49.5936],
        "Калининград": [78, 54.7747, 20.5474],
        "Петрозаводск": [79, 61.7805, 34.3032],
        "Тольятти": [80, 53.5505, 49.3389],
        "Хабаровск": [81, 48.4290, 135.1039],
        "Красноярск 3": [82, 56.0423, 92.7837],
        "Архангельск": [83, 64.5301, 40.5948],
        "Троицк": [86, 55.4544, 37.2884],
        "Сургут": [87, 61.2436, 73.3621],
        "Омск 3": [88, 55.0364, 73.4130],
        "Барнаул 2": [89, 53.3170, 83.8295],
        "Белгород": [90, 50.5529, 36.5606],
        "Череповец": [91, 59.1024, 37.9047],
        "Краснодар 3": [92, 45.1073, 38.9518],
        "Иваново": [93, 56.9467, 41.0590],
        "Ростов 3": [94, 47.2392, 39.5847],
        "Пермь": [109, 57.9696, 56.1467],
        "Тюмень 2": [110, 57.1728, 65.6784],
        "Воронеж 2": [111, 51.6498, 39.3096],
        "Алматы": [113, 43.2343, 76.7811],
        "Домодедово": [114, 55.3952, 37.7807],
        "Ижевск": [115, 56.8379, 53.3070],
        "Зил": [117, 55.6998, 37.6442],
        "Наро-Фоминск": [118, 55.6998, 37.6442],
        "Нижний Новгород": [119, 56.3070, 43.7717],
        "Истра": [122, 55.9053, 36.9010],
        "Хабаровск 2": [123, 48.5465, 135.0579],
        "Новосибирск 4": [124, 54.8491, 83.0653],
        "Клин": [126, 56.3155, 36.7755],
        "Саранск": [127, 54.2090, 45.2490],
        "Кемерово 2": [128, 55.3577, 86.0627],
        "Новокузнецк 2": [129, 53.7568, 87.1773],
        "Магнитогорск": [131, 53.4012, 58.9884],
        "Санкт-Петербург (Парашютная)": [134, 60.0382, 30.2363],
        "Санкт-Петербург (Московское)": [135, 59.8002, 30.3980],
        "Санкт-Петербург (Петергофское)": [136, 59.8520, 30.0964],
        "Санкт-Петербург (Таллинское)": [137, 59.8054, 30.1600],
        "Санкт-Петербург (Уральская)": [138, 59.9551, 30.2456],
        "ЦИЗ Парнас": [139, 60.0669, 30.3477],
        "Санкт-Петербург (Выборгское)": [140, 60.0734, 30.2725],
        "Санкт-Петербург (Руставели)": [141, 60.0274, 30.4346],
        "Калуга": [142, 54.5488, 36.3334],
        "Варшавское шоссе": [143, 55.5719, 37.6037],
        "Мега-Адыгея": [147, 45.0178, 38.9303],
        "Владикавказ": [150, 43.0573, 44.6387],
        "Жуковский": [153, 55.5631, 38.0557],
        "Липецк": [155, 52.5984, 39.4814],
        "Псков": [156, 57.8061, 28.2716],
        "Орёл": [159, 53.0081, 36.1179],
        "Казань 3": [163, 55.8594, 48.8624],
        "Новороссийск": [165, 44.7481, 37.7302],
        "Выхино": [169, 55.7116, 37.8461],
        "Смоленск": [181, 54.8346, 32.0496],
  		"ЦИЗ Елино ": [251, 55.9911, 37.2715],
        "ЦИЗ Косино": [252, 55.7144, 37.8840],
        "ЦИЗ Санкт-Петербург Южный": [253, 59.7798, 30.4553],
        "ДС МСК Мытищи ": [257, 55.9230, 37.7116],
        "РЦ ЮВ": [912, 55.3348, 37.8168],
        "РЦ СЗ": [922, 56.1468, 37.4174],
          
        }

       
shop_name = list(city) # получение списка магазинов-ключей

for x in range(0, len(list(city))):
    name = shop_name[x] # присваиваем переменной имя первого магазина
    info = city[name] # получение данных по ключу
    latitude = info[1]
    longitude = info[2]
    start_date = 20210101
    end_date = 20230831
        
    #Получение данных переключение функция hourly и daily    
    weather_data = get_data(time_resolution="hourly", lon=longitude, lat=latitude, start=start_date, end=end_date)
    output_dir = Path(output_dir) / f"{info[0]} - {name} - ({longitude};{latitude}).xlsx"
    
    # Сохранение DataFrame в xlsx-файл     
    weather_data.to_excel(output_dir, index=True)
    print("Сохранены данные для магазина: ", name)