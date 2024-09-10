import unittest
from dateutil import parser
from pdfarranger.metadata import compareDates

class TestIsMinorFunction(unittest.TestCase):

    def test_modified_before_created(self):
        # Teste quando a data de modificação é anterior à de criação
        modified_date = parser.parse("2024-09-09T12:00:00")
        created_date = parser.parse("2024-09-10T12:00:00")
        result = compareDates(modified_date, created_date)
        self.assertTrue(result)

    def test_modified_equal_to_created(self):
        # Teste quando a data de modificação é igual à de criação
        modified_date = parser.parse("2024-09-10T12:00:00")
        created_date = parser.parse("2024-09-10T12:00:00")
        result = compareDates(modified_date, created_date)
        self.assertTrue(result)

    def test_modified_after_created(self):
        # Teste quando a data de modificação é posterior à de criação
        modified_date = parser.parse("2024-09-11T12:00:00")
        created_date = parser.parse("2024-09-10T12:00:00")
        result = compareDates(modified_date, created_date)
        self.assertFalse(result)
