class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        IntList = [1000, 100, 10, 1]
        IntRecordDict = {
            1000: 0,
            100: 0,
            10: 0,
            1: 0,
        }
        IntRomanDict = {
            1: ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            10: ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            100: ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            1000: ["M", "MM", "MMM"]
        }

        for each in IntList:
            if num >= each:
                IntRecordDict[each] = num // each
                num = num % each
        for key, value in IntRecordDict.items():
            if value > 0:
                ans += "{0}".format(IntRomanDict[key][value - 1])
        return ans