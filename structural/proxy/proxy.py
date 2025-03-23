class RealImage:
    def __init__(self,filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"📷 Loading image: {self.filename}")

    def display(self):
        print(f"📸 Displaying image: {self.filename}")

class ProxyImage:
    def __init__(self,filename):
        self.filename = filename
        self.real_imahe = None
    def display(self):
        if self.real_imahe == None:
            self.real_imahe = RealImage(self.filename);
        self.real_imahe.display()


image1 = ProxyImage("real.txt")
image2 = ProxyImage("hhdhd.txt")

image1.display()
image2.display()
image2.display()
