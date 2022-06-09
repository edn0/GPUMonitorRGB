from openrgb import OpenRGBClient
from openrgb.utils import DeviceType, RGBColor
import os
import GPUtil
import time

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

DRAM0.set_color(pink)
DRAM1.set_color(RGBColor(255, 255, 255))

## TODO
# Instance color (green, yellow, orange, red)
# Move up through color list when temp increase certain value
# Figure out multiple zone to have progression on the surface instead of filled static





def get_load():
    GPU_load = GPUs[0].load
    print(GPU_load*100, "% LOAD")

def get_temps():
    GPU_temp = GPUs[0].temperature
    print(GPU_temp, "°c TEMP")
    if GPU_temp <= 50:
        DRAM1.set_color(green)
    if 51 < GPU_temp < 55:
        DRAM1.set_color(yellow)
    if 56 < GPU_temp < 65:
        DRAM1.set_color(orange)
    if 66 < GPU_temp < 75:
        DRAM1.set_color(redish)
    if 76 < GPU_temp < 84:
        DRAM1.set_color(red)
    
def get_memory():
    GPU_memory_used = GPUs[0].memoryUsed
    print(GPU_memory_used, " MEMORY USED")
    
while True:
    GPUs = GPUtil.getGPUs()
    get_load()
    get_memory()
    get_temps()
    time.sleep(3)
    os.system('cls||clear')
