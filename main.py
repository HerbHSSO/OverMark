from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QTextEdit
from PyQt5 import uic
import sys
from CPU import *
from GPU import *
from RAM import *
from System import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont
import time
from PyQt5.QtCore import QTimer, QTime
import os


class OverMark(QWidget):
    def __init__(self):
        super().__init__()
        self.main_window = uic.loadUi('Designer/main.ui', self)

#CPU logos =========================================================================================================================================================================================
        try:
            self.main_window.cpu.setText(processor.name().split('Core(TM) ')[1].split(' CPU')[0])
        except:
            try:
                self.main_window.cpu.setText(processor.name()[4:17])
            except:
                self.main_window.cpu.setText(processor.name())
        
             
        
        try:
            processor.name().find('intel')
            pixmap = QPixmap('Designer/intel.png')
            self.main_window.logo.setPixmap(pixmap)
            self.main_window.logo.setScaledContents(True)
            
        except:
            try:
                processor.name().find('AMD')
                pixmap = QPixmap('Designer/AMD.png')
                self.main_window.logo.setPixmap(pixmap)
                self.main_window.logo.setScaledContents(True)
            except:
                None
#Main Window configs ======================================================================================================           
        self.main_window.cpu.adjustSize()
        self.main_window.specification.setText(processor.name().replace('(TM)', '™').replace('(R)', '®'))
        self.main_window.cores.setText('{}'.format(processor.cores()))
        self.main_window.threads.setText('{}'.format(processor.threads()))
        self.main_window.clockBase.setText('{}'.format(processor.base()))
        self.main_window.clockBoost.setText('{}'.format(processor.boost()))
        self.main_window.socket.setText('{}'.format(processor.socket()))        
        self.main_window.current.setText('{} GHz'.format(processor.clock()))
        self.main_window.market.setText('{}'.format(processor.market()))
        self.main_window.gpu.setText('{}'.format(videocard.name()))
        self.main_window.gpu.adjustSize()
        self.main_window.specification_2.setText('{}'.format(videocard.name()))
        self.main_window.gpu_boost.setText('{}'.format(videocard.max_clock()))
        self.main_window.driver.setText('{}'.format(videocard.driver()))
        if 'Radeon' in videocard.name():
            self.main_window.setofcores.setText('C.Us:')
            self.main_window.setofcores_2.setText('{}'.format(videocard.compute_units()))
        elif 'GeForce' in videocard.name():
            self.main_window.setofcores.setText('S.Ms:')
            self.main_window.setofcores_2.setText('{}'.format(videocard.compute_units()))
        else:
            self.main_window.setofcores.setText('C.Us:')
            self.main_window.setofcores_2.setText('{}'.format(videocard.compute_units()))
        self.main_window.gpu_cores.setText('{}'.format(videocard.cores()))
        self.main_window.teraflops.setText('{}'.format(videocard.teraflops()))
        self.main_window.type.setText('{}'.format(videocard.type()))
        self.main_window.vram.setText('{}'.format(videocard.vram()))
        self.main_window.current_2.setText('{}'.format(videocard.clock()))
        self.main_window.quantity.setText('{}'.format(memory.quantity()))
        self.main_window.memory_clock.setText('{}MHz'.format(memory.clock()))
        self.main_window.manufacturer_chip.setText('{}'.format(memory.chip_manufacturer()))
        self.main_window.partnumber.setText('{}'.format(memory.partnumber()))
#OS Logos ======================================================================================================================================================
        if 'Windows' in OperationSystem.OS():
            
            self.main_window.system_name.setText('Windows 10')
            windows10 = QPixmap('Designer/Windows-10.png')
            self.main_window.logo_system.setPixmap(windows10)
            self.main_window.logo_system.setScaledContents(True)
        if "Intel" in videocard.name():
            intel_graphics = QPixmap('Designer/intel.png')
            self.main_window.logo_gpu.setPixmap(intel_graphics)
            self.main_window.logo_gpu.setScaledContents(True)
        self.main_window.specification_system.setText('{}'.format(OperationSystem.OS()))
        self.main_window.version_system.setText('{}'.format(OperationSystem.version()))
        self.main_window.bios_name.setText('{}'.format(OperationSystem.bios()))
        self.main_window.manufacturer.setText('{}'.format(OperationSystem.manufacturer()))
        

        if "RX580" in videocard.name():
            self.main_window.gpu_cores.setText('2304')

        self.main_window.show()

  

            

        


        self.timer = QTimer()
        self.timer.timeout.connect(self.percentage_update)
        self.timer.start(5000)
        
    def percentage_update(self):
        self.main_window.percentage.setText('{}%'.format(processor.percentage().replace('[]', '').replace("''", "")))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OverMark()
    app.exec_()
    
