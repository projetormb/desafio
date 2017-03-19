import unittest2

from consumo import responseTwitter, consumoTwitter

def test_responseTwitter(userName, maxTweets):

    print '    - testando response do twitter com userName : ' + userName

    response = responseTwitter(userName, maxTweets)
    return response.status_code

def test_consumoTwitter(userName, maxTweets):
    tweetsRetornados = consumoTwitter(userName, maxTweets)

    print '    - userName : ' + userName + ' maxTweets : ' + str(maxTweets)
    print '      -- retornou : ' + str(len(tweetsRetornados)) + ' tweets ...'
    print ' '

    return len(tweetsRetornados)

class MyTest(unittest2.TestCase):
    def test(self):

        print 'Testando Response do Twitter:'

        self.assertEqual(test_responseTwitter('rmbertoni', 1), 200)
        self.assertEqual(test_responseTwitter('lupcoelho', 1), 200)
        self.assertEqual(test_responseTwitter('accountdontexist', 1), 404)

        print 'Testando consumo da API do Twitter:'

        self.assertEqual(test_consumoTwitter('rmbertoni', 5), 5)
        self.assertEqual(test_consumoTwitter('lupcoelho', 10), 10)

        self.assertNotEqual(test_consumoTwitter('rmbertoni', 5000), 5)

        self.assertEqual(test_consumoTwitter('rmbertoni', 5000), 32)
        self.assertNotEqual(test_consumoTwitter('lupcoelho', 5000), 2357)
        self.assertEqual(test_consumoTwitter('lupcoelho', 5000), 200)

        self.assertEqual(test_consumoTwitter('accountdontexist', 1), 0)

if __name__ == '__main__':
    unittest2.main()
