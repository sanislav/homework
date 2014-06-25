'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
letters. The use of "and" when writing out numbers is in compliance with 
British usage.
'''

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten_ninteen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds = [digit+' hundred' for digit in digits]
thousands = [digit+' thousand' for digit in digits]

def get_number_word(num):
    # below 100
    if num < 10:
        number = digits[num]
    if num >= 10 and num < 20:
        number = ten_ninteen[num-10]
    if num >= 20 and num < 100:
        if num%10 == 0:
            number = tens[num/10 - 1]
        else:
            number = tens[num/10 - 1] + digits[num%10]
    # hundreds
    if num >= 100 and num < 1000:
        if num%100 == 0:
            number = hundreds[num/100]
        else:
            number = hundreds[num/100] + ' and ' + get_number_word(num - num/100 * 100)
    # thousands
    if num >= 1000 and num < 10000:
        if num%1000 == 0:
            number = thousands[num/1000]
        else:
            # todo: do not use and if followed by humdreds
            number = thousands[num/1000] + ' and ' + get_number_word(num - num/100 * 100)

    return number

def count_letters(max):
    num_letters = 0
    for num in xrange(1,max+1):
        num_letters += len(get_number_word(num))

    return num_letters

num_letters = count_letters(1000)
print num_letters