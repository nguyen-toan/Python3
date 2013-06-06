'''
Created on Jun 2, 2013

@author: tnguyen7
'''
import re
import logging
LOG_FILENAME = "property_address.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
DEFAULT_LOG_LEVEL = "warning"
LEVELS = {'debug'    : logging.DEBUG,
          'info'     : logging.INFO,
          'warning'  : logging.WARNING,
          'error'    : logging.ERROR,
          'critical' : logging.CRITICAL}

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)
    
class Address:
    
    def __init__(self, name, street_address, city, state, zip_code):
        logging.info('Creating a new address')
        self._name = name
        self._street_address = street_address
        self._city = city
        self._state = state 
        self._zip_code = zip_code
        
    @property
    def name(self):
        return self._name

    @property
    def street_address(self):
        return self._street_address

    @property
    def city(self):
        return self._city

    @property
    def state(self):
        return self._state

    @property
    def zip_code(self):
        return self._zip_code

    @street_address.setter
    def street_address(self, value):
        self._street_address = value

    @city.setter
    def city(self, value):
        self._city = value

    @state.setter
    def state(self, value):
        "State only allows 2 capital letters or it throws a StateError"
        result = re.match(r"^[A-Z]{2}$", value)
        if not result:
            logging.error('STATE exception')
            raise StateError("Not a state")
        else:
            self._state = value

    @zip_code.setter
    def zip_code(self, value):
        "Zip code must follow the simple US pattern (nnnnn) or it throws a ZipCodeError"
        result = re.match(r"^\d{5}$", value)
        if not result:
            logging.error('ZIPCODE exception')
            raise ZipCodeError("Invalid zip code")
        else:
            self._zip_code = value


class StateError(Exception):
    pass

class ZipCodeError(Exception):
    pass
