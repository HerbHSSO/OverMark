import json, os, time, re
import pyopencl as cl
from pyadl import *
from gpuinfo import GPUInfo







class videocard:
    def name():
        name = "wmic path Win32_VideoController get Name"
        os.popen(name)
        try:
            return str(os.popen(name).read().split('\n\n')[2])
        except:
            return str(os.popen(name).read().split('\n\n')[1])
    def type():
        if "GeForce" in videocard.name():
            return "Discrete"
        elif "Radeon" in videocard.name():
            return "Discrete"
        else:
            return "Integred"
    def vram():
        platform = cl.get_platforms()
        gpu_devices = platform[0].get_devices(device_type=cl.device_type.GPU)[0]
        #print(gpu_devices)
        return float(gpu_devices.global_mem_size / 1024**2)
        
        
    def max_clock():

        platform = cl.get_platforms()
        gpu_devices = platform[0].get_devices(device_type=cl.device_type.GPU)[0]
        #print(gpu_devices)
        return float(gpu_devices.max_clock_frequency)
    def clock():
        if "AMD" in videocard.name():
            try:
                device = ADLManager.getInstance().getDevices()
            
                clock = device.getCurrentEngineClock()
                return clock
            except:
                return ''
        

        
    def compute_units():

        platform = cl.get_platforms()
        gpu_devices = platform[0].get_devices(device_type=cl.device_type.GPU)[0]
        return int(gpu_devices.max_compute_units)

    def driver():
        platform = cl.get_platforms()
        gpu_devices = platform[0].get_devices(device_type=cl.device_type.GPU)[0]
        return str(gpu_devices.driver_version)

    def cores():
        cores_gpu = int('{}'.format(videocard.compute_units())) * 64
        return cores_gpu
        if 'RTX 30' in videocard.name():
            cores_gpu = int('{}'.format(videocard.compute_units())) * 128
            return cores_gpu        
    def teraflops():
        gflops = float('{}'.format(videocard.cores() * videocard.max_clock() * 2)) % 1000000 
        tflops = gflops/1000000
        return tflops





























    
