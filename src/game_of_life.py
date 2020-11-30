'''
Conway's Game of Life
'''
import numpy as np
from scipy.signal import convolve2d
import cv2

TITLE = "Conway's Game of Life (Press Esc to exit)"
GRID_SIZE = 64, 128
MULTIPLIER = 8
DELAY = 1000 // 30

def main():
    ary = np.random.randint(0, 2, size=GRID_SIZE).astype(np.float)
    kernal = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    ary_last = ary_last2 = ary
    new_size = tuple([x*MULTIPLIER for x in ary.shape[::-1]])

    while cv2.waitKey(DELAY) != 27:
        img = (ary > 0.5).astype(np.uint8) * 255
        img = cv2.resize(img, new_size, interpolation=cv2.INTER_NEAREST)
        cv2.imshow(TITLE, img)
        ary_last, ary_last2 = ary, ary_last
        cnv = convolve2d(ary, kernal, mode='same', boundary='wrap')
        ary = ((cnv == 3) + (ary > 0.5) * (cnv == 2)).astype(np.float)
        if np.array_equal(ary, ary_last2): # repeating pattern
            cv2.waitKey(2000)
            ary = np.random.randint(0, 2, size=GRID_SIZE).astype(np.float)
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
