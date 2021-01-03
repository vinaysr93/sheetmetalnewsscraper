from bs4 import BeautifulSoup
import requests
import re
import tkinter as tk
class News():

    def fabricator(self):
        res = requests.get("https://www.thefabricator.com/")

        soup = BeautifulSoup(res.text, "html.parser")
        ltfb = {}
        posts = soup.findAll('a', attrs={"class": "post-link"})
        cleaned_post = []
        for x in range(len(posts)):
            if x % 2 == 0:
                continue
            else:
                cleaned_post.append(posts[x])

        count=0
        for post in cleaned_post:
            np = str(post)

            link = re.search('href="(.*?)"', np)
            title = re.search('title="(.*?)"', np)
            ltfb[title.group(1)] = "thefabricator.com"+link.group(1)
            count=count+1
            if count>10:
                break


        return (ltfb)





    def fractory(self):
        '''Scrapes blog articles from fractory.com website'''
        res = requests.get("https://fractory.com/engineering-blog/")
        soup = BeautifulSoup(res.text, "html.parser")
        posts = soup.findAll('h3', attrs={"class": "c-blog__post-title"})
        cleaned_posts=[]

        for y in range(len(posts)):

            if y%2==0:
                cleaned_posts.append(posts[y])


        # Links and Titles of Fractory
        ltfr={}
        for post in posts:

            sp = str(post)
            link = re.search('href="(.*?)"', sp)
            title = re.search('a href(.*)">(.*?)<', sp)
            ltfr[title.group(2)]=link.group(1)

        return(ltfr)


