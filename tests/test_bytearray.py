import unittest
from jnius import autoclass

class StringArgumentForByteArrayTest(unittest.TestCase):

    def test_string_arg_for_byte_array(self):
        # the ByteBuffer.wrap() accept only byte[].
        ByteBuffer = autoclass('java.nio.ByteBuffer')
        self.assertIsNotNone(ByteBuffer.wrap('hello world'))

    def test_string_arg_with_signed_char(self):
        ByteBuffer = autoclass('java.nio.ByteBuffer')
        self.assertIsNotNone(ByteBuffer.wrap('\x00\xffHello World\x7f'))

    def test_fill_byte_array(self):
        arr = [0, 0, 0]
        Test = autoclass('org.jnius.BasicsTest')()
        Test.fillByteArray(arr)
        self.assertEquals(
            arr,
            [127, 1, -127])
