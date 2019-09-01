# Anyserv
Get a full (GET request as of now) fake REST API with zero coding

#### Installation

        $ git clone https://github.com/rrajaravi/anyserv.git
        $ cd anyserv
        $ python setup.py install

#### Command Line

        $ anyserv -f example/config.json --host 127.0.0.1 -p 5001
         * Running on http://127.0.0.1:5001/ (Press CTRL+C to quit)

        $ anyserv -f example/config.json 
         * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
         
        $ anyserv --help
        usage: anyserv [-h] -f FILE [--host HOST] [-p PORT]

        Serve any static data by providing json file as an input. Refer config.json
        available in github repository example directory for the file format

        optional arguments:
          -h, --help            show this help message and exit
          -f FILE, --file FILE
          --host HOST
          -p PORT, --port PORT         
         
#### Sample Config File

		[  
		   {  
		      "name":"hello",
		      "path":"/",
		      "method": "GET",
		      "response":"hello world!"
		   },
		   {  
		      "name":"myapi",
		      "path":"/api",
		      "method": "GET",
		      "response":{  
		         "version":1,
		         "status":"api working"
		      }
		   },
		   {  
		      "name":"myapiusers",
		      "path":"/api/users",
		      "method": "GET",
		      "response":[  
		         "john",
		         "david",
		         "peter"
		      ]
		   }
		]
## License
MIT
