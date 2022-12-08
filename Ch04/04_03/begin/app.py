import re

five_digit_zip = '98101'
nine_digit_zip = '98101-0003'
phone_number = '234-567-8901'
fiveDigitExpression = r'\d{5}'
print(re.search(fiveDigitExpression, five_digit_zip))
print(re.search(fiveDigitExpression, phone_number))
print(re.search(fiveDigitExpression, nine_digit_zip))
