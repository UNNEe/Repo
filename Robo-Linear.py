i_list = list(input("F: forward;T: backwards \n"))
hold = 0
for i in (i_list):
    if i == "F":
        hold += 1
answer = hold + (hold-len(i_list))
print("The robot walked %d meters from its starting position"%answer)