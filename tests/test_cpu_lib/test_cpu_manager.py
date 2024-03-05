"""Test the CPU manager."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from cpu_lib import CpuManager
from tests.mock_cpu_lib import (mock_command_executor_method, mock_cpu_info, mock_cpu_min_freq, mock_cpu_max_freq,
                                mock_cpu_entity, mock_temperature, mock_use)


class TestCpuManager(unittest.IsolatedAsyncioTestCase):
    """Test the CPU manager."""

    def setUp(self) -> None:
        """Set up the test."""
        self.cpu_manager = CpuManager(CommandManager("augusto", "augusto"))

    async def test_get_cpu(self) -> None:
        """Test correctly get the CPU."""
        with mock.patch(mock_command_executor_method, side_effect=(mock_cpu_info, mock_cpu_min_freq,
                                                                   mock_cpu_max_freq)):
            self.assertEqual(await self.cpu_manager.get_cpu(), mock_cpu_entity)

    async def test_get_temperature(self) -> None:
        """Test correctly get the temperature of CPU."""
        with mock.patch(mock_command_executor_method, return_value=mock_temperature):
            self.assertEqual(await self.cpu_manager.get_cpu_temperature(), 34.9)

    async def test_get_use(self) -> None:
        """Test correctly get the use of CPU."""
        with mock.patch(mock_command_executor_method, return_value=mock_use):
            self.assertEqual(await self.cpu_manager.get_cpu_use(), 25.4)
