import unittest
from post import RedditPost
from reddit_api_call import call, StatusCodeError

class Tests(unittest.TestCase):
    def test_RedditPost(self):
        test_post = RedditPost({})
        self.assertEqual(test_post.title, False)
        self.assertEqual(test_post.url, False)
        self.assertEqual(test_post.thumbnail, False)
        self.assertEqual(test_post.text, False)
        self.assertEqual(test_post.score, False)
        test_post = RedditPost({
            'title': 'blah',
            'score': 'blah',
            'permalink': 'blah'
        })
        self.assertEqual(test_post.title, 'blah')
        self.assertEqual(test_post.url, 'blah')
        self.assertEqual(test_post.thumbnail, False)
        self.assertEqual(test_post.text, False)
        self.assertEqual(test_post.score, 'blah')
        test_post = RedditPost({
            'title': 'blah',
            'score': 'blah',
            'permalink': 'blah',
            'thumbnail': 'blah'
        })
        self.assertEqual(test_post.title, 'blah')
        self.assertEqual(test_post.url, 'blah')
        self.assertEqual(test_post.thumbnail, 'blah')
        self.assertEqual(test_post.text, False)
        self.assertEqual(test_post.score, 'blah')
        test_post = RedditPost({
            'title': 'blah',
            'score': 'blah',
            'permalink': 'blah',
            'thumbnail': 'default'
        })
        self.assertEqual(test_post.title, 'blah')
        self.assertEqual(test_post.url, 'blah')
        self.assertEqual(test_post.thumbnail, False)
        self.assertEqual(test_post.text, False)
        self.assertEqual(test_post.score, 'blah')
        test_post = RedditPost({
            'title': 'blah',
            'score': 'blah',
            'permalink': 'blah',
            'thumbnail': 'nsfw'
        })
        self.assertEqual(test_post.title, 'blah')
        self.assertEqual(test_post.url, 'blah')
        self.assertEqual(test_post.thumbnail, False)
        self.assertEqual(test_post.text, False)
        self.assertEqual(test_post.score, 'blah')
        test_post = RedditPost({
            'title': 'blah',
            'score': 'blah',
            'permalink': 'blah',
            'thumbnail': 'nsfw',
            'text': 'blah'
        })
        self.assertEqual(test_post.title, 'blah')
        self.assertEqual(test_post.url, 'blah')
        self.assertEqual(test_post.thumbnail, False)
        self.assertEqual(test_post.text, False)
        self.assertEqual(test_post.score, 'blah')
        test_post = RedditPost({
            'title': 'blah',
            'score': 'blah',
            'permalink': 'blah',
            'thumbnail': 'self',
            'selftext': 'blah'
        })
        self.assertEqual(test_post.title, 'blah')
        self.assertEqual(test_post.url, 'blah')
        self.assertEqual(test_post.thumbnail, False)
        self.assertEqual(test_post.text, 'blah')
        self.assertEqual(test_post.score, 'blah')

    def test_call(self):
        self.assertRaises(StatusCodeError, call, "kadfjaslkfdjas;lkfjas;lknaknv")
        posts = call("funny")
        self.assertEqual(len(posts), 26)
        self.assertTrue(isinstance(posts[0], RedditPost))
        try:
            call("alksdjf;alskjdf;aslkjfewoin")
        except StatusCodeError as e:
            self.assertEquals(e.code, 404)

if __name__ == '__main__':
    unittest.main()