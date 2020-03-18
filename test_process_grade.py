
#%%
import pandas as pd
import argparse
import os
import shutil

#%%
ap = argparse.ArgumentParser(description='''Parse Grades of students from file
to roster based on R number''')

ap.add_argument('-s', '--save', required=True,
                help='name of the file to be saved')
ap.add_argument('-f', '--file', required=True,
                help='the grade file')
ap.add_argument('-r','--roster', required=True,
                help='the current roster of the class file')
ap.add_argument('-ex','--extra', required=True,
                help='additional version to parse grades in')

args = vars(ap.parse_args())  
directory = 'processed_' + args['save']
try:
    os.mkdir(directory)
except Exception as e:
    print(e)

#%% Test-cell

args = {'file': 'test1-1.xls', 'extra': 'test1-2.xls', 'roster':'class_roster.xlsx', 'save':'test1'}

# Save file in csv format
file = args['save'] + '.csv'

# Load the grade file in
form1  = pd.read_excel(args['file'])
# quiz2 = pd.read_excel('quiz2.xls')
# quiz1.head()
form2 = pd.read_excel(args['extra'])

#Load the class roster in
roster = pd.read_excel(args['roster'])
# roster = pd.read_excel('class_roster.xlsx')
# roster.head()
#%%
quiz_core = form1.loc[:,['RNumber', 'RawScore']]
if args['save'] not in list(roster.columns):
    roster[args['save']] = None
for _ , val in enumerate(quiz_core.values):
    roster.loc[roster['Student ID']==val[0], args['save']] = val[1] + 5
#%%
quiz_core = form2.loc[:,['RNumber', 'RawScore']]
if args['save'] not in list(roster.columns):
    roster[args['save']] = None
for _ , val in enumerate(quiz_core.values):
    roster.loc[roster['Student ID']==val[0], args['save']] = val[1] + 5

#%%

def parse_grade(quiz: pd.DataFrame, roster: pd.DataFrame) -> pd.DataFrame:
    """Parse grades from quiz to roster"""
    quiz_core = quiz.loc[:,['RNumber', 'RawScore']]
    quiz_core.dropna(inplace=True)
    if args['save'] not in list(roster.columns):
        roster[args['save']] = None
    for _ , val in enumerate(quiz_core.values):
        roster.loc[roster['Student ID']==val[0], args['save']] = val[1] + 5
    return roster


#%%
if __name__ == '__main__':
    roster1 = parse_grade(quiz = form1, roster = roster)
    roster2 = parse_grade(quiz = form2, roster = roster1)
    roster.to_csv(os.path.join(directory,file), index=False, header=True)
    shutil.copy(args['file'], os.path.join(directory, args['file']))
    shutil.copy(args['roster'], os.path.join(directory, args['roster']))

#%%
