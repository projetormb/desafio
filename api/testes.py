import unittest2

from consumo import consumoTwitter

def test_consumoTwitter(userName, maxTweets):
    tweetsRetornados = consumoTwitter(userName, maxTweets)
    
    print 'maxTweets: ' + str(maxTweets) + ' retornados: ' + str(len(tweetsRetornados))

    return len(tweetsRetornados)

class MyTest(unittest2.TestCase):
    def test(self):
        self.assertEqual(test_consumoTwitter('rmbertoni', 5), 5)
        self.assertEqual(test_consumoTwitter('lupcoelho', 10), 10)

        self.assertNotEqual(test_consumoTwitter('rmbertoni', 5000), 5)

        self.assertEqual(test_consumoTwitter('rmbertoni', 5000), 32)
        self.assertNotEqual(test_consumoTwitter('lupcoelho', 5000), 2357)
        self.assertEqual(test_consumoTwitter('lupcoelho', 5000), 200)

        self.assertEqual(test_consumoTwitter('accountdontexist', 1), 0)

if __name__ == '__main__':
    unittest2.main()

