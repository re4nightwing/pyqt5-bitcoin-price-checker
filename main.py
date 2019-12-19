import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLineEdit,QVBoxLayout,QLayout,QPushButton,QHBoxLayout,QComboBox,QMainWindow
from PyQt5 import QtGui
from main_window import Ui_MainWindow
import requests
import re

app = QApplication(sys.argv)


class RealMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setup_slots(self):
        self.updateButton.released.connect(self.get_price)
        self.first_run()

    def get_price(self) :
        coin_name = self.btc_list.currentText()
        btc_price = requests.get('https://api.bittrex.com/v3/markets/tickers').json()
        {'symbol': 'BTC-USD', 'lastTradeRate': '6979.99200000', 'bidRate': '6961.95200000', 'askRate': '6961.95300000'}

        for d in btc_price:
            if re.search('.+-US.', coin_name) :
                if re.search('.+-USDT', coin_name):
                    if d['symbol'] == coin_name :
                        #result = float(d['lastTradeRate'])
                        self.bitcoinLabel.setText('Price(USDT) : ')
                        self.bitcoinPriceShow.setText(d['lastTradeRate'])
                        break
                else :
                    if d['symbol'] == coin_name :
                        #result = float(d['lastTradeRate'])
                        self.bitcoinLabel.setText('Price(USD) : ')
                        self.bitcoinPriceShow.setText(d['lastTradeRate'])
                        break 
            elif re.search('.+-BTC', coin_name) :
                if d['symbol'] == coin_name :
                    #result = float(d['lastTradeRate'])
                    self.bitcoinLabel.setText('Price(BTC) : ')
                    self.bitcoinPriceShow.setText(d['lastTradeRate'])
                    break
            elif re.search('.+-ETH', coin_name) :
                if d['symbol'] == coin_name :
                    #result = float(d['lastTradeRate'])
                    self.bitcoinLabel.setText('Price(ETH) : ')
                    self.bitcoinPriceShow.setText(d['lastTradeRate'])
                    break

    def first_run(self):
        new_list = []
        btc_price = requests.get('https://api.bittrex.com/v3/markets/tickers').json()

        for i in btc_price:
            new_list.append(i['symbol'])
        new_list.sort()
        self.btc_list.addItems(new_list)



MainWindow = QMainWindow()
ui = RealMainWindow()
ui.setupUi(MainWindow)
ui.setup_slots()
MainWindow.show()


sys.exit(app.exec_())
