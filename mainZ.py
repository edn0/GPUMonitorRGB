from openrgb import OpenRGBClient
from openrgb.utils import DeviceType, RGBColor
import os
import GPUtil
import time
import psutil

cli = OpenRGBClient("192.168.1.122", 6742, "My client!")

cli.show()

green = RGBColor(0, 128, 0)
yellow = RGBColor(150, 150, 0)
orange = RGBColor(255, 127, 0)
redish = RGBColor(200, 0, 0)
red = RGBColor(255, 0, 0)
pink = RGBColor(233, 39, 233)
black = RGBColor(0, 0, 0)
DRAM0 = cli.get_devices_by_type(DeviceType.DRAM)[0]
DRAM1 = cli.get_devices_by_type(DeviceType.DRAM)[1]

DRAM0.zones[0].resize(5)
DRAM1.zones[0].resize(5)


## TODO
# For startup : set ram sticks to static mode before setting color. It starts up as rainbow.

def get_cpu_usage_pct():
    return psutil.cpu_percent(interval=0.3)

def get_cpu_load():
    CPU_load = get_cpu_usage_pct()
    print(CPU_load, "% CPU LOAD")

    if CPU_load <= 19:
        DRAM0.zones[0].colors[4] = green
    if CPU_load >= 20:
        DRAM0.zones[0].colors[3] = yellow
    elif CPU_load < 20:
        DRAM0.zones[0].colors[3] = black
    if CPU_load >= 40:
        DRAM0.zones[0].colors[2] = orange
    elif CPU_load < 40:
        DRAM0.zones[0].colors[2] = black
    if CPU_load >= 60:
        DRAM0.zones[0].colors[1] = pink
    elif CPU_load < 60:
        DRAM0.zones[0].colors[1] = black
    if CPU_load > 80:
        DRAM0.zones[0].colors[0] = red
    elif CPU_load < 80:
        DRAM0.zones[0].colors[0] = black

def get_load():
    GPU_load = GPUs[0].load
    print(GPU_load*100, "% GPU LOAD")


def get_temps():
    GPU_temp = GPUs[0].temperature
    print(GPU_temp, "°c GPU TEMP")
    if GPU_temp <= 50:
        DRAM1.zones[0].colors[4] = green
    if GPU_temp >= 51:
        DRAM1.zones[0].colors[3] = yellow
    elif GPU_temp < 51:
        DRAM1.zones[0].colors[3] = black
    if GPU_temp >= 56:
        DRAM1.zones[0].colors[2] = orange
    elif GPU_temp < 56:
        DRAM1.zones[0].colors[2] = black
    if GPU_temp >= 66:
        DRAM1.zones[0].colors[1] = pink
    elif GPU_temp < 66:
        DRAM1.zones[0].colors[1] = black
    if GPU_temp > 78:
        DRAM1.zones[0].colors[0] = red
    elif GPU_temp < 78:
        DRAM1.zones[0].colors[0] = black
    
def get_memory():
    GPU_memory_used = GPUs[0].memoryUsed
    print(GPU_memory_used, " MEMORY USED")


    
while True:
    GPUs = GPUtil.getGPUs()
    os.system('cls||clear')
    get_cpu_load()
    DRAM0.zones[0].show()
    get_load()
    DRAM1.zones[0].show()
    get_memory()
    get_temps()
    time.sleep(0.5)