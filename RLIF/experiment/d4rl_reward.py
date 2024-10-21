import numpy as np
import gym
import d4rl
import pandas as pd
import matplotlib.pyplot as plt

# 보상 계산 함수
def calculate_episode_rewards(env_name):
    env = gym.make(env_name)
    dataset = env.get_dataset()
    rewards = dataset['rewards']
    terminals = dataset['terminals']
    timeouts = dataset['timeouts']
    episode_rewards = []
    current_reward = 0.0
    for reward, done, timeout in zip(rewards, terminals, timeouts):
        current_reward += reward
        if done or timeout:
            episode_rewards.append(current_reward)
            current_reward = 0.0
    return np.array(episode_rewards)

# 데이터셋 리스트
datasets = {
    'Medium': 'hopper-medium-v2',
    'Expert': 'hopper-expert-v2',
    'Random': 'hopper-random-v2',
    'Medium Replay': 'hopper-medium-replay-v2',
    'Medium Expert': 'hopper-medium-expert-v2'
}

# 각 데이터셋에서 보상 계산
reward_data = {}
for name, env_name in datasets.items():
    episode_rewards = calculate_episode_rewards(env_name)
    reward_data[name] = {
        'Episode Rewards': episode_rewards,
        'Mean Reward': np.mean(episode_rewards),
        'Min Reward': np.min(episode_rewards),
        'Max Reward': np.max(episode_rewards),
        'Median Reward': np.median(episode_rewards),
        'Num Episodes': len(episode_rewards)
    }

# 데이터프레임으로 변환
df_rewards = pd.DataFrame({name: {
    'Mean Reward': reward_data[name]['Mean Reward'],
    'Min Reward': reward_data[name]['Min Reward'],
    'Max Reward': reward_data[name]['Max Reward'],
    'Median Reward': reward_data[name]['Median Reward'],
    'Num Episodes': reward_data[name]['Num Episodes']
} for name in reward_data}).T
df_rewards.index.name = 'Dataset'

# 결과 출력
print(df_rewards)

# 5개의 데이터셋에 대한 보상 분포 시각화
plt.figure(figsize=(10, 6))

# 각 데이터셋의 히스토그램을 다른 색으로 출력
colors = ['yellowgreen', '#5387DD', 'orange', 'purple', 'red']
for i, (name, data) in enumerate(reward_data.items()):
    plt.hist(data['Episode Rewards'], bins=20, edgecolor='k', alpha=0.7, label=name, color=colors[i])

# 그래프 제목과 축 레이블 설정
plt.title('Episode Reward Distribution: All Datasets', fontsize=24)
plt.xlabel('Episode Reward', fontsize=20)
plt.ylabel('Frequency', fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.legend(fontsize=18)
plt.tight_layout()

# 히스토그램 이미지 저장
plt.savefig('Fig_2_Distribution_of_all_datasets_episode_reward.png')

# 데이터프레임을 CSV로 저장
df_rewards.to_csv('hopper_reward_statistics.csv', index=True)

