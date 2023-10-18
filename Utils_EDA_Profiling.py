import pandas as pd
import os
import re

pd.options.display.max_rows = None
pd.options.display.max_columns = None


def fix_column(x):
    if x[-1]=='.':
        x = x[:-1]
    x = x.replace('.','_')
    x = x.replace('/','_')
    x = x.replace('&', '_')
    x = x.replace(' ','_')
    x = re.sub('_+','_',x)
    x = x.lower()
    return x

def check_missing(df):
    tmp = df
    tmp = tmp.fillna('')
    num = tmp.shape[0]
    tmp = tmp.apply(lambda x: x=='').sum().reset_index()
    tmp.columns = ['index','count']
    tmp['count'] = tmp['count']/num
    tmp['percent'] = tmp['count'].apply(lambda x: round(x,3)*100)
    del tmp['count']
    print('Missing:')
    return tmp

def read_data(path, skiprows=0):
    file_name, file_type = os.path.splitext(path)
    if file_type.lower() in ['.xlsx']:
        df = pd.read_excel(path, skiprows=skiprows)
    elif file_type.lower() in ['.csv']:
        df = pd.read_csv(path, skiprows=skiprows)
    df.head(2).T
    df.columns = [fix_column(x) for x in df.columns]
    df.fillna('', inplace=True)
    print("Num:", df.shape[0])
    display(df.head(2).T)
    return df


def get_single_variable(df, feature_col, id_col='smc'):
    tmp = df
    res = tmp.groupby(feature_col)[id_col].count().reset_index()
    return res





def main():
    df = read_data('./data/XXXX.xlsx', skiprows=0)
    check_missing(df)
    get_single_variable(df, 'XXXX')


if __name__=='__main__':
    main()

    print("Done!")