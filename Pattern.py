class Boyer_Moore:
    def __init__(self, pat):
        self.pattern = pat
        self.R = 256
        self.right = self.heuristic()

    def heuristic(self):
        m = len(self.pattern)
        right = [-1] * self.R
        for i in range(m):
            right[ord(self.pattern[i])] = i
        return right

    def search(self, string):
        n = len(string)
        m = len(self.pattern)
        position = []
        skip = 0
        while (skip <= n - m):
            j = m - 1
            while j >= 0 and self.pattern[j] == string[skip + j]:  # checking phase
                j -= 1
            if j < 0:  # match case
                position.append(skip)
                # The condition s+m < n is necessary for the case when pattern occurs at the end of text
                skip += (m - self.right[ord(string[skip + m])]
                         if skip + m < n else 1)
            else:
                skip += max(1, j - self.right[ord(string[skip + j])])
        return position


class Rabin_Karp:
    def __init__(self, pat):
        self.M = len(pat)
        self.pattern = pat
        self.R = 256
        self.Q = 397  # prime hash number
        self.RM = 1
        for i in range(1, self.M):
            self.RM = (self.RM * self.R) % self.Q
        self.pathash = self.hashing(self.pattern, self.M)

    def hashing(self, key, m):
        h = 0
        for i in range(m):
            h = (self.R * h + ord(key[i])) % self.Q
        return h

    def search(self, string):
        position = []
        N = len(string)
        txtHash = self.hashing(string, self.M)
        if self.pathash == txtHash:
            position[0]
        for i in range(self.M, N):
            txtHash = (txtHash + self.Q - self.RM * ord(string[i-self.M]) % self.Q) % self.Q
            txtHash = (txtHash*self.R + ord(string[i])) % self.Q

            if self.pathash == txtHash:
                position.append(i - self.M + 1)
        return position
