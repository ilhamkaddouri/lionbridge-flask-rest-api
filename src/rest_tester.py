
import unittest
from test_user_router import UserRouterTest

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(UserRouterTest)
	unittest.TextTestRunner().run(suite)