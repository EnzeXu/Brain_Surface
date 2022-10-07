import numpy as np


def build_txt(array, save_path):
    n = len(array)
    array = np.asarray(array).reshape(n)
    with open(save_path, "w") as f:
        for i in range(n):
            f.write("{}\n".format(array[i]))

def build_vtk():
    pass

if __name__ == "__main__":
    print("hello world!")
    a = np.random.rand(148)
    build_txt(a, "data/test.txt")