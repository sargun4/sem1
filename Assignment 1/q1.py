def converttowords(n):
    single_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    two_digits = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen","sixteen", "seventeen", "eighteen",
                  "nineteen"]
                  
    tens_multiple = ["","","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty","ninety"]
    n=str(int(n))
    out_str=0
    if int(n)<10:
        out_str=single_digits[int(n)]
        print(out_str)
    elif int(n)<20:
        out_str=two_digits[int(n)-10]
        print(out_str)
    elif int(n)<99:
        if n[1]=='0':
            out_str=tens_multiple[int(n[0])]
        else:
            out_str=tens_multiple[int(n[0])]+' '+single_digits[int(n[1])]
        print(out_str)
converttowords(int(input()))
