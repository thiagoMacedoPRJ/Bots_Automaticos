from simple_image_download import simple_image_download as simp

im = input('Digite a imagem que Deseja Baixar: ')
qt = int(input('Quantas imagens semelhantes? '))

response = simp.simple_image_download

response().download(im, qt)

print(response().urls(im, qt))