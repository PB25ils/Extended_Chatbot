import sys
cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    print(sys.stdin.readline().rstrip())

speed, distance = input("Enter: ").split()

if distance - speed <= 1:
    print("SWERVE")  
elif speed*5 - distance > 0:
    print("BRAKE")
else:
    print("SAFE")
