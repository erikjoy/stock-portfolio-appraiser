from json import load
from appraiser import FundAppraiser, PortfolioAppraiser


class ProcessConfig:
    @staticmethod
    def _get_holdings_data(config):
        holdings = {}
        cash_equivalents_percentage, total_percentage = 0, 0
        with open(config['holdings_file_path'], 'r') as f:
            for line in f:
                (symbol, percentage) = line.split()
                percentage = float(percentage)
                total_percentage += percentage
                if symbol == config['cash_equivalents_name']:
                    cash_equivalents_percentage += percentage
                else:
                    holdings[symbol] = percentage
        if abs(total_percentage - 100) > 0.000001:
            raise HoldingsPercentageError('The percentages of the holdings don\'t sum up to 100')
        return (holdings, cash_equivalents_percentage)

    @staticmethod
    def _select_appraiser(config):
        (holdings, cash_equivalents_percentage) = ProcessConfig._get_holdings_data(config)
        if config['is_fund']:
            return FundAppraiser(
                holdings,
                cash_equivalents_percentage,
                config['cash_equivalents_growth'],
                config['fund_symbol'])
        else:
            return PortfolioAppraiser(
                holdings,
                cash_equivalents_percentage,
                config['cash_equivalents_growth'])

    @staticmethod
    def process(config):
        return ProcessConfig._select_appraiser(config)

    @staticmethod
    def process_path(config_file_path):
        config = load(open(config_file_path, 'r'))
        return ProcessConfig.process(config)


class HoldingsPercentageError(Exception):
    '''Raise when the percentages of the holdings don't sum up to 100'''