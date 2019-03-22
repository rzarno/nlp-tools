Python server and client to run microservice for text normalization and sentence split.

It's based on python 3.7

Server and client communicate by socket connection.

Project is used for english natural language processing

to start server in main project dir run:
python server.py

to start client in main project dir run:
python client.py

example command:
"sentence-split::Her is some text to  split. Here is another sentence."
"normalize::Some text."

normalization contains:
- lemmatization
- remove stop words
- lowercase
- remove numeric
- remove punctuation
