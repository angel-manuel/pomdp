"""
POMDP models

This module defines MDP and POMDP models
"""

from __future__ import annotations

from typing import List, Optional, Tuple, Dict, Mapping


class Action:
    @staticmethod
    def from_object(state: State, obj: Dict) -> Action:
        name = obj['name']
        reward = float(obj['reward'])

        raw_trans = obj['transition']
        transitions = [tuple(tx) for tx in raw_trans]

        return Action(name=name, state=state, reward=reward, transitions=transitions)

    def __init__(self, name: str, state: 'State', reward: float, transitions: List[Tuple[float, 'State']]):
        self._name = name
        self._state = state
        self._reward = reward
        self._transitions = transitions

    @property
    def name(self) -> str:
        return self._name

    @property
    def full_name(self) -> str:
        return self._state.name + ' ' + self._name

    @property
    def state(self) -> 'State':
        return self._state

    @property
    def reward(self) -> str:
        return self._reward

    @property
    def transitions(self) -> List[Tuple[float, 'State']]:
        return self._transitions


class State:
    _actions: Mapping[str, Action] = {}

    @staticmethod
    def from_object(obj: Dict) -> State:
        name = obj['name']
        return State(name)

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def actions(self) -> List[Action]:
        return self._actions.values()

    def get_action(self, action_name: str):
        return self._actions[action_name]

    def add_action(self, action: Action):
        self._actions[action.name] = action


class MDP:
    _states: Mapping['str', State] = {}

    @staticmethod
    def from_object(obj: Dict) -> MDP:
        name = obj.get('name', 'unnamed')

        mdp = MDP(name)

        states = obj['states']

        for state_obj in states:
            state = State.from_object(state_obj)
            mdp.add_state(state)

        for state_obj in states:
            state = mdp.get_state(state_obj['name'])
            for action_obj in state_obj['actions']:
                action = Action.from_object(state, action_obj)
                state.add_action(action)

        return mdp

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def states(self) -> List[State]:
        return self._states.values()

    def get_state(self, state_name: str) -> State:
        return self._states[state_name]

    def add_state(self, state: State):
        self._states[state.name] = state


class POMDP:
    pass
