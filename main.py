import imgurpython
import urllib
import requests
import os

# escape file name 
# if title throws error, append to "unknwon_title_" the id which is the last element in the string
def escape(name):
    response = "unknown_title_"
    try:
        response = "".join([c for c in str(name) if c.isalpha() or c.isdigit() or c == ' ']).rstrip()
    except:
        for c in reversed(name):
            if c != "_":
                response = response + c
                break
    return response

# download one image
# imgur give access to various formats e.g. png, jpg, so you can change it to your favorite format
def download_image(img, path):
    if img.get("type"):
        if img["type"] == "image/gif" and img["size"] <= 2097152:
            if os.path.exists(path + ".gif") == False:
                urllib.urlretrieve(img["link"], path + ".gif")
        elif img["type"] == "image/gif" and img["size"] > 2097152:
            if os.path.exists(path + ".mp4") == False:
                urllib.urlretrieve(img["mp4"], path + ".mp4")
        else:
            if os.path.exists(path + ".png") == False:
                urllib.urlretrieve(img["link"] + ".png", path + ".png")


if __name__ == "__main__":
    print("You have to register a new app on api.imgur.com to get a client id and secret")
    client_id = str(input("Client id: "))
    client_secret = str(input("Client secret: "))
    username = str(input("Your username: "))
    client = imgurpython.ImgurClient(client_id, client_secret)

    # Authorization url, where you get a pin to get access to your profile
    authorization_url = client.get_auth_url('pin')

    # ... redirect user to `authorization_url`, obtain pin 
    print("Please go here and copy the pin: " + authorization_url)
    pin = str(input('Paste the PIN:'))

    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])

    # cannot get all favorites without the page parameter, so i have to iterate through the pages 
    # maybe a bug
    for page in range(0, 100):
        res = requests.get("https://api.imgur.com/3/account/" + username + "/favorites/" + str(page),
                           headers={'Authorization': 'Bearer %s' % client.auth.get_current_access_token()})
        imgs = res.json()

        # problem with client.get_account_favorites(username) -> not getting all favorites
        # maybe a bug
        for index, img in enumerate(imgs["data"]):
            if img["is_album"] == False:
                print("Loading image" + str(index) + " from " + str(len(imgs["data"])))

                path = os.path.dirname(os.path.abspath(__file__)) + "\\images\\" + escape(img["title"]) + "_" + str(
                    img["id"])
                    
                download_image(img, path)
            else:
                print("Loading album" + str(index) + " from " + str(len(imgs["data"])))

                album = img
                res = requests.get("https://api.imgur.com/3/album/" + img["id"] + "/images",
                                   headers={'Authorization': 'Bearer %s' % client.auth.get_current_access_token()})
                imgs = res.json()

                album_path = os.path.dirname(os.path.abspath(__file__)) + "\\images\\" + escape(album["title"])
                
                if not os.path.exists(album_path):
                    os.makedirs(album_path)

                for img in imgs["data"]:
                    img_path = album_path + "\\" + str(img["id"])
                    download_image(img, img_path)
