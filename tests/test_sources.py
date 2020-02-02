import unittest 
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of Sources Class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''

        self.new_source = Sources('quartz', 'QuartzNews','Global news and business insights','business','usa','https://qz.com/')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    
    def test_init(self):

        self.assertEqual(self.new_source.id,'quartz')
        self.assertEqual(self.new_source.name,'QuartzNews')
        self.assertEqual(self.new_source.description,'Global news and business insights')
        self.assertEqual(self.new_source.category,'business')
        self.assertEqual(self.new_source.country,'usa')
        self.assertEqual(self.new_source.url,'https://qz.com/')


if __name__ == '__main__':
    unittest.main()