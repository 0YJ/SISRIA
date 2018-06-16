

'''this is file contain functions of plotting things '''


import matplotlib.pyplot as plt
from scipy.misc import imresize

def plot_comparison(O_image, down_image):
    O_size = O_image.shape
    plt.subplot(2,3,1)
    plt.imshow(O_image,cmap='gray')
    plt.title('original size')

    plt.subplot(2,3,2)
    imrecov = imresize(down_image,size=O_size,interp='nearest')
    plt.imshow(imrecov,cmap='gray')
    plt.title('nearest ')

    plt.subplot(2,3,3)
    imrecov = imresize(down_image,size=O_size,interp='lanczos')
    plt.imshow(imrecov,cmap='gray')
    plt.title('lanczos ')

    plt.subplot(2,3,4)
    imrecov = imresize(down_image,size=O_size,interp='bilinear')
    plt.imshow(imrecov,cmap='gray')
    plt.title('bilinear ')

    plt.subplot(2,3,5)
    imrecov = imresize(down_image,size=O_size,interp='cubic')
    plt.imshow(imrecov,cmap='gray')
    plt.title('cubic ')


    plt.subplot(2,3,6)
    imrecov = imresize(down_image,size=O_size,interp='bicubic')
    plt.imshow(imrecov,cmap='gray')
    plt.title('bicubic ')

    plt.show()


def plot_2(original,SR):
    plt.subplot(211)
    plt.title('original')
    plt.imshow(original)
    plt.subplot(212)
    plt.title('SR')
    plt.imshow(SR)
    plt.show()

def norm(imrecov):
    imrecov[imrecov>255]=255
    imrecov[imrecov<0]=0
    return imrecov
    
    

def plot_3(O_image,down_image,SR,index):
    O_size = O_image.shape
    plt.subplot(2,3,1)
    plt.xticks([])
    plt.imshow(O_image,cmap='gray')
    plt.title('Original Image')

    plt.subplot(2,3,6)
    
    imrecov = imresize(down_image,size=O_size,interp='nearest')
    imrecov =norm(imrecov)
    plt.imshow(imrecov,cmap='gray')
    plt.xticks([])
    plt.title('Nearest ')

    plt.subplot(2,3,3)
    imrecov = imresize(down_image,size=O_size,interp='lanczos')
    imrecov =norm(imrecov)
    plt.imshow(imrecov,cmap='gray')
    plt.title('Lanczos ')
    plt.xticks([])
    
    plt.subplot(2,3,4)
    imrecov = imresize(down_image,size=O_size,interp='bilinear')
    imrecov =norm(imrecov)
    plt.imshow(imrecov,cmap='gray')
    plt.title('Bilinear ')
    plt.xticks([])
    
    plt.subplot(2,3,5)
    imrecov = imresize(down_image,size=O_size,interp='bicubic')
    imrecov =norm(imrecov)
    plt.imshow(imrecov,cmap='gray')
    plt.title('Bicubic ')
    plt.xticks([])

    plt.subplot(2,3,2)
    plt.imshow(SR,cmap='gray')
    plt.title('SRCNN')
    plt.xticks([])
    
    plt.savefig('OMNIGLOT-outcome-comp_'+str(index))
    plt.show()
    return plt