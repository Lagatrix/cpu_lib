"""Obtains the use of the CPU."""
from shell_executor_lib import CommandManager


class UseGetter:
    """Obtains the use of the CPU."""

    def __init__(self, command_manager: CommandManager) -> None:
        """Initialize the use getter.

        Args:
            command_manager: The command manager to use to execute commands.
        """
        self.__command_manager = command_manager

    async def get_use(self) -> float:
        """Get the use of the CPU.

        Returns:
            The use of the CPU in percentage.

        Raises:
            CommandError: If the exit code is not 0.
        """
        data_list: list[str] = await self.__command_manager.execute_command(
            "/bin/top -n 1 -b | grep 'Cpu(s):' | /bin/awk '{print $2}'")

        return float(data_list[0].replace(",", "."))
