import requests
import pickle
x = requests.get("http://www.pythonchallenge.com/pc/def/banner.p").text
l = pickle.loads(bytes(x, 'utf-8'))
print('\n'.join(''.join(c*n for c,n in a) for a in l))
