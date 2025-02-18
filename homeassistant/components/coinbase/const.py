"""Constants used for Coinbase."""

ACCOUNT_IS_VAULT = "is_vault"

CONF_CURRENCIES = "account_balance_currencies"
CONF_EXCHANGE_BASE = "exchange_base"
CONF_EXCHANGE_RATES = "exchange_rate_currencies"
CONF_EXCHANGE_PRECISION = "exchange_rate_precision"
CONF_EXCHANGE_PRECISION_DEFAULT = 2
CONF_TITLE = "title"
DOMAIN = "coinbase"

# Constants for data returned by Coinbase API
API_ACCOUNT_AMOUNT = "amount"
API_ACCOUNT_AVALIABLE = "available_balance"
API_ACCOUNT_BALANCE = "balance"
API_ACCOUNT_CURRENCY = "currency"
API_ACCOUNT_CURRENCY_CODE = "code"
API_ACCOUNT_HOLD = "hold"
API_ACCOUNT_ID = "id"
API_ACCOUNT_NATIVE_BALANCE = "balance"
API_ACCOUNT_NAME = "name"
API_ACCOUNT_VALUE = "value"
API_ACCOUNTS = "accounts"
API_DATA = "data"
API_RATES = "rates"
API_RATES_CURRENCY = "currency"
API_RESOURCE_PATH = "resource_path"
API_RESOURCE_TYPE = "type"
API_TYPE_VAULT = "vault"
API_USD = "USD"
API_V3_ACCOUNT_ID = "uuid"
API_V3_TYPE_VAULT = "ACCOUNT_TYPE_VAULT"

