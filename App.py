# -*- coding: utf-8 -*-
'''
Created on Jun 12, 2019

@author: yl
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from demo import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.Qt import pyqtSlot

items = ["水果", "主食", "蔬菜", '肉','豆制品','奶']
factors = [1,2,0.5,2,0.5,1]

class MyWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        
        self.items = []
        self.factors = []
        self.amounts = []
        
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        self.comboBox_food.addItems(items)
        self.comboBox_food.setCurrentIndex(2)   # 设置默认值
#         self.comboBox.currentText()   # 获得当前内容
        self.comboBox_food.currentIndexChanged.connect(self.select_item)
        self.doubleSpinBox_amount.valueChanged.connect(self.select_amount)
        
        self.pushButton_add.clicked.connect(self.add_item)
        self.pushButton_del.clicked.connect(self.delete_item)
        self.pushButton_clr.clicked.connect(self.clear_item)
    
    @pyqtSlot(int)
    def lcd_heat(self, heat):
        self.lcdNumber_heat.display(heat)
        
    def calculate(self):
        self.total_heat = 0
        for self.i in range(len(self.factors)):
            self.item_heat = self.factors[self.i] * self.amounts[self.i]
            self.total_heat += self.item_heat
        print(self.total_heat)
        self.lcd_heat(self.total_heat)
        return self.total_heat
        
    def select_item(self):
        return self.comboBox_food.currentText() 
    
    def select_factor(self):
        self.index = items.index(self.select_item())
        return factors[self.index]

    def select_amount(self):
        return self.doubleSpinBox_amount.value()
    
    def table_writeline(self, k):
#         print(self.items)
#         print(self.factors)
#         print(self.amounts)
        self.tableWidget.setItem(k,0,QTableWidgetItem(self.items[k]))
        self.tableWidget.setItem(k,1,QTableWidgetItem(str(self.factors[k])))
        self.tableWidget.setItem(k,2,QTableWidgetItem(str(self.amounts[k])))
    
    def add_item(self):
        if self.select_amount() >= 0:
            self.items.append(self.select_item())
            self.factors.append(self.select_factor())
            self.amounts.append(self.select_amount())
        self.calculate()
#         self.rowcount = self.rowCount()
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.table_writeline(len(self.items)-1)
        
    def delete_item(self):
        self.items.pop()
        self.factors.pop()
        self.amounts.pop()
        self.tableWidget.removeRow(len(self.items)-1)   
        self.calculate()
        
    def clear_item(self):
        self.items.clear()
        self.amounts.clear()
        self.factors.clear()
        self.tableWidget.clearContents()
        self.calculate()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
