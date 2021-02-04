import adatok
import numpy as np
import torch
import random


def attack(images, labels):
    if not adatok.data.attackers[adatok.data.actual_user]:
        return images, labels

    if adatok.data.miss_labeling[adatok.data.actual_user] != 0:
        labels_array = np.array(labels)
        for i in range(len(labels_array)):
            if random.randint(0, 100) < adatok.data.miss_labeling[adatok.data.actual_user]:
                labels_array[i] = random_label(labels_array[i])
        labels = torch.from_numpy(labels_array)


    if adatok.data.noise[adatok.data.actual_user] != 0:
        images_array = np.array(images)
        for i in images_array:
            for j in i[0]:
                if random.randint(0, 100) < adatok.data.noise[adatok.data.actual_user]:
                    for k in range(len(j)):
                        j[k]=random.random()
        images=torch.from_numpy(images_array)



    return images, labels


def random_label(label):
    while True:
        a = random.randint(0, 9)
        if a != label:
            return a
