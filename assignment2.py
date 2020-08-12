class Finder:
    def __init__(self, arr):
        self.list = arr

    def find(self, s):
        return list(filter(lambda x: self.compare_str(x, s), self.list))

    def compare_str(self, s1, s2):
        if len(s1) != len(s2):
            return False
        else:
            dic = {}
            ret = True

            for i in range(0, len(s1)):
                if s1[i] in dic:
                    continue
                else:
                    dic[s1[i]] = s1.count(s1[i])

                if dic[s1[i]] != s2.count(s1[i]):
                    ret = False
                    break

            return ret


finder = Finder(['asd', 'asdd', 'fre'])

print(finder.find('sad'))

