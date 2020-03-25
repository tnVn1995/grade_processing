
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
ap.add_argument('-ex','--extra',
                help='additional version to parse grades in')
ap.add_argument('-cr1', '--credit1',
                help='extra credit to pass in roster1')                
ap.add_argument('-cr2', '--credit2',
                help='extra credit to pass in roster2')                                

args = vars(ap.parse_args())  
directory = 'processed_' + args['save']
try:
    os.mkdir(directory)
except Exception as e:
    print(e)

#%% Test-cell

# args = {'file': 'test1-1.xls', 'extra': 'test1-2.xls', 'roster':'class_roster.xlsx', 'save':'test1'}

# # Save file in csv format
# file = args['save'] + '.csv'

# # Load the grade file in
# form1  = pd.read_excel(args['file'])
# # quiz2 = pd.read_excel('quiz2.xls')
# # quiz1.head()
# if args['extra']:
#     form2 = pd.read_excel(args['extra'])

# #Load the class roster in
# roster = pd.read_excel(args['roster'])
# # roster = pd.read_excel('class_roster.xlsx')
# # roster.head()
#%%
# quiz_core = form1.loc[:,['RNumber', 'RawScore']]
# if args['save'] not in list(roster.columns):
#     roster[args['save']] = None
# for _ , val in enumerate(quiz_core.values):
#     roster.loc[roster['Student ID']==val[0], args['save']] = val[1] + 5
#%%
# if args['extra']:
#     quiz_core = form2.loc[:,['RNumber', 'RawScore']]
#     if args['save'] not in list(roster.columns):
#         roster[args['save']] = None
#     for _ , val in enumerate(quiz_core.values):
#         roster.loc[roster['Student ID']==val[0], args['save']] = val[1] + 5

#%%

def parse_grade(quiz: pd.DataFrame, roster: pd.DataFrame, credit=5) -> pd.DataFrame:
    """Parse grades from quiz to roster"""
    quiz_core = quiz.loc[:,['RNumber', 'RawScore']]
    quiz_core.dropna(inplace=True)
    if args['save'] not in list(roster.columns):
        roster[args['save']] = 0
    for _ , val in enumerate(quiz_core.values):
        roster.loc[roster['Student ID']==val[0], args['save']] = val[1] + credit
    roster[args['save']].where(roster[args['save']] <= 100, 100, inplace=True)
    return roster

def main():
    file = args['save'] + '.csv'

    # Load the grade file in
    form1  = pd.read_excel(args['file'])
    # quiz2 = pd.read_excel('quiz2.xls')
    # quiz1.head()
    if args['extra']:
        form2 = pd.read_excel(args['extra'])
        if args['credit1']:
            credit1 = int(args['credit1'])
            roster = pd.read_excel(args['roster'])
            roster = parse_grade(quiz = form1, roster = roster, credit=credit1)
            # Move files
            roster.to_csv(os.path.join(directory,file), index=False, header=True)
            shutil.copy(args['file'], os.path.join(directory, args['file']))
            shutil.copy(args['roster'], os.path.join(directory, args['roster']))
            
        if args['credit1'] and args['credit2']:
            credit1 = int(args['credit1'])
            credit2 = int(args['credit2'])
            roster = pd.read_excel(args['roster'])
            roster = parse_grade(quiz = form1, roster = roster, credit=credit1)
            roster = parse_grade(quiz = form2, roster = roster, credit=credit2)
            # Move files
            roster.to_csv(os.path.join(directory,file), index=False, header=True)
            shutil.copy(args['file'], os.path.join(directory, args['file']))
            shutil.copy(args['roster'], os.path.join(directory, args['roster']))
            shutil.copy(args['extra'], os.path.join(directory, args['extra']))
        else:
            roster = pd.read_excel(args['roster'])
            roster = parse_grade(quiz = form1, roster = roster)
            roster = parse_grade(quiz = form2, roster = roster)
            # Move files
            roster.to_csv(os.path.join(directory,file), index=False, header=True)
            shutil.copy(args['file'], os.path.join(directory, args['file']))
            shutil.copy(args['roster'], os.path.join(directory, args['roster']))
            shutil.copy(args['extra'], os.path.join(directory, args['extra']))            
    elif args['credit1']:
        if args['credit1']:
            credit1 = int(args['credit1'])
            roster = pd.read_excel(args['roster'])
            roster = parse_grade(quiz = form1, roster = roster, credit=credit1)
            # Move files
            roster.to_csv(os.path.join(directory,file), index=False, header=True)
            shutil.copy(args['file'], os.path.join(directory, args['file']))
            shutil.copy(args['roster'], os.path.join(directory, args['roster']))    
    #Load the class roster in
    else:
        roster = pd.read_excel(args['roster'])
        roster = parse_grade(quiz = form1, roster = roster)
        roster.to_csv(os.path.join(directory,file), index=False, header=True)
        shutil.copy(args['file'], os.path.join(directory, args['file']))
        shutil.copy(args['roster'], os.path.join(directory, args['roster']))

#%%
if __name__ == '__main__':
    main()
