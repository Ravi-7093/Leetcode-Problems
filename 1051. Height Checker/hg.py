a = heights.copy()
        a.sort()
        res = 0
        wrd=zip(a,heights)
        print(tuple(wrd))
        for i, j in zip(a, heights):
            if j != i:
                res += 1
        return res
