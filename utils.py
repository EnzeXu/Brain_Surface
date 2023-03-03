import numpy as np


def build_txt(array, save_path):
    n = len(array)
    array = np.asarray(array).reshape(n)
    with open(save_path, "w") as f:
        for i in range(n):
            f.write("{}\n".format(array[i]))

# def one_time_build():
#     for method in ["method1", "method2"]:
#         for part in ["CN", "MCI", "AD"]:
#             node_list = np.load("data/class/node_class_{}_{}.npy".format(method, part))
#             build_txt(node_list, "data/{}_{}.txt".format(method, part))


if __name__ == "__main__":
    pass

