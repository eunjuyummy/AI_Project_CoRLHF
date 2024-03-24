# CoRLHF: RLHF기반 로봇 팔 제어 프로그램 개발

다품종 유연생산 스마트팩토리
작업 마다 매번 로봇 제어 프로그래밍을 하는 것은 비효율적
강화학습을 통한 자율 제어 프로그래밍 적용
작업 마다 새로 보상함수 설계해야하는 문제 발생

강화학습 방식의 한계 
Real-World에서 특정 모델에 대한 보상 함수를 구하는 것은 매우 복잡한 문제
Develop algorithms which can learn from unshaped reward


RLIF: Interactive Imitation Learning as Reinforcement Learning
RLIF는 인간의 피드백을 Policy를 update하는 방식
보상함수를 설계없이 학습 가능 
인간의 피드백을 받을 수 없는 작업에서 사용할 수 없음


RLHF: Reinforcement Learning with Human Feedback
RLHF는 인간의 피드백을 받아 보상함수를 fine-tuning하는 방식
보상함수를 설계없이 학습 가능 
보상함수를 특정하기 어려운 환경에서 Anchor에 비해 더 유리할 것이라 예상

