#%%
import pandas as pd
import numpy as np
import argparse
import re
from pathlib import Path
#%%
ap = argparse.ArgumentParser(description='''Calculate Class GPA''')

ap.add_argument('-f', '--file', required=True,
                help='Class Grade file')
ap.add_argument('-s', '--save',
                help='File path to save')
args=vars(ap.parse_args())               

def remove_worst(x: np.array) -> pd.Series:
    x = sorted(x)
    x = x[2:]
    return x

def mean(x: np.array) -> pd.Series:
    return round(np.array(x).mean(),3)
# data_path = r'C:\Users\ngu09790\Downloads\Intro to Stat\processed_test2\test2.csv'
def main():
    root = Path(args['file']).parent
    data_path = args['file']
    grades = pd.read_csv(data_path)

    columns = list(grades.columns)

    grades.columns = [x.split(' ')[0] for x in columns]

    tests = [x for x in grades.columns if re.match(r'^[Tt]est\d$(?<![aA-Zz])', x)]
    quizzes = [x for x in grades.columns if re.match(r'^[qQ]uiz.*',x)]

    test_grades = grades[tests]
    quiz_grades = grades[quizzes]

    quiz_grades.fillna(0, inplace=True)
    test_grades.fillna(0, inplace=True)

    quiz_grades.where(quiz_grades <= 100, 100, inplace=True)
    test_grades.where(test_grades <= 100, 100, inplace=True)

    grades[quizzes] = quiz_grades
    grades[tests] = test_grades

    avg_quiz = quiz_grades.apply(remove_worst, axis=1)
    avg_quiz = avg_quiz.apply(mean)

    avg_test = test_grades.mean(axis=1)


    current_gpa = (avg_test*0.3 + avg_quiz*0.15) / 0.45
    grades['current_gpa'] = current_gpa
    grades.to_csv(str(root / args['save']), index=None, header=True)

if __name__ == '__main__':
    main()

#%%
# current_rost = pd.read_excel('current_roster.xlsx')
# old_rost = pd.read_excel('class_roster.xlsx')

# # %%
# for x in old_rost['Student ID'].values:
#     if x not in current_rost['Student ID'].values:
#         print(x)

# %%
