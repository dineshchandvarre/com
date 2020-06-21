#!/usr/local/bin/python

import json
import jsonschema
from jsonschema import Draft3Validator

schema_file = open("congi.json")
schema = json.load(schema_file)

AWS = schema["AWS"]
AZURE = schema['AZURE']

class ValidationService:        
    def valid(self, use_case, data):
        if use_case=='AWS':
            return self.validator(data, AWS)
        elif use_case=='AZURE':
            return self.validator(data, AZURE)
        else:
            return "unknown source"

    def validator(self,data,schema):
        messages=[]
        is_valid=True
        validator = Draft3Validator(schema)
        for i in data:
            try:
                validator.validate({str(i):data[i]})
            except Exception as e:
                print(e.message)
                messages.append('ERROR: ' + e.message)
        if messages:
            is_valid = False
            return(is_valid,messages)
        return is_valid

if __name__=="__main__":
    Aws_input_example={"account": "accountID",
                       "sources": ["source1","source2"],
                       "destinations": ["dest1","dest2"],
                       "ports": ["port1","port2"]
            }
    Azure_input_example = {"Subscription_id":"utu4tu324-u2u4t4-1hu12g4u21-uguug12u43",
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
    res_Azure = obj.valid("AZURE",Azure_input_example)
    res_Aws = obj.valid("AWS",Aws_input_example)
    print(res_Azure,"azure")
    print(res_Aws,"Aws")
