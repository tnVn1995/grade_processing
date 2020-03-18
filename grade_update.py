"""
Spyder Editor

This is a temporary script file.
"""

"""This program will take R# or First and last name as input to update the
scores of the students"""

import argparse
import time
import sys
import pandas as pd
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--lastname",
                help="Lastname of the student")
ap.add_argument("-f", "--firstname",
                help="Firstname of the student")
ap.add_argument("-r", "--R#",
                help="R# of the student")
ap.add_argument('-fi', '--filename',
                help='file path to be processed')
ap.add_argument('-g', '--grade',
                help='grade to be updated')
ap.add_argument('-c', '--column',
                help='column to add values')
ap.add_argument('-s', '--filesave',
                help='file path to be saved')
args = vars(ap.parse_args())

print(f"Starting to process file {args['filename']} ...")


def update_grades(file_name: str, lastname: str = None, firstname: str = None,
                  R_no: str = None, quiz: str = None, grade: int = None) -> pd.DataFrame:
    """This function takes as input the student's first, last name,
    or their R# and their corresponding grade. The function will update
    the student's grade in the filename
    -----
    Input:
        filename: file to be updated
        lastname: last name of the student
        firstname: first name of the student
        R_no: R number of the student
        quiz: quiz number to be updated
        grade: the student's grade

    Return:
        Update the student's grade in filename
    """
    student_grade = pd.read_excel(file_name)
    if quiz in student_grade.columns:
        pass
    else:
        student_grade[quiz] = None
    try:
        if lastname and firstname:
            cond1 = student_grade['Last Name'] == lastname
            cond2 = student_grade['First Name'] == firstname
            print(f"Update {firstname + lastname}'s score to gradebook...")
            student_grade.loc[(cond1) & (cond2), quiz] = float(grade)
        elif R_no:
            R = 'R' + str(R_no)
            cond = student_grade['Student ID'] == R
            print(f'Update the score of student with {R} to gradebook')
            student_grade.loc[cond, quiz] = float(grade)
    except Exception as e:
        print(e)
    return student_grade


def info(file_path: str, R: bool=True) -> str:
    """[show the grades updated of the student ]
    
    Arguments:
        file_path {str} -- [description]
    
    Keyword Arguments:
        R {bool} -- [if True returned the grades updated for 
        the student with the given R number] (default: {True})
    
    Returns:
        str -- [dataframe of the grades updated for student]
    """"""    """
    print('The updated score is ..')
    data = pd.read_excel(file_path)
    if R:
        print(data.dropna(subset=[args['column']]))
        print('the updated score is ..')
        print(data.loc[data['Student ID'] == 'R' + args['R#'], ['First Name', 'Last Name', args['column']]])
    else:
        print(data.dropna(subset=[args['column']]))
        print(update.loc[(cond1) & (cond2), ['Last Name', 'First Name', args['column']]])
def main():
    if args['lastname'] and args['firstname']:
        print('last name and first name added')
    elif args['R#']:
        print('R# added')
    else:
        print('nothing added')
    file_path = Path(args['filesave'])
    # file_path.mkdir(parents=True, exist_ok=True)
    if args['lastname'] and args['firstname']:
        update = update_grades(args['filename'],
                               lastname=args['lastname'],
                               firstname=args['firstname'],
                               quiz=args['column'],
                               grade=args['grade'])
        cond1 = update['Last Name'] == args['lastname']
        cond2 = update['First Name'] == args['firstname']
        update.to_excel(file_path / args['filename'], index=None, header=True)
        info(file_path / args['filename'], R=False)
        print('The updated score is ..')
    elif args['R#']:
        update = update_grades(args['filename'],
                               R_no=args['R#'],
                               quiz=args['column'],
                               grade=args['grade'])
        update.to_excel(file_path / args['filename'], index=None, header=True)
        info(file_path / args['filename'])
#%% fixing errors
import pandas as pd
import os
file = r'C:\Users\ngu09790\Downloads\Intro to Stat\codes_hist_to_correct.txt'
data = pd.read_csv(file,header=None)
test = []
for idx, val in enumerate(data.values):
    test.append(val)
for val in test:
    val = val[0].strip()
    val = val.split(' ')
    val.pop(0)
    val[3] = './class_roster.xlsx'
    val[5] = './'
    command = ' '.join(val)
    print(command)
if __name__ == "__main__":
        main()



