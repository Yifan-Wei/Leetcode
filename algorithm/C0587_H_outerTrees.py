class Solution:
    from typing import List

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        """
        :param trees:
        :return:
        在一个二维的花园中，有一些用 (x, y) 坐标表示的树。
        由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。
        只有当所有的树都被绳子包围时，花园才能围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。
        # 共线凸包问题
        1、按极角坐标序排
            缺点：需要将最后一条边上的点逆序排，才能够将最后一边共线点加入凸包。
        2、按水平序排。
            缺点：若所有点在一条直线上，会产生将所有点入凸包1~n~2的情况，需要特判，当然本题只是用到这些点，无需判断是否重复出现。
        """
        # 特殊情况处理, 如果输入值小于2个, 直接原地输出
        if len(trees)<=2: return trees

        from functools import cmp_to_key  # 用于自定义比较函数
        def dis(p1,p2):
            """计算距离"""
            return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

        def cross(p0, p1, p2):
            """向量叉乘"""
            return (p1[0]-p0[0]) * (p2[1]-p0[1]) - (p2[0]-p0[0]) * (p1[1]-p0[1])

        def dot(p0, p1, p2):
            """向量点乘"""
            return (p1[0]-p0[0])*(p2[0]-p0[0]) + (p1[1]-p0[1])*(p2[1]-p0[1])

        def horizon_sort(p1,p2):
            """水平排序"""
            if p1[0]==p2[0]:
                if p1[1]<p2[1]:
                    return 1
                else:
                    return -1
            else:
                if p1[0]<p2[0]:
                    return 1
                else:
                    return -1

        def polar_sort(p1, p2):
            """极坐标排序"""
            # 弊端在于凸包寻找的过程中会舍掉共线的点, 因为排序始终是以起始点进行的
            # 比如(0,0),(1,1),(2,2),(-2,2),(-1,1)这样的三角形, 无论从近到远还是从远到近都会舍弃掉共线点
            nonlocal trees
            p0 = trees[0]
            cross_res = cross(p0, p1, p2)
            # print(p1, p2, cross_res)
            if cross_res > 0:
                return -1
            elif cross_res == 0 and dis(p0,p1) < dis(p0,p2):
                return -1  # 需要return 1和-1而不是True和False
            else:
                return 1

        # START
        # 输入数组极坐标排序(共线的时候存在问题)
        min_x = 2**31-1
        min_y = 2**31-1
        p0_index = 0
        for ii in range(len(trees)):
            each = trees[ii]
            # 找最下(多个则左下)的作为center点
            if each[1] < min_y or (each[1] == min_y and each[0] <= min_x):
                min_x = each[0]
                min_y = each[1]
                p0_index = ii
        # print("[{0},{1}],index={2}".format(min_x, min_y, p0_index))
        # swap
        tmp = trees[p0_index]
        trees[p0_index] = trees[0]
        trees[0] = tmp
        # sorted是高阶函数, python3不再支持传入比较方法, 但可以使用cmp_to_key包装自定义比较方法(polar_sort)
        trees[1:] = sorted(trees[1:], key=cmp_to_key(polar_sort))
        print(trees)
        # 最后一条边倒序: 这是因为是极坐标排序, 只有最后一条边存在远近距离的区别.
        break_flag = False  # 防止全部都共线, 那样就无需逆转了
        for ii in range(len(trees)-1, 0, -1):
            if cross(trees[0], trees[ii], trees[ii-1]) != 0:
                break_flag = True
                break
        if break_flag:
            trees[ii:len(trees)] = sorted(trees[ii:len(trees)], key=cmp_to_key(polar_sort), reverse=True)
        # 排序完成
        # print(trees)
        # trees[1:] = algorithm_sort(trees[1:],key=cmp_to_key(horizon_sort))

        def Graham(trees):
            """ 这种方案无法解决共线问题"""
            # 要求极坐标排序+最后一条边翻转
            # --------------------------------------------------
            # 已处理栈(存储下标)
            stack = [-1]*(len(trees))
            for ii in range(2):
                stack[ii] = ii
            top = 1 # 栈顶位置
            for ii in range(2, len(trees)):
                if trees[ii] == [2,6]:
                    print("here")
                # 只有满足在逆时针方向才满足凸包性质, 否则退出上一个进入的点, 直到能够满足凸包
                while top>0 and cross(trees[stack[top-1]], trees[stack[top]], trees[ii]) < 0:
                    top -= 1
                top += 1
                stack[top] = ii
            res = []
            # print(stack)
            for ii in range(0, top+1):
                if stack[ii]>=0:
                    res.append(trees[stack[ii]])
            return res

        return Graham(trees)

if __name__ == "__main__":
    s = Solution()
    result = s.outerTrees(trees=[[0,0],[1,0],[1,3],[1,8],[1,9],[2,0],[2,6],[3,0],[3,1],[3,4],[3,6],[4,2],[4,6],[5,7],[5,8],[6,2],[6,4],[7,7],[7,9],[8,0],[8,1],[8,3],[8,5],[9,6]])
    # result = s.outerTrees(trees=[[1,2],[2,2],[4,2],[6,2]])
    print(result)