import json
import argparse

from flask import Flask
from flask import jsonify
from schema import Schema, And, Or, SchemaUnexpectedTypeError, SchemaError

app = Flask(__name__)

schema = Schema([{'name' : And(str, len), 'path': And(str), 'response': Or(str,list,dict,int,bool)}])


def formatter(data):
    if isinstance(data, str):
        return data
        
    return jsonify(data)

def gen_func(data):
    def inner():
        return formatter(data)
    return inner
    
def add_app(dct):
    name, path, data = dct['name'], dct['path'], dct['response']
    app.add_url_rule(path, name, gen_func(data))

def register(jsonData):
    data = jsonData
    for view in data:
        add_app(view)
    
def run(**kwargs):
    app.run(**kwargs)
    
class StoreJson(argparse.Action):
    def __init__(self,
                 option_strings,
                 dest,
                 nargs=None,
                 const=None,
                 default=None,
                 type=None,
                 choices=None,
                 required=False,
                 help=None,
                 metavar=None):
        argparse.Action.__init__(self,
                                 option_strings=option_strings,
                                 dest=dest,
                                 nargs=nargs,
                                 const=const,
                                 default=default,
                                 type=type,
                                 choices=choices,
                                 required=required,
                                 help=help,
                                 metavar=metavar,
                                 )
        return

    def __call__(self, parser, namespace, values,
                 option_string=None):
        # Do some arbitrary processing of the input values
        with open(values, 'r') as f:
            try:
                data = json.load(f)
                schema.validate(data)
            except (SchemaUnexpectedTypeError, SchemaError) as e:
                print(e)
                raise SchemaError("Incompaible JSON data format: " + str(values))
            except Exception:
                raise argparse.ArgumentTypeError("Not a valid json file: " + str(values))
                
        # Save the results in the namespace using the destination
        # variable given to our constructor.
        setattr(namespace, self.dest, data)
