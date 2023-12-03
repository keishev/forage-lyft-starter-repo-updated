from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.splinder_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from car import Car

def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
    battery = SpindlerBattery(last_service_date, current_date)
    Car (engine, battery)

def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = WilloughbyEngine(last_service_mileage, current_mileage)
    battery = SpindlerBattery(last_service_date, current_date)
    Car (engine, battery)

def create_palindrome(current_date, last_service_date, warning_light_on):
    engine = SternmanEngine(warning_light_on)
    battery = SpindlerBattery(last_service_date, current_date)
    Car (engine, battery)

def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = WilloughbyEngine(last_service_mileage, current_mileage)
    battery = NubbinBattery(last_service_date, current_date)
    Car (engine, battery)

def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = CapuletEngine(last_service_mileage, current_mileage)
    battery = NubbinBattery(last_service_date, current_date)
    Car (engine, battery)


