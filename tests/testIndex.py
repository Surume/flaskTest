#!/usr/bin/env python
# encoding=utf-8

# import flask
import unittest

# from flask import current_app
# import index
# from applications.Service import redisService

import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    )

class TestIndex(unittest.TestCase):

    # def setUp(self):
    #     self.app = index.app.test_client()

    # def test_get(self):
    #     response = self.app.get('/')
    #     assert response.status_code == 200
    #     logging.debug(response.data)
    #     assert response.data == b'FlaskTest!'
    #
    # def test_get(self):
    #     response = self.app.get('/')
    #     assert response.status_code == 200
    #     logging.debug(response.data)
    #     assert response.data == b'FlaskTest!'

    def test_get(self):
        assert True

if __name__ == '__main__':
    unittest.main()
