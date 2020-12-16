import json, os, time, re





class memory:
    def quantity():
        dxdiag = "dxdiag /t dxdiag.txt"
        os.popen(dxdiag)
        with open('dxdiag.txt') as f:
            for line in f:
                if "Memory:" in line:
                    return str(line).replace('Memory:', '').replace('\n', '').replace(' ', '').replace('RAM', '')

    def clock():
        clock = 'wmic MEMORYCHIP get Speed'
        return os.popen(clock).read().split('\n\n')[1].replace(' ', '')
    def chip_manufacturer():
        manufacterer = 'wmic MEMORYCHIP get Manufacturer'
        return os.popen(manufacterer).read().split('\n\n')[1].replace('       ', '')      
    def partnumber():
        partnumber = 'wmic MEMORYCHIP get partnumber'
        return os.popen(partnumber).read().split('\n\n')[1].replace(' ', '')      









































