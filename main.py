import qrcode
from PIL import Image, ImageDraw, ImageFont
import json
from init_creds import init_mongo

db = init_mongo()
for club in db.club.find({"asociacion": "SportClub"}):
    input_data = json.dumps({
            "prestador": club["slug"],
            "funcion": "acceso_simple"
    })

    #Creating an instance of qrcode
    qr = qrcode.QRCode(
            version=1,
            box_size=38,
            border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    pix = img.pixel_size

    h = (2480 - pix) // 2
    v = (3508 - pix) // 2
    font = ImageFont.truetype("font2.otf", 180)
    name = club["name"].replace("SportClub ", "").replace("Familia ","")
    with Image.open("A4.FINAL.jpg") as background:
        background.paste(img, (h, v))
        d = ImageDraw.Draw(background)
        ht, vt = d.textsize(name, font=font)
        print(ht)
        d.text(((2480 - ht) // 2, 3000), name, fill=(255, 255, 255), font=font)

        background.save(f'QRfinales/{club["slug"]}.png')






