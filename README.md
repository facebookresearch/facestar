# Facestar Dataset
[![teaser](https://github.com/facebookresearch/facestar/blob/main/teaser.jpg)](https://github.com/facebookresearch/facestar/)

## Description

Existing audio-visual dataset for human speech are either captured in a clean, controlled environment but contain only a small amount of speech data without natural conversations, or are collected *in-the-wild* with unreliable audio quality, interfering sounds, low face resolution, and unreliable or occluded lip motion.

The **Facestar dataset** aims to enable research on audio-visual modeling in a large-scale and high-quality setting. Core dataset features:
* 10 hours of high-quality audio-visual speech data
* audio recordings in a quiet environment at 16kHz
* video of resolution 1300 x 1600 at 60 frames per second
* one female and one male speaker
* natural speech: all data is conversational speech in a video-conferencing setup
* full face visibility: speakers are facing the camera while talking

See the [paper](https://github.com/facebookresearch/facestar/) for more details. If you use the dataset, please cite
```
@inproceedings{yang2022audiovisual,
  title={Audio-Visual Speech Codecs: Rethinking Audio-Visual Speech Enhancement by Re-Synthesis},
  author={Yang, Karren and Markovic, Dejan and Richard, Alexander and Krenn, Steven and Agrawal, Vasu},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2022}
}
```

## Download

The dataset is partitioned into a trainset and a testset for each speaker. Within each partition, there are several sessions, each of which is further subdivided into cuts of about 30 seconds.
For each session, the videos are provided without sound as `sessionXX_cutYY.mp4` and the corresponding audio is provided in the wave file `sessionXX_cutYY.wav`.

### Automatic Download

The `download.py` script automatically downloads the complete dataset and unzips the sessions. Needs to be run with python3. The complete dataset is about 30GB in size.

### Manual Download

If you do not need the full dataset but only selected sessions, you can download them manually:
* [female speaker trainset](https://github.com/facebookresearch/facestar/releases/tag/female_speaker_trainset) (55 sessions)
* [female speaker testset](https://github.com/facebookresearch/facestar/releases/tag/female_speaker_testset) (7 sessions)
* [male speaker trainset](https://github.com/facebookresearch/facestar/releases/tag/male_speaker_trainset) (45 sessions)
* [male speaker testset](https://github.com/facebookresearch/facestar/releases/tag/male_speaker_testset) (5 sessions)

## License

The code and dataset are released under [CC-NC 4.0 International license](https://github.com/facebookresearch/facestar/blob/main/LICENSE).

