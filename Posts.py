#tage number of posts
import time
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
from converter import convert_to_number


def Posts_number(taglist,tagword):
    tags = taglist
    df_posts1=pd.DataFrame({"posts":[]})
    for tag in tags:
        tag=tag.replace("#","")
        while True:
            try:
                url ="https://www.instagram.com/explore/tags/"+tag
                source = requests.get(url).text
                soup = BeautifulSoup(source, 'html.parser')
                meta = soup.find_all("meta",limit=8)
                posts = meta[7]['content']
                posts=posts.split()
                posts=posts[0]
                print(posts)
                
                posts = convert_to_number(posts)
                
                print(posts)
                print(tag+" : "+str(posts))
                df_posts = pd.DataFrame({"posts":[posts]})
                df_posts1=df_posts1.append(df_posts,ignore_index=True)
                break
            
            except:
                print("error")
                continue
            
            
    print(df_posts1)

    df_posts1.to_csv("Posts.csv",index=False)
    print("finished")
    return df_posts1
