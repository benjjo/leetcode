import unittest
from main import *


class TestClass(unittest.TestCase):

    def test_lengthOfLongestSubstring(self):
        """
        Longest Substring Without Repeating Characters

        Given a string s, find the length of the longest
        substring without repeating characters.

        Example 1:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

        Example 2:
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Example 3:
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

        Constraints:
        0 <= s.length <= 5 * 104
        s consists of English letters, digits, symbols and spaces.
        """
        self.test_class = Problem_03()
        self.assertIs(3, self.test_class.lengthOfLongestSubstring("abcabcbb"))
        self.assertIs(1, self.test_class.lengthOfLongestSubstring("bbbbb"))
        self.assertIs(3, self.test_class.lengthOfLongestSubstring("pwwkew"))

    def test_reverse(self):
        """
        Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
        the signed 32-bit integer range [-231, 231 - 1], then return 0.
        Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

        Example 1:
        Input: x = 123
        Output: 321

        Example 2:
        Input: x = -123
        Output: -321

        Example 3:
        Input: x = 120
        Output: 21

        Constraints:
        -231 <= x <= 231 - 1
        """
        self.test_class = Problem_07()
        self.assertEqual(321, self.test_class.reverse(123))
        self.assertEqual(-321, self.test_class.reverse(-123))
        self.assertEqual(21, self.test_class.reverse(120))

    def test_myAtoi(self):
        """
        Example 1:
        Input: s = "42"
        Output: 42
        Explanation: The underlined characters are what is read in, the caret is the current reader position.
        Step 1: "42" (no characters read because there is no leading whitespace)
        Step 2: "42" (no characters read because there is neither a '-' nor '+')
        Step 3: "42" ("42" is read in)
        The parsed integer is 42.
        Since 42 is in the range [-2^31, 2^31 -1], the final result is 42.

        Example 2:
        Input: s = "   -42"
        Output: -42
        Explanation:
        Step 1: "   -42" (leading whitespace is read and ignored)
        Step 2: "   -42" ('-' is read, so the result should be negative)
        Step 3: "   -42" ("42" is read in)
        The parsed integer is -42.
        Since -42 is in the range [-2^31, 2^31 -1], the final result is -42.

        Example 3:
        Input: s = "4193 with words"
        Output: 4193
        Explanation:
        Step 1: "4193 with words" (no characters read because there is no leading whitespace)
        Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
        Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
        The parsed integer is 4193.
        Since 4193 is in the range [-2^31, 2^31 -1], the final result is 4193.

        Constraints:
        0 <= s.length <= 200
        s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
        """
        self.test_class = Problem_08()
        self.assertEqual(42, self.test_class.myAtoi("42"))
        self.assertEqual(-42, self.test_class.myAtoi("   -42"))
        self.assertEqual(4193, self.test_class.myAtoi("4193 with words"))
        self.assertEqual(2147483647, self.test_class.myAtoi("2147483648"))
        self.assertEqual(-2147483648, self.test_class.myAtoi("-2147483649"))
        self.assertEqual(0, self.test_class.myAtoi("words and 987"))
        self.assertEqual(0, self.test_class.myAtoi(".1"))
        self.assertEqual(0, self.test_class.myAtoi("+-12"))
        self.assertEqual(0, self.test_class.myAtoi("+"))
        self.assertEqual(1, self.test_class.myAtoi("+1"))
        self.assertEqual(0, self.test_class.myAtoi("-+12"))
        self.assertEqual(123, self.test_class.myAtoi("123-"))
        self.assertEqual(0, self.test_class.myAtoi("--2"))

    def test_29(self):
        """
        Example 1:
        Input: dividend = 10, divisor = 3
        Output: 3
        Explanation: 10/3 = 3.33333.. which is truncated to 3.

        Example 2:
        Input: dividend = 7, divisor = -3
        Output: -2
        Explanation: 7/-3 = -2.33333.. which is truncated to -2.
        """
        self.test_class = Problem_29()
        self.assertEqual(3, self.test_class.divide(10, 3))
        self.assertEqual(-2, self.test_class.divide(7, -3))

    def test_2438(self):
        """
        Given a positive integer n, there exists a 0-indexed array called powers,
        composed of the minimum number of powers of 2 that sum to n.
        The array is sorted in non-decreasing order,
        and there is only one way to form the array.

        You are also given a 0-indexed 2D integer array queries,
        where queries[i] = [lefti, righti]. Each queries[i] represents a
        query where you have to find the product of all powers[j] with lefti <= j <= righti.

        Return an array answers, equal in length to queries, where answers[i]
        is the answer to the ith query. Since the answer to the ith query may be too large,
        each answers[i] should be returned modulo 10^9 + 7 (the largest prime to fit inside a
        32-bit signed integer without causing overflow).

        Example 1:

        Input: n = 15, queries = [[0,1],[2,2],[0,3]]
        Output: [2,4,64]
        Explanation:
        For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
        Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
        Answer to 2nd query: powers[2] = 4.
        Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
        Each answer modulo 10^9 + 7 yields the same answer, so [2,4,64] is returned.

        Example 2:

        Input: n = 2, queries = [[0,0]]
        Output: [2]
        Explanation:
        For n = 2, powers = [2].
        The answer to the only query is powers[0] = 2. The answer modulo 10^9 + 7 is the same,
        so [2] is returned.


        Constraints:

        1 <= n <= 10^9
        1 <= queries.length <= 10^5
        0 <= starti <= endi < powers.length
        """
        self.test_class = Problem_2438()
        self.assertListEqual([1, 2, 4, 8], self.test_class.make_powers(15))
        self.assertListEqual([2], self.test_class.make_powers(2))
        self.assertListEqual([4], self.test_class.make_powers(4))
        self.assertListEqual([8], self.test_class.make_powers(8))
        self.assertListEqual([16], self.test_class.make_powers(16))
        self.assertListEqual([32], self.test_class.make_powers(32))
        self.assertListEqual([1024], self.test_class.make_powers(1024))
        self.assertListEqual([0b10], self.test_class.make_powers(2))
        self.assertListEqual([0b100000000000000000000000000000],
                             self.test_class.make_powers(536870912))
        # Input:
        n = 15
        queries = [[0,1],[2,2],[0,3]]
        self.assertEqual([2,4,64], self.test_class.productQueries(n, queries))
        n = 2
        queries = [[0, 0]]
        self.assertEqual([2], self.test_class.productQueries(n, queries))
