from captcha.image import ImageCaptcha

image = ImageCaptcha()

data=image.generate('12345')
image.write('12345', '1.png')

