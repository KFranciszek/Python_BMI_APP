import dicBMI
import scoreBMI
# from dicBMI  import BMI_data
from dicBMI  import team
# from dicBMI  import bmiDic
# from scoreBMI  import scoreBMI_data
# from scoreBMI  import score2
# from scoreBMI  import score

def BMI_print ():
    for dict in team:
     print(dict['name'],  " twoje BMI wynosi: ", dict['bmi'])


BMI_print()
