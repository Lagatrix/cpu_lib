"""Mocks of CPU."""
from cpu_lib.entities import Cpu

mock_temperature = ["27800", "29000", "34900"]

mock_use = ["25,4"]

mock_cpu_info = ["vendor_id       : GenuineIntel", "model name      : Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz",
                 "cache size      : 6144 KB", "cpu cores       : 4", "siblings        : 8"]

mock_cpu_info_in_tuple = ("GenuineIntel", "Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz", "6144 KB", 4, 8)

mock_cpu_min_freq = ["800000"]

mock_cpu_max_freq = ["4200000"]

mock_cpu_entity = Cpu(
    vendor="GenuineIntel",
    model="Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz",
    cache_size="6144 KB",
    cores=4,
    siblings=8,
    min_mhz_speed=800,
    max_mhz_speed=4200
)
