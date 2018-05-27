
import unittest

from kalliope.core.NeuronModule import InvalidParameterException
from youtube_searcher import Youtube_searcher


class TestYoutubeSearcher(unittest.TestCase):


    def test_YoutubeSearcher(self):

        #test with valid channel name
        parameters = {"channel":"scott manley"}
        self.assertEqual(Youtube_searcher(**parameters).message["title"],"Why Some Astronomers Think There's An Interstellar Asteroid Near Jupiter")
        self.assertEqual(Youtube_searcher(**parameters).message["returncode"],"None")

        #test with invalid channel name
        parameters = {"channel":"scajosijfsdafdsk"}
        self.assertEqual(Youtube_searcher(**parameters).message["title"],"None")
        self.assertEqual(Youtube_searcher(**parameters).message["returncode"],"Nochannelfound")

        #test with valid channel name but no videos
        parameters = {"channel":"RadekKouzelnik"}
        self.assertEqual(Youtube_searcher(**parameters).message["title"],"None")
        self.assertEqual(Youtube_searcher(**parameters).message["returncode"],"Novideofound")

if __name__ == '__main__':
    unittest.main()
