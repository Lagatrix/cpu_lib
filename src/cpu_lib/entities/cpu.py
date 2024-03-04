"""Represents a CPU."""
from dataclasses import dataclass


@dataclass
class Cpu:
    """Represents a CPU.

    Args:
        model: The model of the CPU.
        vendor: The vendor of the CPU.
        cache_size: The cache size of the CPU.
        siblings: The number of siblings of the CPU.
        cores: The number of cores of the CPU.
        min_mhz_speed: The minimum speed of the CPU in MHz.
        max_mhz_speed: The maximum speed of the CPU in MHz.
    """
    model: str
    vendor: str
    cache_size: str
    siblings: int
    cores: int
    min_mhz_speed: int
    max_mhz_speed: int
