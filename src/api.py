from requests import get


class APIAdapter:
    """Класс для получения данных из OpenStreetMap и OpenSky."""

    def __init__(self):
        self.__openstreetmap_url = "https://nominatim.openstreetmap.org/search"
        self.__opensky_url = "https://opensky-network.org/api/states/all"

    def get_aeroplanes(self, country: str) -> list[dict]:
        """
        Возвращает список самолетов, находящихся в воздушном пространстве страны.
        """

        headers = {"User-Agent": "airplanes-tracker/1.0"}

        params_nominatim = {"country": country, "format": "json", "limit": 1}

        response = get(
            self.__openstreetmap_url,
            headers=headers,
            params=params_nominatim,
        )

        data = response.json()

        bounding_box = data[0]["boundingbox"]

        params_opensky = {
            "lamin": bounding_box[0],
            "lamax": bounding_box[1],
            "lomin": bounding_box[2],
            "lomax": bounding_box[3],
        }

        response = get(
            self.__opensky_url,
            params=params_opensky,
        )

        data = response.json()

        states = data.get("states")

        aeroplanes = []

        for state in states[:50]:
            aeroplanes.append(
                {
                    "callsign": state[1].strip(),
                    "country_register": state[2],
                    "velocity": state[9],
                    "altitude": state[13],
                }
            )

        return aeroplanes
