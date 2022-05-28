import psutil
import platform
import time
from datetime import datetime




import multiprocessing
# print(f"Memory is: {psutil.virtual_memory()}")
# uname = platform.uname()
# print(f"System: {uname.system}")
# print(f"Node Name: {uname.node}")
# print(f"Release: {uname.release}")
# print(f"Version: {uname.version}")
# print(f"Machine: {uname.machine}")
# print(f"Processor: {uname.processor}")
#
# # print(multiprocessing.cpu_count())
#
# start_time = time.time()
# print("--- %s seconds ---" % (time.time() - start_time))


# TODO CREATING A FUNCTION WHICH IS CONVERTING LONG BYTES NUMBER INTO KILO, GIGA, MEGA ETC
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


# TODO CPU CORES
print("HOW MANY IN MY CPU ARE: ")
print(f"Total Cores: {psutil.cpu_count(logical=True)} \n")

#  TODO MEMORY INFORMATION
memory = psutil.virtual_memory()
print(f"Total Memory is : {get_size(memory.total)}")
print(f"Used Memory is : {get_size(memory.used)}")
print(f"Available Memory is: {get_size(memory.available)} \n")

# TODO BOOT TIME OR STARTING TIME OF OUR PC

start_time_pc = psutil.boot_time()
stp = datetime.fromtimestamp(start_time_pc)
print(f"Boot Time: {stp.hour}:{stp.minute}:{stp.second}")