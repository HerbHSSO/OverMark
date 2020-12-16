import json, os, time, re




class OperationSystem:
    def OS():
        dxdiag = "dxdiag /t dxdiag.txt"
        os.popen(dxdiag)
        with open('dxdiag.txt') as f:
            for line in f:
                if "Operating System:" in line:
                    return str(line).replace('Operating System:', '').replace('\n', '').split('(')[0].replace('          ', '')
    
    def version():
        dxdiag = "dxdiag /t dxdiag.txt"
        os.popen(dxdiag)
        with open('dxdiag.txt') as f:
            for line in f:
                if "Operating System:" in line:
                    return str(line).replace('Operating System:', '').replace('\n', '').replace('          ', '').split('(')[1].replace(')', '')
    
    def bios():
        dxdiag = "dxdiag /t dxdiag.txt"
        os.popen(dxdiag)
        with open('dxdiag.txt') as f:
            for line in f:
                if "BIOS:" in line:
                    return str(line).replace('BIOS:', '').replace('\n', '').replace('           ', '')
    
    def manufacturer():
        dxdiag = "dxdiag /t dxdiag.txt"
        os.popen(dxdiag)
        with open('dxdiag.txt') as f:
            for line in f:
                if "System Manufacturer:" in line:
                    return str(line).replace('System Manufacturer:', '').replace('\n', '').replace('           ', '').replace('       ', '')
