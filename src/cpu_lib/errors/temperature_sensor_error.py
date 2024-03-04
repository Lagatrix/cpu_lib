"""This error represents if the system can't detect the temperature sensor."""


class TemperatureSensorError(Exception):
    """This error represents if the system can't detect the temperature sensor."""

    def __init__(self) -> None:
        """Initialize the TemperatureSensorError."""
        super().__init__("The system can't read the temperature sensor.")
