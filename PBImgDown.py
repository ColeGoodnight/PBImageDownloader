import requests

while True:
    link = input("URL: ")
    if link == "done":
        break

    export = link.split('/')

    photoNum = None
    for i, part in enumerate(export):
        if (part == "photo"):
            if i + 1 < len(export):
                photoNum = export[i+1]
                break

    if photoNum == None:
        print("Invalid URL")
        continue

    if int(photoNum) < 1000000: 
        print("Invalid photoNum")
        continue

    photoURL = "http://lp1.pinkbike.org/p0pb" + photoNum + "/" + photoNum + ".jpeg"
    img_data = requests.get(photoURL).content
    with open(photoNum + ".jpg", "wb") as handler:
        handler.write(img_data)