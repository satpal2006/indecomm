'''
    Unit test of maxprice module
'''
import unittest
import maxprice
class TestStock(unittest.TestCase):

    def test_max_price(self):
        stock = maxprice.Stock();
        data = stock.getMaxPrice(None)
        #check the length of data equals to length of company
        self.assertEqual(data.__len__(), 5)

    def test_max_price_valid_data_company_A(self):
        '''
        test company name A and its max price.
        :return: void
        '''
        stock = maxprice.Stock();
        data = stock.getMaxPrice(None)
        #check the name of first company equals to Company-A
        self.assertEqual(data[0][0], 'Company-A')
        #check max stock value of Company-A is 1000
        self.assertEqual(int(data[0][3]), 1000)

    def test_max_price_valid_data_company_B(self):
        '''
        test company name B and its max price.
        :return: void
        '''
        stock = maxprice.Stock();
        data = stock.getMaxPrice(None)
        #check the name of first company equals to Company-B
        self.assertEqual(data[1][0], 'Company-B')
        #check max stock value of Company-A is 1000
        self.assertEqual(int(data[1][3]), 986)

    def test_max_price_valid_data_company_C(self):
        '''
        test company name C and its max price.
        :return: void
        '''
        stock = maxprice.Stock();
        data = stock.getMaxPrice(None)
        #check the name of first company equals to Company-C
        self.assertEqual(data[2][0], 'Company-C')
        #check max stock value of Company-A is 1000
        self.assertEqual(int(data[2][3]), 995)

    def test_max_price_valid_data_company_D(self):
        '''
        test company name D and its max price.
        :return: void
        '''
        stock = maxprice.Stock();
        data = stock.getMaxPrice(None)
        #check the name of first company equals to Company-D
        self.assertEqual(data[3][0], 'Company-D')
        #check max stock value of Company-A is 1000
        self.assertEqual(int(data[3][3]), 999)

    def test_max_price_valid_data_company_E(self):
        '''
        test company name E and its max price.
        :return: void
        '''
        stock = maxprice.Stock();
        data = stock.getMaxPrice(None)
        #check the name of first company equals to Company-E
        self.assertEqual(data[4][0], 'Company-E')
        #check max stock value of Company-A is 1000
        self.assertEqual(int(data[4][3]), 997)

    @unittest.expectedFailure
    def test_max_price_invalid_file(self):
        stock = maxprice.Stock();
        data = stock.getMaxPrice('invalid.csv')
        #check the length of data equals to length of company
        self.assertEqual(data.__len__(), 5)


if __name__ == '__main__':
    unittest.main()