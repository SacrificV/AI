class SuffixAutomaton:
    def __init__(self):
        self.next = [{}]
        self.link = [-1]
        self.length = [0]
        self.last = 0

    def extend(self, c):
        cur = len(self.next)
        self.next.append({})
        self.length.append(self.length[self.last] + 1)
        self.link.append(0)

        p = self.last
        while p != -1 and c not in self.next[p]:
            self.next[p][c] = cur
            p = self.link[p]

        if p == -1:
            self.link[cur] = 0
        else:
            q = self.next[p][c]
            if self.length[p] + 1 == self.length[q]:
                self.link[cur] = q
            else:
                clone = len(self.next)
                self.next.append(self.next[q].copy())
                self.length.append(self.length[p] + 1)
                self.link.append(self.link[q])

                while p != -1 and self.next[p].get(c) == q:
                    self.next[p][c] = clone
                    p = self.link[p]

                self.link[q] = self.link[cur] = clone

        self.last = cur

    def count_substrings(self):
        res = 0
        for i in range(1, len(self.length)):
            res += self.length[i] - self.length[self.link[i]]
        return res


s = input().strip()

sam = SuffixAutomaton()
for c in s:
    sam.extend(c)

print(sam.count_substrings())

#example input
#la bobo
#Output:
#25