import os
import time
import cv2
from tqdm import tqdm

movie_path = '[動画ファイルパス]'


def save_frame_range(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    digit = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    start = time.perf_counter()
    for i in tqdm(range(digit)):
        ret, frame = cap.read()
    end = time.perf_counter()

    print(f'cap.read 実行時間: {end - start}')

    start = time.perf_counter()
    for i in tqdm(range(digit)):
        ret = cap.grab()
    end = time.perf_counter()

    print(f'cap.grab 実行時間: {end - start}')


if __name__=='__main__':
    save_frame_range(movie_path)
