import pandas as pd
import os

def sort(csvfile):
    df = pd.read_csv(csvfile)
    df_sorted = pd.DataFrame()

    for index in range(len(df)):

        number_of_posts = df.loc[index,"posts"]
        tag = df.loc[index,"tags"]
        print(tag ,number_of_posts)
        
        if 1000 <  number_of_posts <=  100000:
            print("between 1k & 100k")
            df_sorted = df_sorted.append({"100k":tag},ignore_index=True)
    
        elif 100000 <  number_of_posts <=  200000:
            print("between 100k & 200k")
            df_sorted = df_sorted.append({"200k":tag},ignore_index=True)
             
        elif 200000 <  number_of_posts <=  300000:
            print("between 200k & 300k")
            df_sorted = df_sorted.append({"300k":tag},ignore_index=True)
        
        
        elif 300000 <  number_of_posts <=  400000:
            print("between 300k & 400k")
            df_sorted = df_sorted.append({"400k":tag},ignore_index=True)
    
    
        elif 400000 <  number_of_posts <=  500000:
            print("between 400 & 500k")
            df_sorted = df_sorted.append({"500k":tag},ignore_index=True)
        elif 500000 <  number_of_posts <=  600000:
            print("between 500k & 600k")
            df_sorted = df_sorted.append({"600k":tag},ignore_index=True)   
             
        elif 600000 <  number_of_posts <=  700000:
            print("between 600k & 700k")
            df_sorted = df_sorted.append({"700k":tag},ignore_index=True)
        
        elif 700000 <  number_of_posts <= 800000:
            print("between 700k & 800k")
            df_sorted = df_sorted.append({"800k":tag},ignore_index=True)
    
        elif 800000 < number_of_posts <= 900000:
            print("between 800k & 900k")
            df_sorted = df_sorted.append({"900k":tag},ignore_index=True)
        
        elif 900000 < number_of_posts <= 1000000 :
            print("between 900k & 1m")
            df_sorted = df_sorted.append({"1m":tag},ignore_index=True)
            
        elif 1000000 < number_of_posts <= 2000000 :
            print("between 1m & 2m")
            df_sorted = df_sorted.append({"1m":tag},ignore_index=True)
            
        elif number_of_posts > 2000000 :
            print("great than 2m")
            df_sorted = df_sorted.append({">2m":tag},ignore_index=True)   
          
        else:
            print("loading....")

    print(df_sorted)
    df_sorted.to_csv("sorted.csv")
    
def delete_emptycols(csvfile):
    print(os.getcwd())
    cwd = os.getcwd()
    df_sorted = pd.read_csv(csvfile,index_col="Unnamed: 0")
    cols = df_sorted.columns.tolist()
    i=0
    for col in cols:
        df_sorted[col] = df_sorted[col].dropna()
        df = df_sorted[col].dropna()
        df = df.reset_index(drop=True)
        ldf = len(df)
        if ldf <3:
            nextcol = cols[i+1]
            print("we combine ",cols[i]," to ",nextcol," and we delete",cols[i])
            df_sorted[nextcol] = df_sorted[nextcol].dropna().append(df_sorted[col],ignore_index=True)
            df_sorted = df_sorted.drop(columns=[col])
            df_sorted.to_csv(cwd+"/sorted1.csv")
        i+=1
        
        
    