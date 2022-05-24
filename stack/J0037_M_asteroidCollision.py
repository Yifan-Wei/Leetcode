from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 2 <= asteroids.length <= 104
        # -1000 <= asteroids[i] <= 1000
        # asteroids[i] != 0
        n = len(asteroids)
        index = 0
        while index < n:
            # 碰撞条件
            print(asteroids, index)
            if index>=1 and asteroids[index-1]>0 and asteroids[index]<0:
                left, right = abs(asteroids[index-1]), abs(asteroids[index])
                if left==right:
                    asteroids.pop(index-1)
                    asteroids.pop(index-1)
                    n = len(asteroids)
                    index -= 2
                elif left<right:
                    asteroids.pop(index-1)
                    index -= 2
                    n = len(asteroids)
                else:
                    asteroids.pop(index)
                    index -= 1
                    n = len(asteroids)
            index += 1
        return asteroids

if __name__ == '__main__':
    s = Solution()
    result = s.asteroidCollision([8,-8])
    print(result)
