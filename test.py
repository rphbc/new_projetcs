from PIL import Image

img = Image.open('Frotrografia.png')
img = img.convert('RGBA')

pixdata = img.load()
pixdatabin = []

input = input("Escreve texto a ser escondido : ")
input = [bin(ord(x))[2:] for x in input]
print(input)


for x in range(img.size[0]):  # img.size[0]
    for y in range(img.size[1]):  # img.size[1]
        px = [bin(pixdata[x, y][0]), bin(pixdata[x, y][1]), bin(pixdata[x, y][2]), bin(pixdata[x, y][3])]
        pixdatabin.append(px)

# print("original: ", pixdatabin)

count = 0
for item in input:
    for c in item:
        pixdatabin[count][-1] = pixdatabin[count][-1][:-1] + c
        count += 1

# print("novo: ", pixdatabin)

pixdataint = []
for item in pixdatabin:
    px = (int(item[0], 2), int(item[1], 2), int(item[2], 2), int(item[3], 2))
    pixdataint.append(px)

# print(pixdataint)

im2 = Image.new(img.mode, (img.size[0], img.size[1]))
imgsave = tuple(pixdataint)
im2.putdata(imgsave)

im2.save('test.png')

#  #########################################################################################

img_rec = Image.open('test.png')
img_rec = img_rec.convert('RGBA')

pixrec_data = img_rec.load()

# print(pixrec_data, img_rec.size)

message = []

for y in range(img_rec.size[1]):
    for x in range(img_rec.size[0]):
        message.append(pixrec_data[x, y][3])

# print(message)

secret_bin = ['0b',]

for item in message:
    if item == 255:
        secret_bin.append(str(1))
    else:
        secret_bin.append(str(0))

secret_bin = ''.join(secret_bin)[:9]

print("texto secreto: ", chr(int(secret_bin, 2)))

