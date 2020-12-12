"""
https://requests.readthedocs.io/en/master/user/quickstart/
"""
import requests
import json
import base64
import numpy as np
import threading

# pip install cryptography
import cryptography
# Used to Generate Keys
# from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

# Used to Store Keys and Read in Keys
from cryptography.hazmat.primitives import serialization

# Used to do Encryption
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_der_private_key
from cryptography.hazmat.primitives.serialization import load_der_public_key


TOKEN = 'e23a96ca37903c94a39b2a3792159e51'
UID = '5178600'
API = 'http://msubackend.xyz/api/?route='
USERS = {}
PUBKEYS = {}
SNAME = "Runtime Terror"
FNAME = "Semeion"
LNAME = "Stafford"
EMAIL = "BullyRanks@ghettoyute.com"


def loadPubKey(pubkey):
    return serialization.load_pem_public_key(pubkey)


def pubKey():
    global PUBKEYS
    route = 'getPubKey'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    try:
        keys = r.json()
    except ValueError as e:
        print("Invalid Json!!!")
        print(r.text)

    for key in keys['data']:
        PUBKEYS[key['uid']] = key


def getUsers():
    global USERS
    global PUBKEYS

    route = 'getUser'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    try:
        users = r.json()
    except ValueError as e:
        print("Invalid Json!!!")
        print(r.text)

    for user in users['data']:
        if user['uid'] in PUBKEYS:
            user['pubkey'] = PUBKEYS[user['uid']]['pubkey']
            USERS[user['uid']] = user


def getActive():
    route = 'getActive'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    active_users = r.json()
    active_users = active_users['data']

    real_active_users = []
    for active in active_users:
        active['fname'] = USERS[active['uid']]['fname']
        active['lname'] = USERS[active['uid']]['lname']
        active['email'] = USERS[active['uid']]['email']
        active['pubkey'] = PUBKEYS[active['uid']]
        real_active_users.append(active)

    return real_active_users


def postMessage(message, to_uid):
    route = 'postMessage'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"

    payload = {
        'uid': UID,
        'to_uid': to_uid,
        'message': message,
        'token': TOKEN
    }

    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, headers=headers, json=payload)
    return r.json()

def postUser():
    route = 'postUser'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"

    payload = {
        'fname': FNAME,
        'lname': LNAME,
        'screen_name': SNAME,
        'email': EMAIL,
        'token': TOKEN,
        'uid': UID
    }

    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, headers=headers, json=payload)
    return r.json()


"""
A: Basic Start Of Workflow: 
    - Generate your own public and private key
    - Post your public key at beginning of session
    - Download everyones public keys so you can encrypt messages.
B: Encrypting a message: 
    - load target users public key and encode it using .encode('utf-8') (turns it into bytes)
    - encrypt the message to them with a string (also encoded utf8)
    - Important! See code snippets below.
        - base64 encode the encrypted message (base64 uses characters that we can put into json or strings)
        - then using your base64 encoded string, decode it AGAIN using .decode('utf8')
    - now you send your message using api
C: Decrypting messages:
    - get the message using the api.
    - decode the message using base64 decode
    - decrypt message 
System As a Whole:
    - Do step A
    - Look at active users
    - Send one of them a message using step B
    - Continuously check for messages from other users
    - Find one, get it and decrypt it.
"""

def getMessages():
    # Get all the messages for my user
    route = 'getMessage'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    payload = {
        'token': TOKEN,
        'uid': UID
    }

def updateMessages():
    threading.Timer(5.0, updateMessages).start()
    getMessages()

def publishKey(pubkey):
    route = 'postPubKey'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"

    payload = {
        'pub_key': pubkey,
        'uid': UID,
        'token': TOKEN
    }
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, headers=headers, json=payload)
    return r.json()


if __name__ == '__main__':

    pubKey()
    getUsers()

    private_key = rsa.generate_private_key(public_exponent=65537,
                                          key_size=2048)

    public_key = private_key.public_key()
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    text_key = str(pem)

    pem.splitlines()[0]

    #Serialize key from bytes and publish to server
    #encoded = base64.b64encode(pem)
    #data = encoded.decode('ascii')

    publishKey(text_key)
    postUser()

    active = getActive()
    print("Active Users Online")
    print("###################")
    for users in range(len(active)):
        name = active[users]['fname']
        print("-", name)

    dicAlone = {}
    for k in USERS.items():
        dicAlone[k[1]['fname']] = [k[1]['uid']]


    #for user in USERS.items():
    #    print((user))

    print("\n========================================")
    print("MENU")
    print("========================================")
    print("1. Send Message")
    print("2. Check Messages\n")

    #action = input("Enter Option: ")
    action = "1"
    while action != "exit".casefold():

        if action == "1":
            send_to = input("Enter user's name: ").capitalize()

            msg = input("Type message: ")

            person = str(dicAlone[send_to])[2:-2]
            theirUID = person

            # Loading that users UID that you want to send to
            pk = loadPubKey(USERS[theirUID]['pubkey'].encode('utf-8'))

            # This encrypts the encoded plaintext message with a users public key
            encrypted = pk.encrypt(
                msg.encode('utf-8'),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            print("ENCRYPTED TEXT", encrypted)
            postMessage(encrypted, theirUID)

        if action == "1":

        print("\n\n++++++++++++++++++++")
        action = input("Enter Option")









    #result = postMessage("This is a plaintext message encrypted with public key 5147600",'5147600')

    # this is me loading a public key from my key dictionary
    #pk = loadPubKey(USERS['5147600']['pubkey'].encode('utf-8'))