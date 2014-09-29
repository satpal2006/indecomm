'''
    This module will help in getting max price of stock of company,
    its complexity is O(n*m), where n is number of data of company and m is number of companies.
'''
import csv, sys
class Stock:
    def __init__(self):
        self.formatter = None;

    def getMaxPrice(self, name):
        with open(name, 'rb') as csvfile:
            try:
                reader = csv.reader(csvfile)
                companies = reader.next()[2:]
                complen = companies.__len__();

                #list formatter for company--[[name,year,month,price],[name,year,month,price]......]
                comp_formatter = [[name,None,None,0] for name in companies]

                #iterate each row and find max with the stored value in temp array.
                for row in reader:
                    for i in xrange(complen):
                        if int(row[i+2]) > int(comp_formatter[i][3]):
                            comp_formatter[i][1] = row[0];
                            comp_formatter[i][2] = row[1];
                            comp_formatter[i][3] = row[i+2];
                self.formatter = comp_formatter

            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (name, reader.line_num, e))
            except:
                print "Unexpected error:", sys.exc_info()[0];
                raise

        return self.formatter;

if __name__ == '__main__':
    fileName = 'test_shares_data.csv'
    utility = Stock();
    print utility.getMaxPrice(fileName)
