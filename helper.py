from json import load
from appraiser import FundAppraiser, PortfolioAppraiser


class ProcessConfig:
    def __init__(self, config_file_path):
        self.config = load(open(config_file_path, 'r'))

    def get_holdings_data(self):
        holdings = {}
        cash_equivalents_percentage, total_percentage = 0, 0
        with open(self.config['holdings_file_path'], 'r') as f:
            for line in f:
                (symbol, percentage) = line.split()
                percentage = float(percentage)
                total_percentage += percentage
                if symbol == self.config['cash_equivalents_name']:
                    cash_equivalents_percentage += percentage
                else:
                    holdings[symbol] = percentage
        if abs(total_percentage - 100) > 0.000001:
            raise HoldingsPercentageError('The percentages of the holdings don\'t sum up to 100')
        return (holdings, cash_equivalents_percentage)

    def select_appraiser(self):
        (holdings, cash_equivalents_percentage) = self.get_holdings_data()
        if self.config['is_fund']:
            return FundAppraiser(
                holdings,
                cash_equivalents_percentage,
                self.config['cash_equivalents_growth'],
                self.config['fund_symbol'])
        else:
            return PortfolioAppraiser(
                holdings,
                cash_equivalents_percentage,
                self.config['cash_equivalents_growth'])

    @staticmethod
    def auto_process(config_file_path):
        settings = ProcessConfig(config_file_path)
        return settings.select_appraiser()


class HoldingsPercentageError(Exception):
    '''Raise when the percentages of the holdings don't sum up to 100'''