WALLETS = {
    "1INCH": "1INCH",
    "AAVE": "AAVE",
    "ADA": "ADA",
    "AED": "AED",
    "AFN": "AFN",
    "ALGO": "ALGO",
    "ALL": "ALL",
    "AMD": "AMD",
    "AMP": "AMP",
    "ANG": "ANG",
    "ANKR": "ANKR",
    "AOA": "AOA",
    "ARS": "ARS",
    "ATOM": "ATOM",
    "AUCTION": "AUCTION",
    "AUD": "AUD",
    "AWG": "AWG",
    "AZN": "AZN",
    "BAL": "BAL",
    "BAM": "BAM",
    "BAND": "BAND",
    "BAT": "BAT",
    "BBD": "BBD",
    "BCH": "BCH",
    "BDT": "BDT",
    "BGN": "BGN",
    "BHD": "BHD",
    "BIF": "BIF",
    "BMD": "BMD",
    "BND": "BND",
    "BNT": "BNT",
    "BOB": "BOB",
    "BOND": "BOND",
    "BRL": "BRL",
    "BSD": "BSD",
    "BSV": "BSV",
    "BTC": "BTC",
    "BTN": "BTN",
    "BWP": "BWP",
    "BYN": "BYN",
    "BYR": "BYR",
    "BZD": "BZD",
    "CAD": "CAD",
    "CDF": "CDF",
    "CGLD": "CGLD",
    "CHF": "CHF",
    "CHZ": "CHZ",
    "CLF": "CLF",
    "CLP": "CLP",
    "CLV": "CLV",
    "CNH": "CNH",
    "CNY": "CNY",
    "COMP": "COMP",
    "COP": "COP",
    "CRC": "CRC",
    "CRV": "CRV",
    "CTSI": "CTSI",
    "CUC": "CUC",
    "CVC": "CVC",
    "CVE": "CVE",
    "CZK": "CZK",
    "DAI": "DAI",
    "DASH": "DASH",
    "DJF": "DJF",
    "DKK": "DKK",
    "DNT": "DNT",
    "DOGE": "DOGE",
    "DOP": "DOP",
    "DOT": "DOT",
    "DZD": "DZD",
    "EGP": "EGP",
    "ENJ": "ENJ",
    "EOS": "EOS",
    "ERN": "ERN",
    "ETB": "ETB",
    "ETC": "ETC",
    "ETH": "ETH",
    "ETH2": "ETH2",
    "EUR": "EUR",
    "FET": "FET",
    "FIL": "FIL",
    "FJD": "FJD",
    "FKP": "FKP",
    "FORTH": "FORTH",
    "GALA": "GALA",
    "GBP": "GBP",
    "GBX": "GBX",
    "GEL": "GEL",
    "GGP": "GGP",
    "GHS": "GHS",
    "GIP": "GIP",
    "GMD": "GMD",
    "GNF": "GNF",
    "GRT": "GRT",
    "GTC": "GTC",
    "GTQ": "GTQ",
    "GYD": "GYD",
    "HKD": "HKD",
    "HNL": "HNL",
    "HNT": "HNT",
    "HRK": "HRK",
    "HTG": "HTG",
    "HUF": "HUF",
    "ICP": "ICP",
    "IDR": "IDR",
    "ILS": "ILS",
    "IMP": "IMP",
    "INR": "INR",
    "IQD": "IQD",
    "ISK": "ISK",
    "JEP": "JEP",
    "JMD": "JMD",
    "JOD": "JOD",
    "JPY": "JPY",
    "KEEP": "KEEP",
    "KES": "KES",
    "KGS": "KGS",
    "KHR": "KHR",
    "KMF": "KMF",
    "KNC": "KNC",
    "KRW": "KRW",
    "KWD": "KWD",
    "KYD": "KYD",
    "KZT": "KZT",
    "LAK": "LAK",
    "LBP": "LBP",
    "LINK": "LINK",
    "LKR": "LKR",
    "LPT": "LPT",
    "LRC": "LRC",
    "LRD": "LRD",
    "LSL": "LSL",
    "LTC": "LTC",
    "LYD": "LYD",
    "MAD": "MAD",
    "MANA": "MANA",
    "MASK": "MASK",
    "MATIC": "MATIC",
    "MDL": "MDL",
    "MGA": "MGA",
    "MIR": "MIR",
    "MKD": "MKD",
    "MKR": "MKR",
    "MLN": "MLN",
    "MMK": "MMK",
    "MNT": "MNT",
    "MOP": "MOP",
    "MRO": "MRO",
    "MTL": "MTL",
    "MUR": "MUR",
    "MVR": "MVR",
    "MWK": "MWK",
    "MXN": "MXN",
    "MYR": "MYR",
    "MZN": "MZN",
    "NAD": "NAD",
    "NGN": "NGN",
    "NIO": "NIO",
    "NKN": "NKN",
    "NMR": "NMR",
    "NOK": "NOK",
    "NPR": "NPR",
    "NU": "NU",
    "NZD": "NZD",
    "OGN": "OGN",
    "OMG": "OMG",
    "OMR": "OMR",
    "OXT": "OXT",
    "PAB": "PAB",
    "PEN": "PEN",
    "PGK": "PGK",
    "PHP": "PHP",
    "PKR": "PKR",
    "PLN": "PLN",
    "POLY": "POLY",
    "PYG": "PYG",
    "QAR": "QAR",
    "QNT": "QNT",
    "RLY": "RLY",
    "REN": "REN",
    "REP": "REP",
    "REPV2": "REPV2",
    "RLC": "RLC",
    "RON": "RON",
    "RSD": "RSD",
    "RUB": "RUB",
    "RWF": "RWF",
    "SAR": "SAR",
    "SBD": "SBD",
    "SCR": "SCR",
    "SEK": "SEK",
    "SGD": "SGD",
    "SHIB": "SHIB",
    "SHP": "SHP",
    "SKL": "SKL",
    "SLL": "SLL",
    "SNX": "SNX",
    "SOL": "SOL",
    "SOS": "SOS",
    "SRD": "SRD",
    "SSP": "SSP",
    "STD": "STD",
    "STORJ": "STORJ",
    "SUSHI": "SUSHI",
    "SVC": "SVC",
    "SZL": "SZL",
    "THB": "THB",
    "TJS": "TJS",
    "TMM": "TMM",
    "TMT": "TMT",
    "TND": "TND",
    "TOP": "TOP",
    "TRB": "TRB",
    "TRY": "TRY",
    "TTD": "TTD",
    "TWD": "TWD",
    "TZS": "TZS",
    "UAH": "UAH",
    "UGX": "UGX",
    "UMA": "UMA",
    "UNI": "UNI",
    "USD": "USD",
    "USDC": "USDC",
    "USDT": "USDT",
    "UYU": "UYU",
    "UZS": "UZS",
    "VES": "VES",
    "VND": "VND",
    "VUV": "VUV",
    "WBTC": "WBTC",
    "WST": "WST",
    "XAF": "XAF",
    "XAG": "XAG",
    "XAU": "XAU",
    "XCD": "XCD",
    "XDR": "XDR",
    "XLM": "XLM",
    "XOF": "XOF",
    "XPD": "XPD",
    "XPF": "XPF",
    "XPT": "XPT",
    "XRP": "XRP",
    "XTZ": "XTZ",
    "YER": "YER",
    "YFI": "YFI",
    "ZAR": "ZAR",  # codespell:ignore zar
    "ZEC": "ZEC",
    "ZMW": "ZMW",
    "ZRX": "ZRX",
    "ZWL": "ZWL",
}

