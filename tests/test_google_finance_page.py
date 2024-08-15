from pytest import mark
from pages.google_finance_page import GoogleFinancePage
import configs
import inspect


class TestGoogleFinance:

    def get_classname(self):
        return self.__class__.__name__

    @mark.stock_symbols
    def test_retrieves_stock_symbols_and_compare_with_test_data(self, driver):
        this_function_name = inspect.currentframe().f_code.co_name
        gf = GoogleFinancePage(driver)
        try:
            gf.get_url(configs.url)
            assert gf.google_finance_title() == configs.google_finance_title

            # Print all stock symbols that are in collection but not in given test data
            unique_to_test_data = set(gf.you_may_be_interested_collection()).difference(set(configs.given_test_data))
            print(unique_to_test_data)

            # Print all stock symbols that are in given test data but not in collection
            unique_to_you_may_be_interested_in = set(configs.given_test_data).difference(
                set(gf.you_may_be_interested_collection()))
            print(unique_to_you_may_be_interested_in)
        except AssertionError:
            gf.take_screenshot(self.get_classname(), this_function_name)
            raise
