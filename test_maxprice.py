'''
    Unit test of maxprice module
'''
import unittest
import maxprice
class TestStock(unittest.TestCase):

    def test_max_price(self):
        stock = maxprice.Stock();
        data = stock.getMaxPrice('test_shares_data.csv')
        #check the length of data equals to length of company
        self.assertEqual(data.__len__(), 5)

    def test_max_price_valid_data(self):
        stock = maxprice.Stock();
        data = stock.getMaxPrice('test_shares_data.csv')
        #check the name of first company equals to Company-A
        self.assertEqual(data[0][0], 'Company-A')
        #check max stock value of Company-A is 1000
        self.assertEqual(int(data[0][3]), 1000)

    @unittest.expectedFailure
    def test_max_price_invalid_file(self):
        stock = maxprice.Stock();
        data = stock.getMaxPrice('invalid.csv')
        #check the length of data equals to length of company
        self.assertEqual(data.__len__(), 5)


if __name__ == '__main__':
    unittest.main()