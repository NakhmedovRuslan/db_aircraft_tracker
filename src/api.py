from requests import get


class APIAdapter:

    def __init__(self) -> None:
        self.__openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
        self.__opensky_url = 'https://opensky-network.org/api/states/all?'


    def get_aeroplanes(self, country: str) -> list[dict]:
        #Headers с user-agent - обязательный параметр при запросе к nominatim.openstreetmap.
        #Вы можете использовать любое название вместо test-app/1.0, например просто test-app.
        headers_nominatim = {
            'User-Agent': 'test-app/1.0',
        }

        #Указываем параметры: в каком формате возвращать данные и максимальную длину списка стран в ответе.
        params_nominatim = {
            'country': country,
            'format': 'json',
            'limit': 1,
        }

        response = get(url=self.__openstreetmap_url, params=params_nominatim, headers=headers_nominatim)

        data = response.json()

        #Пример ответа от nominatim.openstreetmap можно посмотреть в задании курсовой.
        geo_coordinates = data[0].get('boundingbox')

        #Параметры для фильтрации самолетов по их географическим координатам.
        params = {
            'lamin': geo_coordinates[0],
            'lamax': geo_coordinates[1],
            'lomin': geo_coordinates[2],
            'lomax': geo_coordinates[3],
        }

        response = get(url=self.__opensky_url, params=params)

        #Пример ответа от opensky-network можно посмотреть в задании курсовой.
        aeroplanes = response.json()['states'][:50]

        filter_airplanes = []
        for aeroplane in aeroplanes:
            filter_airplanes.append({"Callsign": aeroplane[1].strip(),
                                     "country register": aeroplane[2],
                                     "velocity": aeroplane[9],
                                     "altitude": aeroplane[13]})

        return filter_airplanes


# if __name__ == '__main__':
#     countries = ['Canada', 'China', 'Brazil', 'Germany']
#     api = APIAdapter()
#     for country in countries:
#         print(api.get_aeroplanes(country))
