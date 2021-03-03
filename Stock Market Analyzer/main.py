# Custom module which extracts relevant articles
import newsWebScraper

keywords = [ "Google" ]
news = newsWebScraper.collect_news( keywords )

print( "News Collected:" )
for text in news:
    print(text)
