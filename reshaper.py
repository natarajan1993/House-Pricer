import pandas as pd

df = pd.read_csv('trulia.csv')
# df.drop(df.columns[5:], axis=1, inplace=True)
# df['city'], df['state'] = df['US Metro'].str.split(', ', 1).str
# df.columns = ['quarter', 'us metro', 'starter', 'trade up', 'premium', 'city', 'state']
# df.drop(df.columns[1], axis=1, inplace=True)
df.drop(df.columns[0], axis=1, inplace=True)
# df.replace(to_replace={'state':{
#         'AK': 'Alaska',
#         'AL': 'Alabama',
#         'AR': 'Arkansas',
#         'AZ': 'Arizona',
#         'CA': 'California',
#         'CO': 'Colorado',
#         'CT': 'Connecticut',
#         'DC': 'District of Columbia',
#         'DE': 'Delaware',
#         'FL': 'Florida',
#         'GA': 'Georgia',
#         'GU': 'Guam',
#         'HI': 'Hawaii',
#         'IA': 'Iowa',
#         'ID': 'Idaho',
#         'IL': 'Illinois',
#         'IN': 'Indiana',
#         'KS': 'Kansas',
#         'KY': 'Kentucky',
#         'LA': 'Louisiana',
#         'MA': 'Massachusetts',
#         'MD': 'Maryland',
#         'ME': 'Maine',
#         'MI': 'Michigan',
#         'MN': 'Minnesota',
#         'MO': 'Missouri',
#         'MS': 'Mississippi',
#         'MT': 'Montana',
#         'NC': 'North Carolina',
#         'ND': 'North Dakota',
#         'NE': 'Nebraska',
#         'NH': 'New Hampshire',
#         'NJ': 'New Jersey',
#         'NM': 'New Mexico',
#         'NV': 'Nevada',
#         'NY': 'New York',
#         'OH': 'Ohio',
#         'OK': 'Oklahoma',
#         'OR': 'Oregon',
#         'PA': 'Pennsylvania',
#         'RI': 'Rhode Island',
#         'SC': 'South Carolina',
#         'SD': 'South Dakota',
#         'TN': 'Tennessee',
#         'TX': 'Texas',
#         'UT': 'Utah',
#         'VA': 'Virginia',
#         'VT': 'Vermont',
#         'WA': 'Washington',
#         'WI': 'Wisconsin',
#         'WV': 'West Virginia',
#         'WY': 'Wyoming'
# }},inplace=True)
# df.to_csv('trulia.csv')
print(df.head())