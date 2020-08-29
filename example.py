from helper import ProcessConfig
from json import load

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

for i in arr:
    data = i.calculate()
    if type(data) != float:
        print('%s\nPrice: $%.2f\nChange: %.2f%%' % (i.fund_symbol, data[0], data[1]))
    else:
        print('Portfolio\nChange: %.2f%%' % data)