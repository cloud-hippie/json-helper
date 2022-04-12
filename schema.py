import json

SCHEMA =  {
        "name": "",
        "description": "",
        "version": "",
        "author": "",
        "license": "",
        "posts": [
            {
                "title": "",
                "date": "",
                "content": ""
            }
        ]
    }

class SchemaFile:

    def __init__(self, output_file, value=SCHEMA):
        self.value = value
        self.output_file = output_file
    
    def set_values(self, input_values):
        """
        Sets the input values to the ones within the Schema
        """
        with open(self.output_file, "w") as file_name:
            file_name.write(json.dumps(input_values))

