def investment_years(amt, goal):
    intr = amt
    time = 0
    while intr < goal * amt:
        intr = intr * 1.05
        time += 1
    message = ('The investment of ${:>3,} will be {} times larger in {} years.'.format(amt, goal, time ) )
    return message 




