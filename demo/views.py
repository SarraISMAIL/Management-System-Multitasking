import json
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render,redirect
import psutil
from django.contrib import messages

def nots(request):
    context = {
        'title': 'Computer Specs',
        'processes': getProcessInfo(),
        'ram': getRamInfo()
    }
    return JsonResponse(context)

def coputerSpecs(request):
    context = {
        'title': 'Computer Specs',
        'disk': diskInfo(),
        'cpu': cpuInfo(),
        'ram': getRamInfo()
    }
    return render(request,'computer-spec.html',context)

def test(request):
    context = {
        'title': 'Computer Specs',
        'processes': getProcessInfo(),
        'ram': getRamInfo()
    }
    return render(request,'chart.html',context)

    
def index(request):
    context = {
        'title': 'Process Management System v1',
        'disk': diskInfo(),
        'cpu': cpuInfo(),
        'ram': getRamInfo(),
        'processes': getProcessInfo()
    }
    return render(request,'base.html',context)

def kill(request,id):
    print(f'Deleting process with pid = {id}')
    try:
        # p = psutil.Process(id)
        # p.terminate() 
        print("---> OK Process killed  ")
        context = {
            'type': 'success',
            'msg': "OK Process killed",
            'data': getProcessInfo()
        }
        return JsonResponse(context)
    except:
        print("---> Failed to kill Process ! ")
        context = {
            'type': 'warning',
            'msg': "Failed to kill Process",
            'data': getProcessInfo()
        }
        return JsonResponse(context)    

def kill_process(request,id):
    print(f'Deleting process with pid = {id}')
    try:
        p = psutil.Process(id)
        p.terminate() 
        print("---> OK Process killed  ")
        messages.success(request,"OK Process killed")
    except:
        print("---> Failed to kill Process ! ")
        messages.warning(request,"Failed to kill Process")
    return redirect('demo:index')

def diskInfo():
    # Hard disk info
    disk = psutil.disk_usage('/')
    totalDisk = round(disk[0] / float(2**30),2)
    usedDisk = round(disk[1] / float(2**30),2)
    freeDisk = round(disk[2] / float(2**30),2)
    freeDiskPercent = round(disk[3],2)
    # add cpu info : intel core i9 etc...
    str1 = usedDisk,
    str2 = freeDisk
    diskInfo = {
        'listVal':[usedDisk,freeDisk],
        'listLab':["Used","Free"],
        'total':totalDisk,
        'freePercent':freeDiskPercent,
        'used': usedDisk,
        'free':freeDisk
    }
    return diskInfo

def cpuInfo():
    cpuCount = psutil.cpu_count()
    phyCpuCount = psutil.cpu_count(logical=False)
    cpuFreq = round(psutil.cpu_freq()[2] / float(1000),2)
    cpuUsage = round(psutil.cpu_percent(interval=None),2)
    cpuLeft = round(100 - cpuUsage,2) #int= None just for last call
    #print(f'Total: {cpuCount}, phyiscal: {phyCpuCount}, max freq: {cpuFreq} GHz,cpu usage: {cpuUsage} %, left: {cpuLeftPercent} %')
    cpuInfo = {
        'listVal':[cpuUsage,cpuLeft],
        'listLab':["Used","Free"],
        'total':cpuCount,
        'physical':phyCpuCount,
        'freq':cpuFreq,
        'used':cpuUsage,
        'free':cpuLeft
    }
    return cpuInfo

def getRamInfo():
    totalRam = psutil.virtual_memory().total / (1024 ** 3)
    usedRam = psutil.virtual_memory().percent
    freeRam  = round(100 - usedRam,2)
    data =  {
        "total":round(totalRam,2),
        "used":usedRam,
        "free":freeRam
    }
    return data

def getProcessInfo():
    L = []
    for proc in psutil.process_iter():
        try:
            data = {
                'pid':proc.pid,
                'name':proc.name(),
                'status':proc.status(),
                'mem': round(proc.memory_percent(),2),
                'cpu': round(proc.cpu_percent(),2)
            }
            L.append(data)
        except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
            pass
    newlist = sorted(L, key=lambda d: d['mem'], reverse=True) 
    return newlist

