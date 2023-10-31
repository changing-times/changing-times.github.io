from bs4 import BeautifulSoup
from .Parser import Parser

class ArticleParser(Parser):

    def __init__(self, html):
        super().__init__(html)


    def parse(self, publisher):
        soup = BeautifulSoup(self.html, "html.parser")
        if publisher == "New York Times":
                title = soup.select("article h1")
                author = soup.select(".last-byline") 
                paragraphs = soup.select("p[class*=evys1bk0]") #NYT
                update = soup.select("span[class*=e16638kd]")
        elif publisher == "CNN":
                title = soup.select("article h1")
                author = soup.select(".byline__name,.metadata__byline__author>a")
                paragraphs = soup.select("p[class*=zn-body__paragraph], div[class*=zn-body__paragraph], div[class*=article__content] p")
                update = soup.select("div[class*=timestamp]")
        elif publisher == "BBC":
                title = soup.select("article h1")
                author = soup.select(".author-unit,.e5xb54n2>span>strong, .e5xb54n0>span>strong, .e5xb54n1>span>strong")
                paragraphs = soup.select("article > div[data-component=text-block] p")
                update = "" 
        elif publisher == "The Blaze":
                title = soup.select("article h1[data-type=text]")
                author = soup.select(".post-author")
                paragraphs = soup.select("div[class~=body-description] > p:not(:has([class*=media]))") #TheBlaze
                update ="" 
        elif publisher == "Daily Beast":
                title = soup.select("article h1")
                author = soup.select("h4[class*=Byline__name]")
                paragraphs = soup.select("article[class*=Body] p") #Daily Beast
                update = soup.select("time>span")
        elif publisher == "National Review":
                title = soup.select("article h1")
                author = soup.select("div>div>div>.author, div[class*=article-author]")
                paragraphs = soup.select("div[class*=article-content] > p[class!=news-tip-cta], div[class*=article-content] > blockquote") #National Review
                update = soup.select("div[class*=article-content]>p:first-child") #get first child of div>p>strong 
        elif publisher == "Washington Post":
                title = soup.select("h1[class*=headline]")
                author = soup.select("a[data-qa=author-name], span[data-qa=author-name], span[class*=author-name], a[class*=author-name]")
                paragraphs = soup.select(".article-body p, p") #Washington Post
                update = soup.select("span[data-qa*=timestamp-updated-text],span[data-testid=updated-and-published-span]")
        elif publisher == "Yahoo News":
                title = soup.select("h1[data-test-locator=headline]")
                author = soup.select(".caas-author-byline-collapse")
                paragraphs = soup.find_all("p", class_=False) #Yahoo News
                update = "" 
        elif publisher == "Newsmax":
                title = soup.select("h1[class=article]")
                author = soup.select("span[itemprop=author]")
                paragraphs = soup.select("#mainArticleDiv > p") #Newsmax
                update = "" 
        elif publisher == "MarketWatch":
                title = soup.select("h1[class=article__headline]")
                author = soup.select("h4[itemprop=name]")
                paragraphs = soup.select("div[class~=article__body] > p, div[class=paywall] > p") #MarketWatch
                update = soup.select("time[class*=timestamp--update]")
        elif publisher == "Daily Mail":
                title = soup.select("#js-article-text > h2, #js-article-text > p")
                author = soup.select(".author")
                paragraphs = soup.find_all("p", class_="mol-para-with-font") #Daily Mail
                update = "" #in title
        elif publisher == "Huffington Post":
                title = soup.select("header h1, header time")
                author = soup.select("div[class*=entry__byline__author],div[class*=author-card__name]>a[class*=author-card__link],.entry-wirepartner__byline,.wire-partner-component")
                paragraphs = soup.find_all("p") #Huffington Post
                update = soup.select("time, span[aria-label*=Updated]")
        elif publisher == "New York Post":
                title = soup.select("header > h1[class*=headline], a:-soup-contains('Updated'), .article-header > h1[class*=postid], .article-header > p[class=byline-date]")
                author = soup.select(".byline__author>a,.byline>a,.byline__author>span,.author-byline span, div[id=author-byline]>p[class*=byline]")
                paragraphs = soup.select("div[class*=entry-content] > p") #New York Post
                update = "" #in title
        elif publisher == "The Guardian":
                title = soup.select("h1[class=css-dxy9hs],h1[class=dcr-125vfar]")
                author = soup.select("a[rel=author]")
                paragraphs = soup.select("p , div[class=dcr-km9fgb]") #The Guardian
                update = soup.select("aside[data-gu-name*=meta]") #last modified
        elif publisher == "OAN":
                title = soup.select("header > h1")
                paragraphs = soup.select("div[class~=entry-content] > p, div[class~=entry-content] h5") #OAN
                author = ""
                update = "div[class~=entry-content]"
        elif publisher == "Fox News":
                title = soup.select("time:-soup-contains('Updated'), header > h1, header > h2")
                author = soup.select(".author-byline>span>span>a")
                paragraphs = soup.select("div[class=article-body] > p") #Fox News
                update = "" 
        elif publisher == "The Hill":
                title = soup.select("h1[class=title]")
                author = soup.select("section[class*=submitted-by]>span>a,.submitted-wrp>span>a")
                paragraphs = soup.select("div[class*=field-item] > p,div[class*=article__text]>p") #The Hill
                update = "" 
        elif publisher == "The Epoch Times":
                title = soup.select("div[class=post_title], div[class=date]")
                author = soup.select(".author_name,.author>a>span[class*=info]")
                paragraphs = soup.find_all("p") #The Epoch Times
                update = ""
        elif publisher == "BuzzFeed":
                title = soup.select("article h1")
                paragraphs = soup.select("p, span:has(:not([class*=xs-block]))") #BuzzFeed

        body_contents = []
        title_contents = []
        author_contents = []
        list2 = []
        update_contents = []
        timestamp_contents = []
        filter_list = ["our Terms of Service and Privacy Policy", "All Rights Reserved", "Over the Past 60 Days", "Fear & Greed Index", "Latest Market News", "All rights reserved", "Last modified", "Reporter, Huffpost", "By signing up you agree", "curated by Post editors", "Sign in", "News•", "Perspective•", "Analysis•", "Review•", "Sign up for"]

        for t in title:
            title_contents.append(t.text)
        for paragraph in paragraphs:
            if(not any(x in paragraph.text for x in filter_list)):
                body_contents.append(paragraph.text)
        for a in author:
            if(a):
                if("By " in a.text):
                    text2 = a.text[3:]
                else:
                    text2 = a.text
                text2 = text2.lower()
                if(" and " in text2):
                    list2.append(text2.split(" and "))
                if(" & " in text2):
                    list2.append(text2.split(" & "))
                if(text2 not in author_contents and not list2):
                    author_contents.append(text2)
                if(list2):
                    author_contents.append(list2)
        for u in update:
            if(u):
                print(u)
                u = str(u.text)
                u = u.lower()
                update_contents.append(u)
            pass
        for ts in timestamp:
            timestamp_contents.append(ts.text)

        self.article_title = title_contents
        self.article_author = author_contents
        self.article_text = body_contents
        self.article_update = update_contents
        self.article_timestamp = timestamp_contents
