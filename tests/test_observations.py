import os, sys
sys.path.append(os.path.abspath('.'))
import pytest
import urllib


from weather import observations

def test_invalid_state():
    with pytest.raises(KeyError, match='zzz'):
        obs = observations.Observations('zzz')

obs = observations.Observations('Vic')

def test_obs():
    assert obs is not None

def test_acknowedgment_url():
    assert len(obs.url) > 0
    assert len(obs.acknowedgment) > 0

def test_identifier():
    assert obs.identifier == 'IDV60920'

def test_station_list():
    stations = obs.stations()
    assert len(stations) > 10

    for station in stations:
        station_wmo_id = station['wmo-id']
        assert station_wmo_id is not None

        station_description = station['description']
        assert station_description is not None

        station_air_temperature = obs.air_temperature(station['wmo-id'])
    
def test_air_temperature():
    air_temperature = obs.air_temperature('95936')
    assert air_temperature is not None

def test_description():
    wmo_id = '95936'
    assert obs.station_attribute(wmo_id, 'description') == 'Melbourne (Olympic Park)'
