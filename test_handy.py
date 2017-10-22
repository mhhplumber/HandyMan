from flask import *
from urllib.request import urlopen



def main():
    print(urlopen("127.0.0.1:5000/create_new_task", data=jsonify(name='haylee')))
          

main();

