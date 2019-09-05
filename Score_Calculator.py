from ScoreCalculator import ScoreCalculator
import time

print("="*26)
print("Gymnast Score Calculator")
print("="*26)

name = input("Enter the Gymnast's name: ")
scores = input("Enter the scores: ")

fir, sec, thi, fort, fif, six, sev = scores.split(" ")

# 클래스 생성
Gymnast_cal = ScoreCalculator(int(fir), int(sec), int(thi), int(fort), int(fif), int(six), int(sev))

delMax_list = Gymnast_cal.del_max() #최대값 삭제
delMin_list = Gymnast_cal.del_min() #최소값 삭제

avg_score = Gymnast_cal.avg_score() #평균 구하기

print("Calculator processing", end = "")

#time.sleep 함수를 사용하여 마치 컴퓨터가 계산한 것 처럼 보여준다.
#time.sleep()에서 괄호 안에 초를 넣어준다.

for i in range(9):
    time.sleep(1)
    print(".", end = "")

print()

print(name+"'s final score is: %0.2f" %avg_score)