class ImageBase64:
    def __init__(self, src):
        info = src.split(';')[0]
        self.extension = info.split('/')[1]
        str_data = src.split('base64')[1]
        self.data = str.encode(str_data)