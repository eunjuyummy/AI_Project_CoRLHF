import gymnasium as gym
import numpy as np
from gymnasium.wrappers import RecordVideo
from base64 import b64encode
from IPython.display import display, HTML
from collections import deque
from typing import Dict
import moviepy.editor as mpy
import matplotlib.pyplot as plt
from stable_baselines3 import DDPG

# make env
train_env = gym.make('AdroitHandPenSparse-v1')

# training DDPG
model = DDPG("MlpPolicy", train_env)
model.learn(total_timesteps=int(1e6), progress_bar=True)
model.save("DDPG_pen_model_trained")

# make test env
test_env = gym.make('AdroitHandPenSparse-v1', render_mode="rgb_array")
test_env = RecordVideo(test_env, "results_video", episode_trigger=lambda e: True)

# load model
trained_model = DDPG.load("DDPG_pen_model_trained")

# test
observation, info = test_env.reset()
while True:
    action, _states = trained_model.predict(observation)
    observation, reward, terminated, truncated, info = test_env.step(action)
    if terminated:
        break
test_env.close()

# 녹화된 비디오 파일 읽고 base64로 변환
video_file = "results_video/rl-video-episode-0.mp4"
with open(video_file, "rb") as video:
    mp4 = video.read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
# HTML을 사용하여 비디오 표시
display(HTML(f"""
<video controls style='margin: auto; display: block'>
    <source src='{data_url}' type='video/mp4'>
</video>
"""))
