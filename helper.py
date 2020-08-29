from json import load
from appraiser import FundAppraiser, PortfolioAppraiser


class ProcessConfig:
    @staticmethod
    def _get_holdings_data(config):
        holdings = {}
        cash_equivalents_percentage, total_percentage = 0, 0
        holdings_list = open(config['holdings_file_path'], 'r')
        for i in holdings_list:
            (symbol, percentage) = i.split()
            percentage = float(percentage)
            total_percentage += percentage
            if symbol == config['cash_equivalents_name']:
                cash_equivalents_percentage += percentage
            else:
                holdings[symbol] = percentage
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