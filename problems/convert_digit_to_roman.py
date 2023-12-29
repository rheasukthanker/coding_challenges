#User function template for Python 3

class Solution:
    def convertRoman(self, n):
        #Code here
        roman = []
        pw = 1
        while True:
            digit = n%(10)
            if digit!=0:
                roman = roman + [self.get_symbol(digit*(10**(pw-1)))]
                
            else:
                n = n //10
                pw = pw+1
                digit_tens = (n%10)
                if digit_tens == 0:
                    continue
                roman = roman + [self.get_symbol(digit_tens*(10**(pw-1)))]
            n = n//(10)
            pw = pw+1
            if n == 0:
                break
        roman_str = ""
        for s in roman[::-1]:
            roman_str = roman_str + s
        return roman_str
            
        
    def get_symbol(self, digit):
        if digit == 1:
            return "I"
        elif digit == 2:
            return "II"
        elif digit == 3:
            return "III"
        elif digit == 4:
            return "IV"
        elif digit == 5:
            return "V"
        elif digit == 6:
            return "VI"
        elif digit == 7:
            return "VII"
        elif digit == 8:
            return "VIII"
        elif digit == 9:
            return "IX"
        elif digit == 10:
            return "X"
        elif digit  == 20:
            return "XX"
        elif digit  == 30:
            return "XXX"     
        elif digit  == 40:
            return "XL"
        elif digit == 50:
            return "L"
        elif digit == 60:
            return "LX"
        elif digit == 70:
            return "LXX"
        elif digit == 80:
            return "LXXX"
        elif digit == 90:
            return "XC"
        elif digit == 100:
            return "C"
        elif digit == 200:
            return "CC"
        elif digit == 300:
            return "CCC"
        elif digit == 400:
            return "CD"
        elif digit == 500:
            return "D"
        elif digit == 600:
            return "DC"
        elif digit == 700:
            return "DCC"
        elif digit == 800:
            return "DCCC"
        elif digit == 900:
            return "CM"
        elif digit == 1000:
            return "M"
        elif digit == 2000:
            return "MM"
        elif digit == 3000:
            return "MMM"
