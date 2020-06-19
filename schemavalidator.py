import jsonschema
#from jsonschema import DraftValidator

class ValidationService:        
    @staticmethod
    def valid(use_case,data):
        if use_case=='AWS':
            return validator(data,AWS)
        elif use_case=='AZURE':
            return validator(data,AZURE)
        elif use_case=='Manual':
            return True


def validator(data,use_case):

    schema=use_case
    v= jsonschema.Draft3Validator(schema)
    messages=[]
    errors= sorted(v.iter_errors(data),key=lambda e:e.path)
    for error in errors:
        messages.append(('ERROR: '+ error.message))
    is_valid=True
    if errors:
        is_valid = False
        return(is_valid,messages)
    return is_valid



AWS={
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "account": {
      "type": "string"
    },
    "sources": {
      "type": "array",
      "items": [
        {
          "type": "string"
        },
        {
          "type": "string"
        }
      ]
    },
    "destinations": {
      "type": "array",
      "items": [
        {
          "type": "string"
        },
        {
          "type": "string"
        }
      ]
    },
    "ports": {
      "type": "array",
      "items": [
        {
          "type": "string"
        },
        {
          "type": "string"
        }
      ]
    }
  },
  "required": [
    "account",
    "sources",
    "destinations",
    "ports"
  ]
}


Aws_input_example={
    "account": "accountID",
    "sources": ["source1","source2"],
    "destinations": ["dest1","dest2"],
    "ports": ["port1","port2"]
}



AZURE={
"$schema": "http://json-schema.org/draft-04/schema#",
"type": "object",
"properties": {
"Subscription_id": {
    "type": "string"
},
"product_id": {
    "type": "string"
},
"application_id": {
    "type": "string"
},
"Contact_email": {
    "type": "string"
},
"rules": {
    "type": "array",
    "items": [
    {
        "type": "object",
        "properties": {
        "sources": {
            "type": "array",
            "items": [
            {
                "type": "string"
            },
            {
                "type": "string"
            },
            {
                "type": "string"
            }
            ]
        },
        "destinations": {
            "type": "array",
            "items": [
            {
                "type": "string"
            },
            {
                "type": "string"
            }
            ]
        },
        "ports": {
            "type": "array",
            "items": [
            {
                "type": "string"
            },
            {
                "type": "integer"
            }
            ]
        }
        },
        "required": [
        "sources",
        "destinations",
        "ports"
        ]
    },
    {
        "type": "object",
        "properties": {
        "sources": {
            "type": "array",
            "items": [
            {
                "type": "string"
            },
            {
                "type": "string"
            },
            {
                "type": "string"
            }
            ]
        },
        "destinations": {
            "type": "array",
            "items": [
            {
                "type": "string"
            },
            {
                "type": "string"
            }
            ]
        },
        "ports": {
            "type": "array",
            "items": [
            {
                "type": "string"
            },
            {
                "type": "string"
            }
            ]
        }
        },
        "required": [
        "sources",
        "destinations",
        "ports"
        ]
    }
    ]
}
},
"required": [
"Subscription_id",
"product_id",
"application_id",
"Contact_email",
"rules"
]
}    
Azure_input_example = {"Subscription_id":"utu4tu324-u2u4t4-1hu12g4u21-uguug12u43",
"product_id":"abc",
"application_id":"abc",
"Contact_email":"john@example.com",
"rules": [{
    "sources":["source1","source2","source3"],
    "destinations": ["dest1","dest2"],
    "ports": ["port1"]
},
{
    "sources":["source1","source2","source3"],
    "destinations": ["dest1","dest2"],
    "ports": ["port1","port2"]
}]
}



if __name__=="__main__":
    print(validator(Azure_input_example,AZURE))
    #print(validator(Aws_input_example,AWS))
    q=ValidationService.valid(AZURE,Azure_input_example)
    print(q)
