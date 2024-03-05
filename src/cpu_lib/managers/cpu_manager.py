"""Obtains the CPU of the system."""
from shell_executor_lib import CommandManager

from cpu_lib.entities import Cpu
from cpu_lib.managers.getters import InformationGetter, TemperatureGetter, UseGetter


class CpuManager:
    """Obtains the CPU of the system."""

    def __init__(self, command_manager: CommandManager) -> None:
        """Initialize the CPU manager.

        Args:
            command_manager: The command manager to use to execute commands.
        """
        self.__information_getter = InformationGetter(command_manager)
        self.__temperature_getter = TemperatureGetter(command_manager)
        self.__use_getter = UseGetter(command_manager)

    async def get_cpu(self) -> Cpu:
        """Obtains the information of the CPU.

        Returns:
            The information of the CPU.

        Raises:
            CommandError: If the exit code is not 0.
        """
        vendor, model_name, cache_size, cpu_cores, siblings = await self.__information_getter.get_cpu_info()

        return Cpu(
            vendor=vendor,
            model=model_name,
            cache_size=cache_size,
            cores=cpu_cores,
            siblings=siblings,
            min_mhz_speed=await self.__information_getter.get_cpu_min_freq(),
            max_mhz_speed=await self.__information_getter.get_cpu_max_freq()
        )

    async def get_cpu_temperature(self) -> float:
        """Obtains the temperature of the CPU.

        Returns:
            The temperature of the CPU in Celsius.

        Raises:
            CommandError: If the exit code is not 0.
        """
        return await self.__temperature_getter.get_temperature()

    async def get_cpu_use(self) -> float:
        """Obtains the use of the CPU.

        Returns:
            The use of the CPU in percentage.

        Raises:
            CommandError: If the exit code is not 0.
        """
        return await self.__use_getter.get_use()
