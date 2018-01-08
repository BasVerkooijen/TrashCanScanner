import requests

def productExists( stripecode ):
	r = requests.get('http://154.59.112.9:8000/products/' + str(stripecode) + "/")
	if r.status_code >= 400:
		return False
	elif r.status_code >= 200 and r.status_code < 300:
		return r.json()["name"]
	else:
		return False

def addToShoppingList( listid, stripecode , amount ):
	payload = {'add_product': str(stripecode), 'amount': amount}
	r = requests.patch("http://154.59.112.9:8000/lists/" + str(listid) + "/", data=payload)
	return
