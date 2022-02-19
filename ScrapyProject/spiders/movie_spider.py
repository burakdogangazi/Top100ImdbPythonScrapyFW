import scrapy


class MoviesSpider(scrapy.Spider):
    name = "movies"
    
    start_urls = [
        "https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"
    ]

    def parse(self, response):
        
        movie_name = response.css("h3.lister-item-header a::text").extract()
        movie_ranking = response.css("span.lister-item-index.unbold.text-primary::text").extract()
        movie_certificate = response.css("p.text-muted span.certificate::text").extract()
        movie_runtime = response.css("p.text-muted span.runtime::text").extract()
        movie_genre = response.css("p.text-muted span.genre::text").extract()
        movie_imdb = response.css("div.ratings-bar div.inline-block.ratings-imdb-rating strong::text").extract()
        i = 0
        while ( i < len(movie_ranking)):
            yield {
                "ranking" : movie_ranking[i],
                "name" : movie_name[i],
                "certificate" : movie_certificate[i],
                "runtime" : movie_runtime[i],
                "genre" : movie_genre[i],
                "rating" : movie_imdb[i]
            } 
            i+=1
       
       