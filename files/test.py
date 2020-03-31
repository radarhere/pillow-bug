from PIL import Image, ImageDraw, ImageFont, features

print(features.check('raqm'))
print(Image.__version__)

img = Image.new('RGB', (800, 300), color = (73, 109, 137))
d = ImageDraw.Draw(img)
fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf', 24, layout_engine=ImageFont.LAYOUT_BASIC)
d.text((10, 10), "༄༅། །སྒྲུབ།", font=fnt, fill=(255, 255, 0))
img.save('result.png')
fnt = ImageFont.truetype('NotoSansTibetan-Regular.ttf', 24, layout_engine=ImageFont.LAYOUT_RAQM)
print("things work until...")
res = fnt.getmask("༄༅། །སྒྲུབ།", features=['ccmp', 'abvs', 'blws', 'calt', 'liga', 'kern', 'abvm', 'blwm', 'mkmk'])