import weather_au

# https://docs.python.org/3/library/xml.dom.html#module-xml.dom

class Observations:

    def __init__(self, state):

        self.state = state
        self.url = weather_au.OBSERVATION_PRODUCT_URL[state]
        self.soup = weather_au.fetch_xml(self.url)
        print(self.url)
        self.identifier = self.soup.identifier.contents[0]
        self.acknowedgment = f'Data courtesy of Bureau of Meteorology ({self.url})'
    

    def stations(self):
        # List of station attributes

        station_list =[]

        for station in self.soup.find_all('station'):
            station_list.append(station.attrs)

        return station_list


    def station_elements(self, wmo_id=None):
        # Element child tags for a specified station

        return self.soup.find('station', {'wmo-id': wmo_id})


    def station_attribute(self, wmo_id=None, attribute=None):

        attrs = self.soup.find('station', {'wmo-id': wmo_id}).attrs

        if attribute in attrs:
            return attrs[attribute]
        else:
            return None


    def air_temperature(self, wmo_id=None):
        """ Don't assume that any elements exist or that there is an element with type air_temperature
        """

        elements = self.soup.find('station', {'wmo-id': wmo_id})

        if elements is not None:
            air_temperature_el = elements.find('element', {'type': 'air_temperature'})

            if air_temperature_el is not None and len(air_temperature_el.contents) > 0:
                    return air_temperature_el.contents[0]

        return None

    def relative_humidity(self, wmo_id=None):
        """ Don't assume that any elements exist or that there is an element with type air_temperature
        """

        elements = self.soup.find('station', {'wmo-id': wmo_id})

        if elements is not None:
            relative_humidity_el = elements.find('element', {'type': 'rel-humidity'})

            if relative_humidity_el is not None and len(relative_humidity_el.contents) > 0:
                    return relative_humidity_el.contents[0]

        return None

    def wind_dir(self, wmo_id=None):
        """ Don't assume that any elements exist or that there is an element with type wind_dir
        """

        elements = self.soup.find('station', {'wmo-id': wmo_id})

        if elements is not None:
            wind_dir_el = elements.find('element', {'type': 'wind_dir'})

            if wind_dir_el is not None and len(wind_dir_el.contents) > 0:
                    return wind_dir_el.contents[0]

        return None

    def pressure(self, wmo_id=None):
        """ Don't assume that any elements exist or that there is an element with type pressure
        """

        elements = self.soup.find('station', {'wmo-id': wmo_id})

        if elements is not None:
            pressure_el = elements.find('element', {'type': 'pres'})

            if pressure_el is not None and len(pressure_el.contents) > 0:
                    return pressure_el.contents[0]

        return None
        
    def wind_dir_deg(self, wmo_id=None):
        """ Don't assume that any elements exist or that there is an element with type wind_dir_deg
        """

        elements = self.soup.find('station', {'wmo-id': wmo_id})

        if elements is not None:
            wind_dir_deg_el = elements.find('element', {'type': 'wind_dir_deg'})

            if wind_dir_deg_el is not None and len(wind_dir_deg_el.contents) > 0:
                    return wind_dir_deg_el.contents[0]

        return None

    def wind_spd_kmh(self, wmo_id=None):
        """ Don't assume that any elements exist or that there is an element with type wind_spd_kph
        """

        elements = self.soup.find('station', {'wmo-id': wmo_id})

        if elements is not None:
            wind_spd_kph_el = elements.find('element', {'type': 'wind_spd_kmh'})

            if wind_spd_kph_el is not None and len(wind_spd_kph_el.contents) > 0:
                    return wind_spd_kph_el.contents[0]

        return None

    def rainfall(self, wmo_id=None):
        """ Don't assume that any elements exist or that there is an element with type rainfall
        """

        elements = self.soup.find('station', {'wmo-id': wmo_id})

        if elements is not None:
            rainfall_el = elements.find('element', {'type': 'rainfall'})

            if rainfall_el is not None and len(rainfall_el.contents) > 0:
                    return rainfall_el.contents[0]

        return None
    def __str__(self):
        return str(self.soup)


if __name__ == "__main__":
    x = Observations("Vic")
    print(x.air_temperature(95936))
    print(x.relative_humidity(95936))
    print(x.pressure(95936))
    print(x.rainfall(95936))
    print(x.wind_dir(95936))
    print(x.wind_dir_deg(95936))
    print(x.wind_spd_kmh(95936))
