s = """Command the robot with:
L - turn left
R - turn right
M - move forward
? - print this message
Q - quit
"""
direction = {'M': 'North', 'L': 'West', 'R': 'East'}

print("Hello! Robot coming online.")
print(s)

x = y = 0


while True:
    inp = input()

    if inp.upper() == 'Q':
        print("Robot shutting down.")
        break
    elif inp == '?':
        print(s)
        continue

    if inp.upper() == 'M':
        y += 1
    elif inp.upper() == 'L':
        x -= 1
    elif inp.upper() == 'R':
        x += 1

    if inp.upper() in direction:
        print("Robot at (" + str(x) + ", " + str(y) + ") facing " + direction[inp.upper()])