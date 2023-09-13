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
