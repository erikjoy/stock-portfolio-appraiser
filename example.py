from helper import ProcessConfig
from json import load
from appraiser import PortfolioAppraiser

arr = []

#Option 1
jatax_fund = ProcessConfig.process_path('example/jatax/jatax_config.json')
arr.append(jatax_fund)

#Option 2
tech_config = load(open('example/tech/tech_config.json', 'r'))
tech_portfolio = ProcessConfig.process(tech_config)
arr.append(tech_portfolio)

#Option 3
airline_config = {
    "holdings_file_path": "example/airline/airline_holdings.txt",
    "is_fund": False,
    "fund_symbol": "n/a",
    "cash_equivalents_name": "CASHEQUIV",
    "cash_equivalents_growth": 1.0
}
airline_portfolio = ProcessConfig.process(airline_config)
arr.append(airline_portfolio)

#Option 4
industrial_holdings = {
    "LMT": 20,
    "RTX": 15,
    "GE": 10,
    "GD": 10,
    "SMGZY": 20,
    "RYCEY": 10,
    "HDS": 10
}
industrial_portfolio = PortfolioAppraiser(
    holdings=industrial_holdings,
    cash_equivalents_percentage=5,
    cash_equivalents_growth=1.0)
arr.append(industrial_portfolio)

for i in arr:
    data = i.calculate()
    if type(data) != float:
        print('%s\nPrice: $%.2f\nChange: %.2f%%\n' % (i.fund_symbol, data[0], data[1]))
    else:
        print('Portfolio\nChange: %.2f%%\n' % data)