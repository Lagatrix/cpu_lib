"""Test the temperature getter."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager, CommandError

from cpu_lib import TemperatureSensorError
from cpu_lib.managers.getters import TemperatureGetter
from tests.mock_cpu_lib import mock_command_executor_method, mock_temperature


class TestTemperatureGetter(unittest.IsolatedAsyncioTestCase):
    """Test the temperature getter."""

    def setUp(self) -> None:
        """Set up the test."""
        self.temperature_getter = TemperatureGetter(CommandManager("augusto", "augusto"))

    async def test_get_temperature(self) -> None:
        """Test correctly get the temperature of CPU."""
        with mock.patch(mock_command_executor_method, return_value=mock_temperature):
            self.assertEqual(await self.temperature_getter.get_temperature(), 34.9)

    async def test_get_temperature_not_found_sensor(self) -> None:
        """Test error when getting the temperature of CPU."""
        with mock.patch(mock_command_executor_method, return_value=[]):
            with self.assertRaises(TemperatureSensorError):
                await self.temperature_getter.get_temperature()

    async def test_get_temperature_error(self) -> None:
        """Test error when getting the temperature of CPU."""
        with mock.patch(mock_command_executor_method, side_effect=CommandError(1, "")):
            with self.assertRaises(TemperatureSensorError):
                await self.temperature_getter.get_temperature()
