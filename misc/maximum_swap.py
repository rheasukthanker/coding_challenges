'''You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.'''
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        max_right_index = [0] * n

        max_right_index[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            max_right_index[i] = (
                i
                if num_str[i] > num_str[max_right_index[i + 1]]
                else max_right_index[i + 1]
            )

        for i in range(n):
            if num_str[i] < num_str[max_right_index[i]]:
                num_str[i], num_str[max_right_index[i]] = (
                    num_str[max_right_index[i]],
                    num_str[i],
                )
                return int("".join(num_str))

        return num

class Solution:
    def maximumSwap(self, num: int) -> int:
        new_num = ''
        digits = [int(n) for n in list(str(num))]
        if len(digits) == 1:
            return num
        if len(digits) == 2:
            s = ''
            for d in sorted(digits,reverse=True):
                s = s+str(d)
            return int(s)
        swap_count = 1
        i = 0
        end_id = len(digits)
        while swap_count >0 and i<len(digits):
            max_num = -1
            max_id = -1
            min_id = i
            counter = i
            if max(digits[i:]) == digits[i]:
                i = i+1
                continue
            for d in digits[i:end_id]:
                if d>=max_num:
                    max_num = d
                    max_id = counter
                counter = counter+1
            temp = digits[max_id]
            digits[max_id] = digits[min_id]
            digits[min_id] = temp
            if max_id != min_id:
                swap_count = swap_count - 1
            i = i+1
        digit_str = ''
        for d in digits:
            digit_str +=str(d)
        return int(digit_str)
