"""Obtains the information of the CPU."""
from shell_executor_lib import CommandManager


class InformationGetter:
    """Obtains the information of the CPU."""

    def __init__(self, command_manager: CommandManager) -> None:
        """Initialize the information getter.

        Args:
            command_manager: The command manager to use to execute commands.
        """
        self.__command_manager = command_manager

    async def get_cpu_info(self) -> tuple[str, str, str, int, int]:
        """Obtains the information of the CPU.

        Returns:
            A tuple with the information of CPU in this order: vendor, model name, cache size, cpu cores and siblings.

        Raises:
            CommandError: If the exit code is not 0.
        """
        command_filter: str = '/model name|vendor_id|cpu cores|siblings|cache size/'
        data_list: list[str] = await (self.__command_manager.execute_command
                                      (f"/bin/cat /proc/cpuinfo | /bin/awk '{command_filter}'"))

        return (data_list[0].split(": ")[1], data_list[1].split(": ")[1], data_list[2].split(": ")[1],
                int(data_list[3].split(": ")[1]), int(data_list[4].split(": ")[1]))

    async def get_cpu_min_freq(self) -> float:
        """Obtains the minimum frequency of the CPU.

        Returns:
            The minimum frequency of the CPU in megahertz.

        Raises:
            CommandError: If the exit code is not 0.
        """
        data_list: list[str] = await (self.__command_manager.execute_command
                                      ("/bin/cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq"))

        return int(data_list[0]) / 1000

    async def get_cpu_max_freq(self) -> float:
        """Obtains the maximum frequency of the CPU.

        Returns:
            The maximum frequency of the CPU in megahertz.

        Raises:
            CommandError: If the exit code is not 0.
        """
        data_list: list[str] = await (self.__command_manager.execute_command
                                      ("/bin/cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq"))

        return int(data_list[0]) / 1000
