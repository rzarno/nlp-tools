from src.socket_handler import SocketHandler
from src.sentence_splitter.sentence_splitter import SentenceSplitter
from src.nlp.text_processor import TextProcessor

socketHandler = SocketHandler('127.0.0.1', 64647)

while True:
    socketHandler.s_accept()
    request = socketHandler.read_data()
    action, data = request.decode().split('::')
    if action == 'sentence-split':
        sentenceSplitter = SentenceSplitter()
        resp = sentenceSplitter.split(data)
    elif action == 'normalize':
        resp = TextProcessor().normalize(data)
    else:
        continue

    socketHandler.send_data(resp)
    socketHandler.close_socket()
