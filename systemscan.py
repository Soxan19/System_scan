from platform import *
from json import *
import shutil 
system_data = {
    "OS":{
        "Username":node(),
        "OS name":system(),
        "Machine type":machine(),
        "System`s version":version(),
        },
    "Disk":{
        "Total space(in GB)":round((shutil.disk_usage('/').total)/1024**3,2),
        "Used space(in GB)":round((shutil.disk_usage('/').used)/1024**3,2),
        "Free space(in GB)":round((shutil.disk_usage('/').free)/1024**3,2),
        },
    "Python":{
        "Python version": python_version(),
        "Python implementation": python_implementation(),
        }
}
with open("system_data.json ","w",encoding ="utf-8") as file:
    dump(system_data,file,indent = 4, ensure_ascii=False)