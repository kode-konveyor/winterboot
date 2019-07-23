import unittest
from winterboot.Autowired import Autowired


class testDTO(unittest.TestCase):

    def setUp(self):
        self.exampleDTO : ExampleDTO = Autowired('ExampleDTOFactory').call()

    def testDTO_can_be_created(self):
        self.assertEqual(None, self.exampleDTO.existingAttribute)

    def test_allowed_attribute_can_be_written(self):
        self.exampleDTO.existingAttribute = 2
        self.assertEqual(2, self.exampleDTO.existingAttribute)

    def test_nonexisting_attribute_cannot_be_read(self):
        self.assertRaises(AttributeError, lambda: self.exampleDTO.nonExistingAttribute)


    def setNonExistingAttribute(self):
        self.exampleDTO.nonExistingAttribute = 2

    def test_nonexisting_attribute_cannot_be_written(self):
        self.assertRaises(AttributeError, self.setNonExistingAttribute)


if __name__ == "__main__":
    unittest.main()