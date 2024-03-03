import requests

from data.config import TWO_GIS_MAPS_API_KEY as api_key


def find_smth(latitude, longitude, query):
    url = 'https://catalog.api.2gis.com/3.0/items'

    if query == "📍Мусорные баки":
        query = 'Контейнер для мусора'

    elif query == "📍Переработка мусора":
        query = "переработка мусора"
    params = {
        'key': api_key,
        'q': query,
        'point': f'{longitude},{latitude}',
        'radius': 5000,
        'type': 'branch',
        'search_nearby': 'true',
        'sort': 'distance',
        'fields': 'items.point,items.address_name'
    }

    response = requests.get(url, params=params)
    response_data = response.json()

    ddict = {}
    try:
        for index, item in enumerate(response_data['result']['items']):
            coordinates = item['point']
            try:
                address = item['address_name']
            except Exception as e:
                address = index
            ddict[address] = coordinates
    except Exception as e:
        pass
    return ddict
