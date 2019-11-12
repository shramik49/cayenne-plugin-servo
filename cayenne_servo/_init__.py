"""
This module provides a class for interfacing with a servo.
"""
from myDevices.utils.logger import info
from myDevices.plugins.analog import AnalogOutput


class Servo(AnalogOutput):
    """Class for interacting with a TMP36 sensor"""

    def __init__(self, adc, channel):
        """Initializes TMP36 device.
        Arguments:
        adc: The analog to digital converter extension ID, e.g. 'cayenne_mcp3xxx:MCP'
        channel: The channel on the ADC the TMP36 is connected to
        """        
        AnalogInput.__init__(self, adc)
        self.channel = channel

    def get_temperature(self):
        """Gets the temperature as a tuple with type and unit."""
        return ((self.read_volt(self.channel) * 1000 - 500) / 10, 'temp', 'c')
