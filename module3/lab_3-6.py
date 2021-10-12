# create dict called countries with several values (say 5), where keys will be country name and value - domain name, i.e. {Ukraine:UA}
dictCountries = {
    'Ukraine': 'UA',
    'France': 'FR',
    'England': 'EN',
    'Poland': 'PL',
    'Canada': 'CA'
}
# create another dict called capitals, where values of countries will be keys, and values will be the capitals i.e. {'UA': 'Kiev'}
dictCapitals = {
    'UA': 'Kiev',
    'FR': 'Paris',
    'EN': 'London',
    'PL': 'Warsaw',
    'CA': 'Ottawa'
}
# add one more element to each dict above
dictCountries['Germany'] = 'GE'
dictCapitals['GE'] = 'Berlin'
# print sentence "Domain for COUNTRY is DOMAIN." for each record in countries where DOMAIN and COUNTRY have to be replaced with .format()
for key, country in dictCountries.items():
    sentenceFormat = "Domain for {} is {}.".format(key, country)
    print(sentenceFormat)
# print sentence "The capital of COUNTRY is CAPITAL" for each record in capitals where COUNTRY and CAPITAL have to be replaced with .format()
# Merge sentences above together with one cycle
# Add to each value of countries another two domains: COM and GOV, as they can be used too. So value will became a list
# Answer on the questions how embedded data structures works, i.e. list as a value of dictionary.