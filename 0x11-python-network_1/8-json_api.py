#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter """

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv[1]) <= 1:
        q = ""
    else:
        q = sys.argv[1]

    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get('id'), response.get('name')))
    except ValueError:
        print("Not a valid JSON")
