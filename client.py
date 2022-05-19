
from pysocket import PySocketClient

host = "ip"
port = "port"

ps = PySocketClient(host, port)

ps.connect()