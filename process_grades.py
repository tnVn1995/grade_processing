
#%%
import pandas as pd
import argparse
import os
import shutil


ap = argparse.ArgumentParser()

ap.add_argument('-s', '--save', required=True,
                help='name of the file to be saved')
ap.add_argument('-f', '--file', required=True,
                help='the grade file')
ap.add_argument('-r','--roster', required=True,
                help='the current roster of the class file')

args = vars(ap.parse_args())  
directory = 'processed' + args['save']
try:
    os.mkdir(directory)
except Exception as e:
    print(e)

# Save file in csv format
file = args['save'] + '.csv'

# Load the grade file in
quiz1 = pd.read_excel(args['file'])

# quiz1.head()


#%%

#Load the class roster in
roster = pd.read_excel(args['roster'])

# roster.head()


#%%

def parse_grade(quiz: pd.DataFrame, roster: pd.DataFrame) -> pd.DataFrame:
    """Parse grades from quiz to roster"""
    quiz_core = quiz.loc[:,['RNumber', 'RawScore']]
    for idx, val in enumerate(quiz_core.values):
        roster.loc[roster['Student ID']==val[0],'quiz1'] = (val[1]+1)*10
    return roster



#%%
roster.to_csv(file, index=False, header=True)

if __name__ == '__main__':
    roster.to_csv(os.path.join(directory,file), index=False, header=True)
    shutil.move(args['file'], os.path.join(directory, args['file']))
    shutil.move(args['roster'], os.path.join(directory, args['roster']))

#%%
