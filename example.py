from appraiser import PortfolioAppraiser, FundAppraiser

def main():
    mutual_fund = FundAppraiser(
        holdings={
            "MSFT": 7.9,
            "AAPL": 7.46,
            "AMZN": 4.71,
            "MA": 4.33,
            "ADBE": 4.32,
            "ASML": 3.98,
            "CRM": 3.59,
            "TXN": 3.38,
            "BABA": 2.94,
            "TSM": 2.78,
            "NVDA": 2.45,
            "LRCX": 2.41,
            "MCHP": 2.33,
            "V": 2.32,
            "FB": 2.27,
            "GOOGL": 2.19,
            "TCEHY": 2.13,
            "ZEN": 2.08,
            "CDNS": 2.06,
            "FIS": 2.02,
            "EQIX": 1.76,
            "NFLX": 1.64,
            "MU": 1.32,
            "AMT": 1.20,
            "ADSK": 1.10,
            "CCI": 1.08,
            "TEAM": 1.03,
            "KLAC": 1.03,
            "CSGP": 0.95,
            "AVLR": 0.93,
            "MELI": 0.92,
            "WIX": 0.81,
            "TMUS": 0.81,
            "XLNX": 0.78,
            "TYL": 0.75,
            "CNSWF": 0.71,
            "NICE": 0.64,
            "WDAY": 0.63,
            "MTCH": 0.60,
            "GDDY": 0.56,
            "TWLO": 0.55,
            "CGNX": 0.54,
            "GPN": 0.54,
            "PYPL": 0.51,
            "SAIL": 0.47,
            "INTU": 0.45,
            "LBRDA": 0.45,
            "MPNGF": 0.43,
            "ADYYF": 0.42,
            "GWRE": 0.42,
            "ETSY": 0.39,
            "RNG": 0.38,
            "RP": 0.38,
            "MDLA": 0.35,
            "WEX": 0.31,
            "CDAY": 0.29,
            "OKTA": 0.26,
            "NOW": 0.24,
            "PCTY": 0.20,
            "CREE": 0.14,
            "SLAB": 0.11
        },
        cash_equivalents_percentage=5.27,
        cash_equivalents_change=1.0,
        fund_symbol="JATAX"
    )
    fund_data = mutual_fund.calculate()
    display_results(fund_data, 'JATAX')

    tech_portfolio = PortfolioAppraiser(
        holdings={
            "AAPL": 10,
            "HNHPF": 10,
            "MSFT": 10,
            "DELL": 10,
            "SNE": 10,
            "IBM": 10,
            "INTC": 10,
            "PCRFY": 10,
            "HPQ": 10,
            "AMZN": 9
        },
        cash_equivalents_percentage=1.0,
        cash_equivalents_change=1.0
    )
    tech_data = tech_portfolio.calculate()
    display_results(tech_data, 'Tech Portfolio')

    airline_portfolio = PortfolioAppraiser(
        holdings={
            "DAL": 20,
            "AAL": 18,
            "UAL": 15,
            "LUV": 15,
            "JBLU": 15,
            "ALK": 15
        },
        cash_equivalents_percentage=2.0,
        cash_equivalents_change=1.0
    )
    airline_data = airline_portfolio.calculate()
    display_results(airline_data, 'Airline Portfolio')

    industrial_portfolio = PortfolioAppraiser(
        holdings={
            "LMT": 20,
            "RTX": 15,
            "GE": 10,
            "GD": 10,
            "SMGZY": 20,
            "RYCEY": 10,
            "HDS": 10
        },
        cash_equivalents_percentage=5.0,
        cash_equivalents_change=1.0
    )
    industrial_data = industrial_portfolio.calculate()
    display_results(industrial_data, 'Industrial Portfolio')

def display_results(data, title: str):
    if type(data) != float:
        print('%s\nPrice: $%.2f\nChange: %.2f%%\n' % (title, data[0], data[1]))
    else:
        print('%s\nChange: %.2f%%\n' % (title, data))

if __name__ == '__main__':
    main()