ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
tens = {10: 'ten', 11: 'eleven', 12:  'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
        20:  'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seven', 80: 'eighty', 90: 'ninety'}

number = int(input())

if number <= 9:
    print(ones[number])
elif 10 <= number <= 20:
    print(tens[number])
elif 21 <= number <= 99:
    a = number // 10 * 10
    b = number % 10
    out = tens[a]
    if b > 0:
        out += " " + ones[b]
    print(out)
else:
    a = number // 100 * 100
    b = (number % 100) // 10 * 10
    c = number % 10
    out = ones[a // 100] + " hundred"
    if b > 0 and c > 0:
        if b == 10:
            out += " and " + tens[b + c]
        else:
            out += " and " + tens[b] + " " + ones[c]
    elif b > 0:
        out += " and " + tens[b]
    elif c > 0:
        out += " and " + ones[c]
    print(out)