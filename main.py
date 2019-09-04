import sys
import time
import os
import pandas as pd
from selenium import webdriver
from allhashtag import all_hashtag
from Posts import Posts_number
from sorting import sort, delete_emptycols
from generate import gen
from upload import upload

driver=webdriver.Chrome(r"./chromedriver")
#argument 

if len(sys.argv) == 2:
    tagword =str(sys.argv[1])
    print(tagword)
else:
    print("entre the tag")
    exit()    

df_maintags = all_hashtag(driver, tagword)
print(df_maintags)
lst_maintags = df_maintags.values.tolist()

for tag in lst_maintags:
    print(tag[0])
    print(type(tag[0]))
    df_subtags = all_hashtag(driver, tag[0])
    print(df_subtags)
    df_maintags=df_maintags.append(df_subtags,ignore_index=True)
    print(df_maintags)
df_maintags = df_maintags.drop_duplicates("tags")
print(df_maintags)
print(type(df_maintags))
tagslist = df_maintags["tags"]
print(tagslist)

dfPosts=Posts_number(tagslist,tagword)
print(dfPosts)


df_maintags.to_csv("Tags.csv")
Tags = pd.read_csv("Tags.csv")
Posts = pd.read_csv("Posts.csv")
df_result = Tags.join(Posts)
df_result = df_result.drop(columns=["Unnamed: 0"])
df_result = df_result.sort_values(by=["posts"]) 

##########create folder and change directory################
try:
    os.makedirs(tagword)
except:
    print("folder exist")
    
os.chdir(tagword)
######################################################################

print(df_result)
name="#"+tagword+".csv"
df_result.to_csv(name,index=False)

sort(name)
delete_emptycols("sorted.csv")

gen("sorted1.csv")
os.chdir("..")
path = os.path.join(tagword,"hashtags.txt")
tagword= tagword+".txt"
upload(tagword,path)




