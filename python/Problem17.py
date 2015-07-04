def number_to_words(number):
    ones_place = ["zero",
                  "one",
                  "two",
                  "three",
                  "four",
                  "five",
                  "six",
                  "seven",
                  "eight",
                  "nine"]

    teens = ["ten",
             "eleven",
             "twelve",
             "thirteen",
             "fourteen",
             "fifteen",
             "sixteen",
             "seventeen",
             "eighteen",
             "nineteen",]

    twenty_to_one_hundred = [
                             "twenty",
                             "thirty",
                             "forty",
                             "fifty",
                             "sixty",
                             "seventy",
                             "eighty",
                             "ninety"]
    if number > 0 and number < 10:
        return ones_place[number]

    if number >= 10 and number < 20:
        return teens[number%10]

    if number >= 20 and number < 100:
        val = twenty_to_one_hundred[(number//10)-2]
        if number % 10 != 0:
            val = val + "-" + ones_place[number%10]
        return val

    if number >= 100 and number < 1000:
        val = ones_place[((number//100) % 10)]
        val += " "
        val += "hundred"

        if number%100 != 0:
            v = number%100
            val += " and "
            val += number_to_words(v)
        return val

    if number >= 1000:
        val = ones_place[number//1000]
        val += " "
        val += "thousand"

        if number % 1000 < 100 and number % 1000 != 0:
            val += " and "

        if number%1000 != 0:
            v = number % 1000
            val += number_to_words(v)
        return val

total = 0
for i in range(1, 1001):
    total += len(number_to_words(i).replace(' ', '').replace('-', ''))
print(total)

