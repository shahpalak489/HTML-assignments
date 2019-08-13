import socket
import os

hostname = socket.gethostname()
# os.environ["ENVIRONMENT"] = ""
os.environ["DATABASE_SERVER"] = "LAPTOP-QDH3PMIF"
os.environ["DATABASE_NAME"] = "master"
os.environ["DATABASE_USER"] = ""
os.environ["DATABASE_PASSWORD"] = ""
