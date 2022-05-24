class Solution:
    from typing import List
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        res_dict = {}
        for each in strs:
            tmp = list(each)
            tmp.sort()
            key = "".join(tmp)
            if key not in res_dict:
                res_dict[key]=len(res)
                res.append([])
            res[res_dict[key]].append(each)
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.groupAnagrams(["a"])
    print(result)