"""
Copyright (c) Meta Platforms, Inc. and affiliates.
All rights reserved.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""


import os
import zipfile
import urllib.request


""" progress bar if tqdm is installed """
try:
    import tqdm
    has_tqdm = True
except:
    has_tqdm = False


class ProgressBar:
    def __init__(self, iterable, has_tqdm):
        self.has_tqdm = has_tqdm
        self.iterable = tqdm.tqdm(iterable) if has_tqdm else iterable

    def print(self, msg):
        if self.has_tqdm:
            self.iterable.set_description(msg)
        else:
            print(msg)


dataset = {
    "url": "https://github.com/facebookresearch/facestar/releases/download/",
    "male_speaker": {
        "trainset": range(1, 46),
        "testset": range(1, 6),
    },
    "female_speaker": {
        "trainset": range(1, 56),
        "testset": range(1, 8),
    }
}


""" iterate over subjects """
for speaker in ["male_speaker", "female_speaker"]:
    print(f"### Downloading {speaker} ###")

    """ iterate over partitions """
    for partition in ["testset", "trainset"]:
        print(f"    downloading {partition}...")

        """ iterate over sessions """
        pbar = ProgressBar(dataset[speaker][partition], has_tqdm)
        for idx in pbar.iterable:
            pbar.print(f"    session{idx:02d}")

            """ create target directory """
            os.makedirs(f"{speaker}/{partition}", exist_ok=True)

            """ download zip file"""
            with urllib.request.urlopen(f"{dataset['url']}/{speaker}_{partition}/session{idx:02d}.zip") as f:
                data = f.read()
            f.close()

            with open(f"{speaker}/{partition}/session{idx:02d}.zip", "wb") as g:
                g.write(data)
            g.close()

            """ unzip """
            with zipfile.ZipFile(f"{speaker}/{partition}/session{idx:02d}.zip", "r") as f:
                f.extractall(f"{speaker}/{partition}")
            f.close()

            """ clean up """
            os.remove(f"{speaker}/{partition}/session{idx:02d}.zip")

