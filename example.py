from helper import ProcessConfig

arr = []

jatax = ProcessConfig.auto_process('example/jatax/jatax_config.json')
arr.append(jatax)

tech_portfolio = ProcessConfig.auto_process('example/tech/tech_config.json')
arr.append(tech_portfolio)

airline_portfolio = ProcessConfig.auto_process('example/airline/airline_config.json')
arr.append(airline_portfolio)

for i in arr:
    data = i.calculate()
    if type(data) != float:
        print('%s\nPrice: $%.2f\nChange: %.2f%%' % (i.fund_symbol, data[0], data[1]))
    else:
        print('Portfolio\nChange: %.2f%%' % data)