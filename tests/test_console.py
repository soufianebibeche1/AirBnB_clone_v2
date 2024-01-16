import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsoleCreateParams(unittest.TestCase):
    def test_create_with_params(self):
        console = HBNBCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            console.onecmd('create State name="California"')
            state_id = mock_stdout.getvalue().strip()
        
        self.assertTrue(state_id)

    def test_create_with_multiple_params(self):
        console = HBNBCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            console.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
            place_id = mock_stdout.getvalue().strip()
        
        self.assertTrue(place_id)

if __name__ == '__main__':
    unittest.main()
