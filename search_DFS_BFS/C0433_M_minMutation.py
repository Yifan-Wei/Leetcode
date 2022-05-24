class Solution:
    """
    start.length == 8
    end.length == 8
    0 <= bank.length <= 10
    bank[i].length == 8
    start、end和bank[i]仅由字符['A', 'C', 'G', 'T']组成
    """
    from typing import List
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        res = 2**31-1
        total = len(bank)
        map = [0] * total

        def is_valid_mutation(s1: str, s2: str) -> bool:
            mutation_num = 0
            for ii in range(len(s1)):
                if s1[ii] != s2[ii]:
                    mutation_num += 1
                if mutation_num > 1:
                    return False
            if mutation_num == 1:
                return True
            return False

        def dfs(try_times, now_str, used_map):
            nonlocal res
            print("NOW STR:", now_str)
            # 如果当前尝试到的字符串是终点, 挑战最低记录
            if now_str == end:
                res = min(res, try_times)
                return
            # 不是终点就找所有可能的下继
            for ii in range(len(used_map)):
                if not used_map[ii] and is_valid_mutation(now_str, bank[ii]):
                    used_map[ii] = 1
                    dfs(try_times + 1, bank[ii], used_map)
                    used_map[ii] = 0
        dfs(0, start, map)
        if res!=2**31-1:
            return res
        else:
            return -1

if __name__ == '__main__':
    s = Solution()
    # start = "AAAAACCC"
    # end = "AACCCCCC"
    # bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
    # start = "AACCGGTT"
    # end = "AAACGGTA"
    # bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    start = "ABAC"
    end = "AAAA"
    bank = ["ACCC", "ACCE", "ACCF", "ACCH", "ACCK"]

    result = s.minMutation(start, end, bank)
    print(result)
