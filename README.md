# CoRLHF: RLHF기반 로봇 팔 제어 프로그램 개발

## 프로젝트의 배경
다품종 소량생산을 지향하는 스마트 팩토리에서는 다양한 유형의 생산 라인을 효율적으로 관리하는 것이 필수적이다. 이러한 환경에서는 다양한 작업을 위해 로봇의 제어 프로그램을 일일이 설정하는 것은 비효율적이다. 이 문제에 대한 해결책으로 강화학습 기반의 자율 제어 프로그래밍이 제안되고 있습니다. 하지만 이 방식을 적용할 때 매 작업에 특화된 보상 함수를 새로 설계해야 한다는 문제가 발생한다.

본 프로젝트에서는 RLHF를 통해 이 문제를 해결하고자 한다.

RLIF: Interactive Imitation Learning as Reinforcement Learning (Anchor)
RLIF는 인간의 피드백을 Policy를 update하는 방식
보상함수를 설계없이 학습 가능 
인간의 피드백을 받을 수 없는 작업에서 사용할 수 없음


RLHF: Reinforcement Learning with Human Feedback
RLHF는 인간의 피드백을 받아 보상함수를 fine-tuning하는 방식
보상함수를 설계없이 학습 가능 
보상함수를 특정하기 어려운 환경에서 Anchor에 비해 더 유리할 것이라 예상

