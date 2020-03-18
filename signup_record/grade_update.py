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

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--lastname",
                help="Lastname of the student")
ap.add_argument("-f", "--firstname",
                help="Firstname of the student")
ap.add_argument("-r", "--R#",
                help="R# of the student")
ap.add_argument('-fi', '--filename',
                help='File to be processed')
ap.add_argument('-g', '--grade',
                help='grade to be updated')
ap.add_argument('-c', '--column',
                help='column to add values')
ap.add_argument('-s', '--filesave',
                help='file name to be saved')
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
            student_grade.loc[(cond1) & (cond2), quiz] = int(grade)
        elif R_no:
            R = 'R' + str(R_no)
            cond = student_grade['Student ID'] == R
            print(f'Update the score of student with {R} to gradebook')
            student_grade.loc[cond, quiz] = int(grade)
    except Exception as e:
        print(e)
    return student_grade


def info(file_path: str, R: bool=True) -> str:
    """Print the output data"""
    print('The updated score is ..')
    data = pd.read_excel(file_path)
    if R:
        print(data.dropna(subset=[args['column']]))
        print('the updated score is ..')
        print(data.loc[data['Student ID'] == 'R' + args['R#'], ['First Name', 'Last Name', args['column']]])
    else:
        print(data.dropna(subset=[args['column']]))
        print(update.loc[(cond1) & (cond2), ['Last Name', 'First Name', args['column']]])

if __name__ == "__main__":
    if args['lastname'] and args['firstname']:
        print('last name and first name added')
    elif args['R#']:
        print('R# added')
    else:
        print('nothing added')
    file_path = args['filesave']
    if args['lastname'] and args['firstname']:
        update = update_grades(args['filename'],
                               lastname=args['lastname'],
                               firstname=args['firstname'],
                               quiz=args['column'],
                               grade=args['grade'])
        cond1 = update['Last Name'] == args['lastname']
        cond2 = update['First Name'] == args['firstname']
        update.to_excel(file_path, index=None, header=True)
        info(file_path, R=False)
        print('The updated score is ..')
        # data = pd.read_excel(file_path)
        # print(data.dropna(subset=[args['column']]))
        # print(update.loc[(cond1) & (cond2), ['Last Name', 'First Name', args['column']]])
    elif args['R#']:
        update = update_grades(args['filename'],
                               R_no=args['R#'],
                               quiz=args['column'],
                               grade=args['grade'])
        update.to_excel(file_path, index=None, header=True)
        info(file_path)
        # data = pd.read_excel(file_path)
        # print(data.dropna(subset=[args['column']]))
        # print('the updated score is ..')
        # print(data.loc[data['Student ID'] == 'R' + args['R#'], ['First Name', 'Last Name', args['column']]])
