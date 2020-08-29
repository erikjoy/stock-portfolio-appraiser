import yfinance


class PortfolioAppraiser:
    def __init__(self,
                 holdings,
                 cash_equivalents_percentage,
                 cash_equivalents_growth):
        self.holdings = holdings
        self.cash_equivalents_percentage = cash_equivalents_percentage
        self.cash_equivalents_growth = cash_equivalents_growth

    def calculate(self):
        holdings_data = yfinance.download(' '.join(tuple(self.holdings)), group_by='ticker', period='2d')
        if len(self.holdings) != len(holdings_data.columns) / 6:
            raise RateLimitError('Requests were rejected due to the rate and volume of recent requests')
        total_holdings_value = 0
        for symbol in self.holdings:
            stock_closing_data = holdings_data[symbol]['Close']
            closing_price_yesterday = float(stock_closing_data[0])
            closing_price_today = float(stock_closing_data[1])
            holding_percentage = self.holdings[symbol]
            current_holding_value = closing_price_today / closing_price_yesterday * holding_percentage
            total_holdings_value += current_holding_value
        total_holdings_value += self.cash_equivalents_percentage * self.cash_equivalents_growth
        return total_holdings_value - 100


class FundAppraiser(PortfolioAppraiser):
    def __init__(self, 
                 holdings,
                 cash_equivalents_percentage,
                 cash_equivalents_growth,
                 fund_symbol):
        super().__init__(holdings, cash_equivalents_percentage, cash_equivalents_growth)
        self.fund_symbol = fund_symbol

    def calculate(self):
        percentage_change = super().calculate()
        fund_data = yfinance.Ticker(self.fund_symbol)
        closing_price_data = fund_data.history(period='2d')['Close']
        if len(closing_price_data) == 0:
            raise RateLimitError('Requests were rejected due to the rate and volume of recent requests')
        last_closing_price = closing_price_data[0]
        fund_current_value = last_closing_price * (percentage_change + 100) / 100
        return (fund_current_value, percentage_change)


class RateLimitError(Exception):
    '''Raise when yfinance rejects requests due to the rate and volume of recent requests'''