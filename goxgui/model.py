import abc

from PyQt4.QtCore import QAbstractTableModel
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QVariant
from PyQt4.QtCore import SIGNAL
from market import Market
from preferences import Preferences


class Model(QAbstractTableModel):
    '''
    Model representing a collection of orders.
    '''

    def __init__(self, parent):
        QAbstractTableModel.__init__(self, parent)

    # private methods

    def _slot_changed(self):
        self.emit(SIGNAL("layoutChanged()"))

    @abc.abstractmethod
    def _get_header(self):
        pass

    # Qt methods

    @abc.abstractmethod
    def rowCount(self, parent):
        pass

    def columnCount(self, parent):
        return len(self._get_header())

    def data(self, index, role):

        if role == Qt.TextAlignmentRole:
            return Qt.AlignRight | Qt.AlignVCenter

        if (not index.isValid()) or (role != Qt.DisplayRole):
            return QVariant()

        row = index.row()
        col = index.column()

        if col == 0:
            return QVariant(str(self.get_price(row)))
        if col == 1:
            return QVariant(str(self.get_size(row)))

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self._get_header()[col])
        return QVariant()

    # public methods

    @abc.abstractmethod
    def get_price(self, index):
        pass

    @abc.abstractmethod
    def get_size(self, index):
        pass


class ModelBid(Model):

    def __init__(self, parent, market, preferences):
        Model.__init__(self, parent)
        self.__market = market
        self.__preferences = preferences
        self.__market.signal_orderbook_changed.connect(self._slot_changed)

    def _get_header(self):
        symbolQuote = self.__preferences.get_currency(
            Preferences.CURRENCY_INDEX_QUOTE).symbol
        symbolBase = self.__preferences.get_currency(
            Preferences.CURRENCY_INDEX_BASE).symbol
        return ['Bid ' + symbolQuote, 'Size ' + symbolBase]

    def get_price(self, index):
        return self.__market.get_order(Market.ORDER_TYPE_BID, index)[0]

    def get_size(self, index):
        return self.__market.get_order(Market.ORDER_TYPE_BID, index)[1]

    def rowCount(self, parent):
        return self.__market.get_order_count(Market.ORDER_TYPE_BID)


class ModelAsk(Model):

    def __init__(self, parent, market, preferences):
        Model.__init__(self, parent)
        self.__market = market
        self.__preferences = preferences
        self.__market.signal_orderbook_changed.connect(self._slot_changed)

    def _get_header(self):
        symbolQuote = self.__preferences.get_currency(
            Preferences.CURRENCY_INDEX_QUOTE).symbol
        symbolBase = self.__preferences.get_currency(
            Preferences.CURRENCY_INDEX_BASE).symbol
        return ['Ask ' + symbolQuote, 'Size ' + symbolBase]

    def get_price(self, index):
        return self.__market.get_order(Market.ORDER_TYPE_ASK, index)[0]

    def get_size(self, index):
        return self.__market.get_order(Market.ORDER_TYPE_ASK, index)[1]

    def rowCount(self, parent):
        return self.__market.get_order_count(Market.ORDER_TYPE_ASK)
