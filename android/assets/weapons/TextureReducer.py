from PIL import Image

recom = True
while recom:
   
    while True:
        nom = input("Nom du fichier ?")
        imageBase = Image.open(nom)
        imagePixBase = imageBase.load()
        imageEnd = Image.new('RGBA', (int(imageBase.size[0]/2),int(imageBase.size[1]/2)))
        imagePixEnd = imageEnd.load()
        for i in range(0,imageEnd.size[0]):
            for j in range(0,imageEnd.size[1]):
                imagePixEnd[i,j] = imagePixBase[i*2,j*2]
                
        imageEnd.save(nom)
        """       
        pixelsTileB.append(tileBase[i].load())
        tile.append(Image.new('RGBA', (10,10)))
        tile[i].paste(tileBase[i], (1, 1))

        pixelsTile = tile[i].load()
        for i in range(8):
            pixelsTile[i+1,9] = pixelsTile[i+1,8]
            pixelsTile[i+1,0] = pixelsTile[i+1,1]
        for i in range(10):
            pixelsTile[9,i] = pixelsTile[8,i]
            pixelsTile[0,i] = pixelsTile[1,i]

    im = Image.new('RGBA', template.size)
    for i in range(int(im.size[0]/10)):
        for j in range(int(im.size[1]/10)):
            im.paste(tile[i%nf], (i*10,j*10))

    pixels = im.load()
    pixelsTemplate = template.load()

    couleur = (0,0,0,0)
    coul = int(input("Couleur des contours (1 = automatique, 2 = manuel, 3 = noir): "))
    if coul == 3: couleur = (0,0,0,255)
    elif coul != 1: couleur = (int(input("rouge (0-255) ")), int(input("vert (0-255) ")), int(input("bleu (0-255) ")), int(input("alpha (0-255): ")))
    else:
        moyenne = pixelsTileB[0][0,0]
        for i in range(8):
            for j in range(8):
                if i != 0 or j != 0:
                    moyenne = (moyenne[0]+pixelsTileB[0][i,j][0], moyenne[1]+pixelsTileB[0][i,j][1], moyenne[2]+pixelsTileB[0][i,j][2])
        couleur = (int(moyenne[0]/150), int(moyenne[1]/150), int(moyenne[2]/150))

    for i in range(template.size[0]):
        for j in range(template.size[1]):
            if pixelsTemplate[i,j][2] == 0 and pixelsTemplate[i,j][1] == 0 and pixelsTemplate[i,j][0] == 0 and pixelsTemplate[i,j][3] >0:
                pixelsTemplate[i,j] = couleur
            if pixelsTemplate[i,j][3] > 0:
                pixels[i,j] = pixelsTemplate[i,j]

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if pixels[i,j][0] == 0 and pixels[i,j][1] == 255 and pixels[i,j][2] == 0:
                pixels[i,j] = (0,0,0,0)

    nom = input("Sauvegarder sous quel nom? (sous la forme nom.png): ")
    im.save(nom)
    recom = int(input("Recommencer? (1 = oui, 2 = non): ")) == 1"""

