"""Test the information getter."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from cpu_lib.managers.getters import InformationGetter
from tests.mock_cpu_lib import (mock_cpu_info, mock_command_executor_method, mock_cpu_info_in_tuple, mock_cpu_min_freq,
                                mock_cpu_max_freq)


class TestInformationGetter(unittest.IsolatedAsyncioTestCase):
    """Test the information getter."""

    def setUp(self) -> None:
        """Set up the test."""
        self.information_getter = InformationGetter(CommandManager("augusto", "augusto"))

    async def test_get_cpu_info(self) -> None:
        """Test correctly get the information of CPU."""
        with mock.patch(mock_command_executor_method, return_value=mock_cpu_info):
            self.assertEqual(await self.information_getter.get_cpu_info(), mock_cpu_info_in_tuple)

    async def test_get_cpu_min_freq(self) -> None:
        """Test correctly get the minimum frequency of CPU."""
        with mock.patch(mock_command_executor_method, return_value=mock_cpu_min_freq):
            self.assertEqual(await self.information_getter.get_cpu_min_freq(), 800)

    async def test_get_cpu_max_freq(self) -> None:
        """Test correctly get the maximum frequency of CPU."""
        with mock.patch(mock_command_executor_method, return_value=mock_cpu_max_freq):
            self.assertEqual(await self.information_getter.get_cpu_max_freq(), 4200)
