"""Obtains the temperature of the CPU."""
from shell_executor_lib import CommandManager, CommandError

from cpu_lib.errors import TemperatureSensorError


class TemperatureGetter:
    """Obtains the temperature of the CPU."""

    def __init__(self, command_manager: CommandManager) -> None:
        """Initialize the temperature getter.

        Args:
            command_manager: The command manager to use to execute commands.
        """
        self.__command_manager = command_manager

    async def get_temperature(self) -> float:
        """Get the temperature of the CPU.

        Returns:
            The temperature of the CPU in Celsius.

        Raises:
            TemperatureSensorError: If the temperature sensor is not found.
        """
        try:
            data_list: list[str] = await self.__command_manager.execute_command(
                "/bin/cat /sys/class/thermal/thermal_zone*/temp")

            if len(data_list) > 2:
                return float(f"{data_list[-1][0]}{data_list[-1][1]}.{data_list[-1][2]}")

            raise TemperatureSensorError()
        except CommandError:
            raise TemperatureSensorError()
