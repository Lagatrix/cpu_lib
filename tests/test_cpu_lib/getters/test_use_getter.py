"""Test the use getter."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from cpu_lib.managers.getters import UseGetter
from tests.mock_cpu_lib import mock_command_executor_method, mock_use


class TestUseGetter(unittest.IsolatedAsyncioTestCase):
    """Test the use getter."""

    def setUp(self) -> None:
        """Set up the test."""
        self.use_getter = UseGetter(CommandManager("augusto", "augusto"))

    async def test_get_use(self) -> None:
        """Test correctly get the use of CPU."""
        with mock.patch(mock_command_executor_method, return_value=mock_use):
            self.assertEqual(await self.use_getter.get_use(), 25.4)
