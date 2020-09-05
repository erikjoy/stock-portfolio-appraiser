import yfinance


class PortfolioAppraiser:
    def __init__(self,
                 holdings: dict,
                 cash_equivalents_percentage: float,
                 cash_equivalents_change: float):
        PortfolioAppraiser._validate_percentages(holdings, cash_equivalents_percentage)
        self.holdings = holdings
        self.cash_equivalents_percentage = cash_equivalents_percentage
        self.cash_equivalents_change = cash_equivalents_change

    def calculate(self):
        holdings_data = yfinance.download(' '.join(tuple(self.holdings)), group_by='ticker', period='2d')
        if len(holdings_data.columns) / 6 == 1:
            symbol = tuple(self.holdings)[0]
            total_holdings_value = self._assist_calculate(holdings_data['Close'], symbol)
        else:
            total_holdings_value = 0
            for symbol in self.holdings:
                stock_closing_data = holdings_data[symbol]['Close']
                total_holdings_value += self._assist_calculate(stock_closing_data, symbol)
        total_holdings_value += self.cash_equivalents_percentage * self.cash_equivalents_change
        return total_holdings_value - 100

    def _assist_calculate(self, data, symbol):
        closing_price_yesterday = float(data[0])
        closing_price_today = float(data[2]) if (len(data) == 3 and data[1] != data[1]) else float(data[1])
        holding_percentage = self.holdings[symbol]
        current_holding_value = closing_price_today / closing_price_yesterday * holding_percentage
        return current_holding_value

    @staticmethod
    def _validate_percentages(holdings, cash_equivalents_percentage):
        total_percentage = 0
        for percentage in holdings.values():
            total_percentage += percentage
        total_percentage += cash_equivalents_percentage
        if abs(total_percentage - 100) > 0.000001:
            raise HoldingsPercentageError('The percentages of the holdings don\'t sum up to 100')

class FundAppraiser(PortfolioAppraiser):
    def __init__(self, 
                 holdings: dict,
                 cash_equivalents_percentage: float,
                 cash_equivalents_change: float,
                 fund_symbol: str):
        super().__init__(holdings, cash_equivalents_percentage, cash_equivalents_change)
        self.fund_symbol = fund_symbol

    def calculate(self):
        percentage_change = super().calculate()
        fund_data = yfinance.Ticker(self.fund_symbol)
        closing_price_data = fund_data.history(period='2d')['Close']
        last_closing_price = closing_price_data[0]
        fund_current_value = last_closing_price * (percentage_change + 100) / 100
        return (fund_current_value, percentage_change)


class HoldingsPercentageError(Exception):
    '''Raise when the percentages of the holdings don't sum up to 100'''