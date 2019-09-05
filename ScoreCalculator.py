class ScoreCalculator:
    score_list = []
    def __init__(self, fir, sec, thi, fort, fif, six, sev):
        self.score_list = [fir, sec, thi, fort, fif, six, sev]
    def del_max(self):
        maxS = max(self.score_list)  #int 값으로 max값 나옴.
        i = self.score_list.index(maxS)
        del self.score_list[i]
        return self.score_list
    def del_min(self):
        minS = min(self.score_list)
        i = self.score_list.index(minS)
        del self.score_list[i]
        return self.score_list
    def avg_score(self):
        sum = 0
        num = len(self.score_list)
        for i in range(num):
            sum += self.score_list[i]
        return sum/num

