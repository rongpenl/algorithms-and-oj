# https://blog.csdn.net/yanghua_kobe/article/details/8914970
class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """

    def strStr2(self, source, target):
        # write your code here
        if source == None or target == None:
            return -1
        m, n = len(target), len(source)
        if m > n:
            return -1
        elif m == 0:
            return 0
        elif m == n:
            if source == target:
                return 0
            else:
                return -1
        else:
            BASE = 256
            MOD = 13457
            # http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
            targetHash = 0
            sourceHash = 0
            multiple = 1
            for i in range(m):
                targetHash = (ord(target[i])+targetHash*BASE) % MOD
                sourceHash = (ord(source[i]) + sourceHash*BASE) % MOD
                multiple = multiple if i == 0 else (multiple*BASE) % MOD
            i = 0
            while i + m < n:
                if sourceHash == targetHash and target == source[i:i+m]:
                    return i
                else:
                    sourceHash = (
                        (sourceHash - ord(source[i])*multiple)*BASE + ord(source[i+m])) % MOD
                    i += 1
            return -1
