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
print('-----------------Countries----------------------')
for country, key in dictCountries.items():
    sentenceFormat = "Domain for {} is {}.".format(country, key)
    print(sentenceFormat)

# print sentence "The capital of COUNTRY is CAPITAL" for each record in capitals where COUNTRY and CAPITAL have to be replaced with .format()
print('\n-----------------Capitals ----------------------')
for key, capital in dictCapitals.items():
    sentenceFormat = "The capital of {} is {}.".format(key, capital)
    print(sentenceFormat)

# Merge sentences above together with one cycle
print('\n----------------- Merge sentences above together with one cycle ----------------------')
for countries, value in dictCountries.items():
    togetherCycle = "Domain for {} is {}. The capital is {}".format(countries, value, dictCapitals[value])
    print(togetherCycle)

# Add to each value of countries another two domains: COM and GOV, as they can be used too. So value will became a list
print('Add to each value of countries another two domains: COM and GOV')
for key, value in dictCountries.items():
    newTwoDomains = dictCountries[key] = [value, 'COM', 'GOV']
    print(newTwoDomains)

# Answer on the questions how embedded data structures works, i.e. list as a value of dictionary.