from openrgb import OpenRGBClient
from openrgb.utils import DeviceType, RGBColor
import os
import GPUtil
import time
import psutil

cli = OpenRGBClient("192.168.1.122", 6742, "My client!")

cli.show()

green = RGBColor(0, 128, 0)
yellow = RGBColor(255, 255, 0)
orange = RGBColor(255, 127, 0)
redish = RGBColor(200, 0, 0)
red = RGBColor(255, 0, 0)
pink = RGBColor(233, 39, 233)

DRAM0 = cli.get_devices_by_type(DeviceType.DRAM)[0]
DRAM1 = cli.get_devices_by_type(DeviceType.DRAM)[1]



## TODO
# Figure out multiple zone to have progression on the surface instead of filled static


def get_cpu_usage_pct():
    return psutil.cpu_percent(interval=0.5)

def get_cpu_load():
    CPU_load = get_cpu_usage_pct()
    print(CPU_load, "% CPU LOAD")

    if CPU_load <= 19:
        DRAM0.set_color(green)
    if 20 < CPU_load < 39:
        DRAM0.set_color(yellow)
    if 40 < CPU_load < 59:
        DRAM0.set_color(orange)
    if 60 < CPU_load < 79:
        DRAM0.set_color(pink)
    if 80 < CPU_load < 100:
        DRAM0.set_color(red)

def get_load():
    GPU_load = GPUs[0].load
    print(GPU_load*100, "% GPU LOAD")



def get_temps():
    GPU_temp = GPUs[0].temperature
    print(GPU_temp, "°c GPU TEMP")
    if GPU_temp <= 50:
        DRAM1.set_color(green)
    if 51 < GPU_temp < 55:
        DRAM1.set_color(yellow)
    if 56 < GPU_temp < 65:
        DRAM1.set_color(orange)
    if 66 < GPU_temp < 75:
        DRAM1.set_color(pink)
    if 76 < GPU_temp < 84:
        DRAM1.set_color(red)
    
def get_memory():
    GPU_memory_used = GPUs[0].memoryUsed
    print(GPU_memory_used, " MEMORY USED")
    
while True:
    GPUs = GPUtil.getGPUs()
    get_cpu_load()
    get_load()
    get_memory()
    get_temps()
    time.sleep(2)
    os.system('cls||clear')
