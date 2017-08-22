from dicBMI import team

def writeBMI(team):
    w = open("BMI_TEAM.txt", 'w')
    for i in team:
        w.write(str(i) + '\n')
    w.close()


writeBMI (team)
