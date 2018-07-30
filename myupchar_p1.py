import scrapy
from urllib.parse import urljoin
url_news = ["https://www.myupchar.com/disease/"]
class HindiDiseaseUpchharSpider(scrapy.Spider):
    name = "hindi_disease_upchaar"
    start_urls = url_news
    def parse(self, response):
        articles =  response.xpath("//*[contains(@id, 'tab1')]//a/@href").extract()
        for a in articles:
            url = urljoin(response.url, a)
            yield scrapy.Request(url, callback=self.parse_article)
    def parse_article(self, response):
        data = {
                'article_name': response.xpath("//div[@class ='col-md-12']//h1/text()").extract_first(),
                'article': response.xpath("//section[@class='para']//div[@class='col-md-12 col-sm-12 col-xs-12']//p/text()|//section[@class='para']//div[@class='col-md-12 col-sm-12 col-xs-12']//div[@class='sticky-container']//h2//text()|//section[@class='para']//div[@class='col-md-12 col-sm-12 col-xs-12']//div/h3[@dir='ltr']//text()").extract()
            }
        try:
            with open("myupchaar/"+data["article_name"].split("-")[1]+".txt","w") as g:
                g.write(data["article_name"].split("-")[0])
                g.write("\n")
                for para in data["article"]:
                    g.write(para)
                    g.write("\n")
        except:
           with open("myupchaar/"+data["article_name"]+".txt","w") as g:
                g.write(data["article_name"])
                g.write("\n")
                for para in data["article"]:
                    g.write(para)
                    g.write("\n")
