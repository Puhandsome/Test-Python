a = int(input())
b = int(input())
m = int(input())
answer_found = False

for x in range(m // a, -1, -1):
    if (m - a*x) % b == 0:  # compute y only if it will result in an integer
        answer_found = True
        y = (m - a*x) // b
        print("Teddy bear:", x, "Kitty doll:", y)

if not answer_found:
    print("Not possible")