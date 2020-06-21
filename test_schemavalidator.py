#!/usr/local/bin/python

import unittest
from unittest import TestCase
from schemavalidator import *

schema_file = open("congi.json")
schema = json.load(schema_file)

AWS = schema["AWS"]
AZURE = schema['AZURE']

class test_ValidationService(TestCase):
    """Test case for Validator"""
    def test_valid_Azure(self):
        """Test case for valid function.
            use_case = AZURE
            data valid input"""
        instance = {"Subscription_id":"utu4tu324-u2u4t4-1hu12g4u21-uguug12u43",
                    "product_id":"123",
                    "application_id":"abc",
                    "Contact_email":"john@example.com",
                    "rules": [{"sources":["source1","source2","source3"],
                    "destinations": ["dest1","dest2"],
                    "ports": ["port1"]
                        },
                    {"sources":["source1","source2","source3"],
                    "destinations": ["dest1","dest2"],
                    "ports": ["port1","port2"]
                        }]}
        obj = ValidationService()
        response = obj.valid("AZURE",instance)
        self.assertTrue(response)

    def test_valid_AWS(self):
        """Test case for valid function.
            use_case = AWS
            data valid input"""
        instance = {"account": "accountID",
                       "sources": ["source1","source2"],
                       "destinations": ["dest1","dest2"],
                       "ports": ["port1","port2"]
            }
        obj = ValidationService()
        response = obj.valid("AWS",instance)
        self.assertTrue(response)

    def test_valid_AWS(self):
        """Test case for valid function.
            use_case = AWS
            data valid input"""
        instance = {"account": "accountID",
                    "sources": ["source1","source2"],
                    "destinations": ["dest1","dest2"],
                    "ports": ["port1","port2"]
            }
        obj = ValidationService()
        response = obj.valid("AWS",instance)
        self.assertTrue(response)

    def test_valid_unknown_source(self):
        """Test case for valid function.
            use_case = unknown
            data valid input"""
        instance = {"account": "accountID",
                    "sources": ["source1","source2"],
                    "destinations": ["dest1","dest2"],
                    "ports": ["port1","port2"]
            }
        obj = ValidationService()
        response = obj.valid("gsuit",instance)
        self.assertEqual(response,"unknown source")

    def test_validator_AWS_data_error(self):
        """Test case for validator function.
            schema = AWS
            data invalid input"""
        instance = {"account": 5434,
                    "sources": ["source1","source2"],
                    "destinations": ["dest1","dest2"],
                    "ports": ["port1","port2"]
            }
        obj = ValidationService()
        response = obj.validator(instance, AWS)
        self.assertEqual(response,(False, ["ERROR: 5434 is not of type 'string'"]))

    def test_validator_Azure_data_error(self):
        """Test case for validator function.
            schema = azure
            data invalid input"""
        instance = {"Subscription_id":456644,
                    "product_id":"22344",
                    "application_id":"abc",
                    "Contact_email":"john@example.com",
                    "rules": [{"sources":["source1","source2","source3"],
                    "destinations": ["dest1","dest2"],
                    "ports": ["port1"]
                        },
                    {"sources":["source1","source2","source3"],
                    "destinations": ["dest1","dest2"],
                    "ports": ["port1","port2"]
                        }]}
        obj = ValidationService()
        response = obj.validator(instance,AZURE)
        self.assertEqual(response,(False, ["ERROR: 456644 is not of type 'string'"]))

    def test_validator_schema_error(self):
        """Test case for validator function.
            schema = AWS
            data invalid input"""
        instance = {"account": 5434,
                    "sources": ["source1","source2"],
                    "destinations": ["dest1","dest2"],
                    "ports": ["port1","port2"]
            }
        obj = ValidationService()
        with self.assertRaises(AttributeError):
             obj.validator(instance,[])


def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_ValidationService("test_valid_Azure"))
    suite.addTest(test_ValidationService("test_valid_AWS"))
    suite.addTest(test_ValidationService("test_valid_AWS"))
    suite.addTest(test_ValidationService("test_valid_unknown_source"))
    suite.addTest(test_ValidationService("test_validator_AWS_data_error"))
    suite.addTest(test_ValidationService("test_validator_Azure_data_error"))
    suite.addTest(test_ValidationService("test_validator_schema_error"))
    return suite


if __name__=="__main__":
    result = unittest.TextTestRunner(verbosity=2).run(suite())
    failures = [str(each[0]) + str(each[1]) for each in result.failures]
    errors = [str(each[0]) + str(each[1]) for each in result.errors]
    final_result = json.dumps({"test passed":result.testsRun,"failures": failures, "errors": errors})
    

    

    
         
