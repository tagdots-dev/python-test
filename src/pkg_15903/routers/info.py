import psutil
from fastapi import APIRouter
from fastapi_health import health


def get_system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    load_avg = psutil.getloadavg()

    system_info = {}
    if any([isinstance(cpu_usage, float) and cpu_usage > 95, mem_usage > 95, disk_usage > 80]):
        system_info["status"] = "warning"
    else:
        system_info["status"] = "healthy"
    system_info_system = {
        "cpu_usage": f'{cpu_usage}%',
        "mem_usage": f'{mem_usage}%',
        "disk_usage": f'{disk_usage}%',
        "load_avg": {
            "1 min": f'{load_avg[0]:.3}',
            "5 min": f'{load_avg[1]:.3}',
            "15 min": f'{load_avg[2]:.3}'
        }
    }
    system_info['system'] = system_info_system
    return system_info


router = APIRouter()
router.add_api_route(
    "/info",
    health([get_system_info]),
    tags=["system info"],
    summary="Get System Info"
)
