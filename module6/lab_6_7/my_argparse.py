# Create a module with name my_argparse.py with next code implementation:
#  Check that executable script __name__ variable is equal to “__main__”
#  If yes print next:
#  String 'Parcer initialized!' and variables: lang, keyword and value
#  3 variables are script arguments
#  Set coding of the script as “utf8”
#  Import argparse module
#  Create parser object
#  Add parser argument with key “–l”, string type, “ua” as default value and add any
# help string for key. Store this value into lang variable
#  Add parser argument with key “–c”, string type, “word” as default value and add
# any help string for key. Store this value into keyword variable.
#  Add parser argument with key “–m”, integer type, “0” as default value and add
# any help string for key. Store this value into value variable.

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-1", '--lang', type=str, default='ua',
                    help="Chose language abbreviation! (Ex. 'ua','en')")

parser.add_argument("-c", '--keyword', type=str, default='word',
                    help="Chose word for filter! (Ex. 'hello')")

parser.add_argument("-m", '--value', type=int, default=0,
                    help="Chose number of the best moody for tweets! (Ex. '10', '-12')")

args = parser.parse_args()

lang = args.lang
keyword = args.keyword
value = args.value

if __name__ == '__main__':
    print('Parcer initialized!')
    print(lang, keyword, value)