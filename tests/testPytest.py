# setup_function
# test_numbers_3_4
# .teardown_function
# setup_function
# test_strings_a_3
# .teardown_function
# in class TestUM -> setup_class
# in class TestUM -> setup_method
# in class TestUM -> setup
# test_numbers_5_6
# .in class TestUM -> teardown
# in class TestUM -> teardown_method
# in class TestUM -> setup_method
# in class TestUM -> setup
# test_strings_b_2
# .in class TestUM -> teardown
# in class TestUM -> teardown_method
# in class TestUM -> teardown_class
# teardown_module


#
#
# def setup_module():
#     print ("setup_module")  # first
#
# def teardown_module():
#     print ("teardown_module")
#
# def setup_function(function):
#     print ("setup_function")  # second
#
# def teardown_function(function):
#     print ("teardown_function")
#
# def test_numbers_3_4():
#     print 'test_numbers_3_4' # third
#
# def test_strings_a_3():
#     print 'test_strings_a_3'
#
#
# class TestStory:
#
#     def setup_module(self):
#         self.y = 20
#
# class TestUM:
#
#
#     def setup(self):
#         self.x = 10
#         print ("in class TestUM -> setup")
#         print "value of y"
#
#     def teardown(self):
#         print ("in class TestUM -> teardown")
    #
    # def setup_class(cls):
    #     print ("in class TestUM -> setup_class")
    #
    # def teardown_class(cls):
    #     print ("in class TestUM -> teardown_class")
    #
    # def setup_method(self, method):
    #     print ("in class TestUM -> setup_method")
    #
    # def teardown_method(self, method):
    #     print ("in class TestUM -> teardown_method")

    # def test_numbers_5_6(self):
    #     print 'test_numbers_5_6 with x = ' + self.x
    #
    # def test_strings_b_2(self):
    #     print 'test_strings_b_2'
