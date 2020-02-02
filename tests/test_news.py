import unittest 
from app.models import News

 
class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of News Class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''

        self.new_news = News('BuzzfeedNews', 'A Pro-Trump Blog Doxed A Chinese Scientist It Falsely Accused Of Creating The Coronavirus As A Bioweapon', 'The scientist\'s name, photo, email, and a telephone number are being spread across American social media.', 'https://img.buzzfeed.com/buzzfeed-static/static/2020-01/31/20/asset/644212146cbb/sub-buzz-1115-1580503700-1.jpg?downsize=1040%3A%2A&output-quality=auto&output-format=auto', 'https://www.buzzfeednews.com/article/ryanhatesthis/a-pro-trump-blog-has-doxed-a-chinese-scientist-it-falsely','2020-02-02T16:03:03Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
    
    def test_init(self):

        self.assertEqual(self.new_news.author,'BuzzfeedNews')
        self.assertEqual(self.new_news.title,'A Pro-Trump Blog Doxed A Chinese Scientist It Falsely Accused Of Creating The Coronavirus As A Bioweapon')
        self.assertEqual(self.new_news.description,'The scientist\'s name, photo, email, and a telephone number are being spread across American social media.')
        self.assertEqual(self.new_news.urlToImage,'https://img.buzzfeed.com/buzzfeed-static/static/2020-01/31/20/asset/644212146cbb/sub-buzz-1115-1580503700-1.jpg?downsize=1040%3A%2A&output-quality=auto&output-format=auto')
        self.assertEqual(self.new_news.url,'https://www.buzzfeednews.com/article/ryanhatesthis/a-pro-trump-blog-has-doxed-a-chinese-scientist-it-falsely')
        self.assertEqual(self.new_news,publishedAt,'2020-02-02T16:03:03Z')



if __name__ == '__main__':
    unittest.main()