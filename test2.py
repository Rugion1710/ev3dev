import pandas as pd

df = pd.read_excel('conversion_table.xlsx')
prefix_length = df['CIDR prefix length'].tolist()
decimal_netmask = df['Dotted Decimal Netmask'].tolist()
conversion_dictionary= dict(zip(decimal_netmask, prefix_length))
