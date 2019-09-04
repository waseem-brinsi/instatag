import pandas as pd
import numpy as  np


def gen(sorted_file):
    df_sorted = pd.read_csv(sorted_file,index_col="Unnamed: 0") 

    cols = df_sorted.columns.tolist()
    cols.reverse()
    
    print("this",cols)
    with open("hashtags.txt","a") as file:
        tagl = []
        while len(tagl) != 30:

            for col in cols:
                df=df_sorted[col].dropna()
                df = df.reset_index(drop=True)
                tags = df.sample(n=1).tolist()
                tagl += tags
                tagl = list(dict.fromkeys(tagl))


                if len(tagl)==30:
                    print(tagl,type(tagl))
                    print(len(tagl))
                    
                    break

        for el in tagl:
            print(el ,end=" ")
            el=el+" "
            file.write(el)
                
        print("you need ","tags")