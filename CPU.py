import wmi, os, psutil, cpuinfo

global computer
computer = wmi.WMI()

class processor:
    def name():
        cpu = computer.Win32_Processor()[0]
        return cpu.Name
    def base():
        return cpuinfo.get_cpu_info()['hz_advertised_friendly']
    def boost():
        return cpuinfo.get_cpu_info()['hz_actual_friendly']
    def cores():
        return psutil.cpu_count(logical=False)
    def threads():
        return psutil.cpu_count()
    def socket():
        socket = "wmic cpu get SocketDesignation"
        return os.popen(socket).read().split('\n\n')[1].split('\n\n\n\n')[0].replace(' ', '')
    def clock():
        return '{}'.format(psutil.cpu_freq()).split('current=')[1].split(',')[0]
    def market():
        market = "wmic cpu get AssetTag"
        return os.popen(market).read().split('\n\n')[1].split('             \n\n\n\n')[0]

    def percentage():
        percentage = "wmic cpu get loadPercentage"
        return str(os.popen(percentage).read().split('\n\n')[1].split('\n\n\n\n')).replace(' ', '')
     