RATES = {
    "1INCH": "1INCH",
    "AAVE": "AAVE",
    "ACH": "ACH",
    "ADA": "ADA",
    "AED": "AED",
    "AFN": "AFN",
    "AGLD": "AGLD",
    "ALCX": "ALCX",
    "ALGO": "ALGO",
    "ALL": "ALL",
    "AMD": "AMD",
    "AMP": "AMP",
    "ANG": "ANG",
    "ANKR": "ANKR",
    "AOA": "AOA",
    "API3": "API3",
    "ARPA": "ARPA",
    "ARS": "ARS",
    "ASM": "ASM",
    "ATOM": "ATOM",
    "AUCTION": "AUCTION",
    "AUD": "AUD",
    "AVAX": "AVAX",
    "AWG": "AWG",
    "AXS": "AXS",
    "AZN": "AZN",
    "BADGER": "BADGER",
    "BAL": "BAL",
    "BAM": "BAM",
    "BAND": "BAND",
    "BAT": "BAT",
    "BBD": "BBD",
    "BCH": "BCH",
    "BDT": "BDT",
    "BGN": "BGN",
    "BHD": "BHD",
    "BICO": "BICO",
    "BIF": "BIF",
    "BLZ": "BLZ",
    "BMD": "BMD",
    "BND": "BND",
    "BNT": "BNT",
    "BOB": "BOB",
    "BOND": "BOND",
    "BRL": "BRL",
    "BSD": "BSD",
    "BSV": "BSV",
    "BTC": "BTC",
    "BTN": "BTN",
    "BTRST": "BTRST",
    "BWP": "BWP",
    "BYN": "BYN",
    "BYR": "BYR",
    "BZD": "BZD",
    "CAD": "CAD",
    "CDF": "CDF",
    "CGLD": "CGLD",
    "CHF": "CHF",
    "CHZ": "CHZ",
    "CLF": "CLF",
    "CLP": "CLP",
    "CLV": "CLV",
    "CNH": "CNH",
    "CNY": "CNY",
    "COMP": "COMP",
    "COP": "COP",
    "COTI": "COTI",
    "COVAL": "COVAL",
    "CRC": "CRC",
    "CRO": "CRO",
    "CRV": "CRV",
    "CTSI": "CTSI",
    "CTX": "CTX",
    "CUC": "CUC",
    "CVC": "CVC",
    "CVE": "CVE",
    "CZK": "CZK",
    "DAI": "DAI",
    "DASH": "DASH",
    "DDX": "DDX",
    "DESO": "DESO",
    "DIA": "DIA",
    "DJF": "DJF",
    "DKK": "DKK",
    "DNT": "DNT",
    "DOGE": "DOGE",
    "DOP": "DOP",
    "DOT": "DOT",
    "DZD": "DZD",
    "EGP": "EGP",
    "ENJ": "ENJ",
    "ENS": "ENS",
    "EOS": "EOS",
    "ERN": "ERN",
    "ETB": "ETB",
    "ETC": "ETC",
    "ETH": "ETH",
    "ETH2": "ETH2",
    "EUR": "EUR",
    "FARM": "FARM",
    "FET": "FET",
    "FIL": "FIL",
    "FJD": "FJD",
    "FKP": "FKP",
    "FORTH": "FORTH",
    "FOX": "FOX",
    "FX": "FX",
    "GALA": "GALA",
    "GBP": "GBP",
    "GBX": "GBX",
    "GEL": "GEL",
    "GFI": "GFI",
    "GGP": "GGP",
    "GHS": "GHS",
    "GIP": "GIP",
    "GMD": "GMD",
    "GNF": "GNF",
    "GODS": "GODS",
    "GRT": "GRT",
    "GTC": "GTC",
    "GTQ": "GTQ",
    "GYD": "GYD",
    "GYEN": "GYEN",
    "HKD": "HKD",
    "HNL": "HNL",
    "HNT": "HNT",
    "HRK": "HRK",
    "HTG": "HTG",
    "HUF": "HUF",
    "ICP": "ICP",
    "IDEX": "IDEX",
    "IDR": "IDR",
    "ILS": "ILS",
    "IMP": "IMP",
    "IMX": "IMX",
    "INR": "INR",
    "INV": "INV",
    "IOTX": "IOTX",
    "IQD": "IQD",
    "ISK": "ISK",
    "JASMY": "JASMY",
    "JEP": "JEP",
    "JMD": "JMD",
    "JOD": "JOD",
    "JPY": "JPY",
    "KEEP": "KEEP",
    "KES": "KES",
    "KGS": "KGS",
    "KHR": "KHR",
    "KMF": "KMF",
    "KNC": "KNC",
    "KRL": "KRL",
    "KRW": "KRW",
    "KWD": "KWD",
    "KYD": "KYD",
    "KZT": "KZT",
    "LAK": "LAK",
    "LBP": "LBP",
    "LCX": "LCX",
    "LINK": "LINK",
    "LKR": "LKR",
    "LPT": "LPT",
    "LQTY": "LQTY",
    "LRC": "LRC",
    "LRD": "LRD",
    "LSL": "LSL",
    "LTC": "LTC",
    "LYD": "LYD",
    "MAD": "MAD",
    "MANA": "MANA",
    "MASK": "MASK",
    "MATIC": "MATIC",
    "MCO2": "MCO2",
    "MDL": "MDL",
    "MDT": "MDT",
    "MGA": "MGA",
    "MIR": "MIR",
    "MKD": "MKD",
    "MKR": "MKR",
    "MLN": "MLN",
    "MMK": "MMK",
    "MNT": "MNT",
    "MOP": "MOP",
    "MPL": "MPL",
    "MRO": "MRO",
    "MTL": "MTL",
    "MUR": "MUR",
    "MUSD": "MUSD",
    "MVR": "MVR",
    "MWK": "MWK",
    "MXN": "MXN",
    "MYR": "MYR",
    "MZN": "MZN",
    "NAD": "NAD",
    "NCT": "NCT",
    "NGN": "NGN",
    "NIO": "NIO",
    "NKN": "NKN",
    "NMR": "NMR",
    "NOK": "NOK",
    "NPR": "NPR",
    "NU": "NU",
    "NZD": "NZD",
    "OGN": "OGN",
    "OMG": "OMG",
    "OMR": "OMR",
    "ORN": "ORN",
    "OXT": "OXT",
    "PAB": "PAB",
    "PAX": "PAX",
    "PEN": "PEN",
    "PERP": "PERP",
    "PGK": "PGK",
    "PHP": "PHP",
    "PKR": "PKR",
    "PLA": "PLA",
    "PLN": "PLN",
    "PLU": "PLU",
    "POLS": "POLS",
    "POLY": "POLY",
    "POWR": "POWR",
    "PRO": "PRO",
    "PYG": "PYG",
    "QAR": "QAR",
    "QNT": "QNT",
    "QUICK": "QUICK",
    "RAD": "RAD",
    "RAI": "RAI",
    "RARI": "RARI",
    "RBN": "RBN",
    "REN": "REN",
    "REP": "REP",
    "REPV2": "REPV2",
    "REQ": "REQ",
    "RGT": "RGT",
    "RLC": "RLC",
    "RLY": "RLY",
    "RON": "RON",
    "RSD": "RSD",
    "RUB": "RUB",
    "RWF": "RWF",
    "SAR": "SAR",
    "SBD": "SBD",
    "SCR": "SCR",
    "SEK": "SEK",
    "SGD": "SGD",
    "SHIB": "SHIB",
    "SHP": "SHP",
    "SHPING": "SHPING",
    "SKK": "SKK",
    "SKL": "SKL",
    "SLL": "SLL",
    "SNX": "SNX",
    "SOL": "SOL",
    "SOS": "SOS",
    "SPELL": "SPELL",
    "SRD": "SRD",
    "SSP": "SSP",
    "STD": "STD",
    "STORJ": "STORJ",
    "STX": "STX",
    "SUKU": "SUKU",
    "SUPER": "SUPER",
    "SUSHI": "SUSHI",
    "SVC": "SVC",
    "SZL": "SZL",
    "THB": "THB",
    "TJS": "TJS",
    "TMM": "TMM",
    "TMT": "TMT",
    "TND": "TND",
    "TOP": "TOP",
    "TRAC": "TRAC",
    "TRB": "TRB",
    "TRIBE": "TRIBE",
    "TRU": "TRU",  # codespell:ignore tru
    "TRY": "TRY",
    "TTD": "TTD",
    "TWD": "TWD",
    "TZS": "TZS",
    "UAH": "UAH",
    "UGX": "UGX",
    "UMA": "UMA",
    "UNFI": "UNFI",
    "UNI": "UNI",
    "USD": "USD",
    "USDC": "USDC",
    "USDT": "USDT",
    "UST": "UST",
    "UYU": "UYU",
    "UZS": "UZS",
    "VES": "VES",
    "VGX": "VGX",
    "VND": "VND",
    "VUV": "VUV",
    "WBTC": "WBTC",
    "WCFG": "WCFG",
    "WLUNA": "WLUNA",
    "WST": "WST",
    "XAF": "XAF",
    "XAG": "XAG",
    "XAU": "XAU",
    "XCD": "XCD",
    "XDR": "XDR",
    "XLM": "XLM",
    "XOF": "XOF",
    "XPD": "XPD",
    "XPF": "XPF",
    "XPT": "XPT",
    "XRP": "XRP",
    "XTZ": "XTZ",
    "XYO": "XYO",
    "YER": "YER",
    "YFI": "YFI",
    "YFII": "YFII",
    "ZAR": "ZAR",  # codespell:ignore zar
    "ZEC": "ZEC",
    "ZEN": "ZEN",
    "ZMW": "ZMW",
    "ZRX": "ZRX",
    "ZWL": "ZWL",
}
