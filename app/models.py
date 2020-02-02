class News:
    '''
    News class that defines the news articles object
    '''

    def __init__(self, author, title, description, urlToImage, url, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.publishedAt = publishedAt

class Sources:
    '''
    Sources class that defines the news sources object
    '''

    def __init__(self, id, name, description, category, country, url):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.country = country
        self.url = url