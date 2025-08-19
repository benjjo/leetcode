import re


class Problem_03(object):

    def __init__(self):
        self.temp_str = str()
        self.counter = int()
        self.rolling_counter = int()

    def lengthOfLongestSubstring(self, s):
        """
        type s: str
        :rtype: int
        """
        self.rolling_counter = 0
        self.counter = 0
        self.temp_str = ""

        for n in range(len(s)):
            # print(f'Char is: {s[n]}, range is: {n}, rolling is: {self.rolling_counter}, counter is {self.counter}')
            if s[n] not in self.temp_str:
                self.counter += 1
                self.temp_str += s[n]
                if self.counter > self.rolling_counter:
                    self.rolling_counter = self.counter
            else:
                self.temp_str = str()
                self.counter = 0

        return self.rolling_counter


class Problem_07(object):

    def __init__(self):
        self.temp_str = str()
        self.assignment = str()

    def set_assignment(self, s):
        """
        type s: str
        :rtype: str
        """
        self.assignment = "-" if s[0] == "-" else ""

    def reverse(self, x):
        """
        type x: int
        :rtype: int
        """
        self.set_assignment(str(x))
        self.temp_str = str(x) if str(x)[0] != "-" else str(x)[1:]
        self.temp_str = self.assignment + self.temp_str[::-1]

        return int(self.temp_str)


class Problem_08(object):
    """
    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s
    atoi function).

    The algorithm for myAtoi(string s) is as follows:
    1. Read in and ignore any leading whitespace.

    2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it
    is either. This determines if the final result is negative or positive respectively. Assume the result is positive
    if neither is present.

    3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of
    the string is ignored.

    4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer
    is 0. Change the sign as necessary (from step 2).

    5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 -1], then clamp the integer so that it
    remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than
    2^31 -1 should be clamped to 2^31 -1.
    Return the integer as the final result.
    Note:

    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
    """

    def __init__(self):
        self.MAX_INT32 = pow(2,31) - 1
        self.MIN_INT32 = pow(-2,31)

    def clean(self, s):
        """
        If the first string in the s argument is not all numbers, temp_str defaults to '0'.
        type s: str
        :rtype: str
        """
        s = s.strip()
        # create 'match' for the first string of numbers
        match = re.search(r'\d+', s)
        if not match:
            return 0

        # Create 'preface' for the string leading up to the first string of numbers.
        preface = re.search('[a-zA-Z.+-]+', s)

        # Returns 0 if there are 'a-z', 'A-Z', '.' characters before the number
        if preface and preface.span()[0] < match.span()[0]:
            if preface.span()[1] > 1:
                return 0
            # If the preface span comes before the match, the preface is first.
            output = 0
            if '+' == s[match.span()[0]-1] and preface.span()[1] == 1:
                output = match.group()
            if '-' == s[match.span()[0]-1] and preface.span()[1] == 1:
                output = '-' + str(match.group())
            return int(output)

        if match:
            output = match.group()
            if '-' == s[match.span()[0]-1] and match.span()[0]-1 == 0:
                output = '-' + str(output)
            return int(output)
        return 0

    def enforce_32bit_signed(self, value):
        if value > self.MAX_INT32:
            return self.MAX_INT32
        elif value < self.MIN_INT32:
            return self.MIN_INT32
        return value

    def myAtoi(self, test_string):
        """
        type s: str
        :rtype: int
        """
        output_number = self.clean(test_string)
        output_number = self.enforce_32bit_signed(output_number)
        return output_number


class Problem_29(object):
    """
    29. Divide Two Integers    Medium
    Given two integers dividend and divisor, divide two integers without using multiplication,
    division, and mod operator.

    The integer division should truncate toward zero, which means losing its fractional part.
    For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

    Return the quotient after dividing dividend by divisor.

    Note: Assume we are dealing with an environment that could only store integers within the 32-bit
    signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than
    231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

    Constraints:
    -231 <= dividend, divisor <= 231 - 1
    divisor != 0
    """

    def __init__(self):
        self.MAX_INT32 = pow(2, 31) - 1
        self.MIN_INT32 = pow(-2, 31)

    def enforce_32bit_signed(self, value):
        if value > self.MAX_INT32:
            return self.MAX_INT32
        elif value < self.MIN_INT32:
            return self.MIN_INT32
        return value

    def divide(self, dividend, divisor):
        if divisor == 0:
            raise ZeroDivisionError("division by zero")
        neg = (dividend < 0) ^ (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)
        q = 0
        while a >= b:
            shift = a.bit_length() - b.bit_length()
            cand = b << shift
            if cand > a:
                shift -= 1
                cand = b << shift
            a -= cand
            q += 1 << shift
        return self.enforce_32bit_signed((-q if neg else q))


class Problem_2438(object):
    """
    Given a positive integer n, there exists a 0-indexed array called powers,
    composed of the minimum number of powers of 2 that sum to n.
    The array is sorted in non-decreasing order, and there is only one way to form the array.
    """

    def __init__(self):
        self.powers = list()
        # Constants
        self.BIG_PRIME = pow(10,9) + 7

    def make_powers(self, n):
        powers = list()
        big_bin = 0b100000000000000000000000000000
        while big_bin:
            if big_bin & n:
                powers.append(big_bin)
            big_bin = big_bin >> 1
        powers.sort()
        return powers

    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        self.powers = self.make_powers(n)
        output = list()
        for query in queries:
            start = query[0]
            stop = query[1]
            if stop == start:
                output.append((self.powers[start] % self.BIG_PRIME))
            else:
                rolling = 0
                for i in range(start,stop+1):
                    rolling = rolling * self.powers[i] if rolling else self.powers[i]
                output.append((rolling % self.BIG_PRIME))
        return output

