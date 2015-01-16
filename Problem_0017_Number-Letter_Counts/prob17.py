dic = {
	"1": "one",
	"2": "two",
	"3": "three",
	"4": "four",
	"5": "five",
	"6": "six",
	"7": "seven",
	"8": "eight",
	"9": "nine",
	"10": "ten",
	"11": "eleven",
	"12": "twelve",
	"13": "thirteen",
	"14": "fourteen",
	"15": "fifteen",
	"16": "sixteen",
	"17": "seventeen",
	"18": "eighteen",
	"19": "nineteen",
	"20": "twenty",
	"30": "thirty",
	"40": "forty",
	"50": "fifty",
	"60": "sixty",
	"70": "seventy",
	"80": "eighty",
	"90": "ninety",
}

def getStr(number):
	if number > 0 and number <= 20:
		return dic[str(number)]
	elif number < 100:
		if number % 10 == 0:
			return dic[str(number)]
		else:
			return dic[str(number-number%10)]+"-"+dic[str(number%10)]
	elif number < 1000:
		if number % 100 == 0:
			return dic[str(number/100)]+" hundred"
		else:
			return dic[str(number/100)]+" hundred and "+getStr(number%100)
	elif number == 1000:
		return "one thousand"
	else:
		return ""

def getLen(str):
	cnt = 0
	for i in range(len(str)):
		if str[i] != ' ' and str[i] != '-':
			cnt += 1
	return cnt

sum = 0
for i in range(1,1001):
	sum += getLen(getStr(i))
print sum