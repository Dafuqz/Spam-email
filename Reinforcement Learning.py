from simple_rl.agents import Agent, RandomAgent
from simple_rl.tasks import ChainMDP
from simple_rl.run_experiments import run_agents_on_mdp
import random
from collections import defaultdict

class NewAgent(Agent):

	def __init__(self, name, actions, gamma=0.99):
		Agent.__init__(self, name, actions, gamma)
		self.reward_history = defaultdict(dict)
		self.prev_state = None
		self.prev_action = ""

	def act(self, state, reward):
		'''
		Args:
			state (State)
			reward (float)

		Returns:
			(str): Represents an action.
		'''

		# This function is called every time step for the agent to:
			# Get rewarded for previous action
			# See the new state.
			# Take a new action.

		# Store previous reward.
		if not self.prev_action in self.reward_history[self.prev_state].keys():
			self.reward_history[self.prev_state][self.prev_action] = reward

		# Choose new action.
		next_action = self.choose_action(state)

		# Update previous state/action pointers.
		self.prev_action = next_action
		self.prev_state = state

		return next_action

	def choose_action(self, state):
		'''
		Args:
			(state)

		Returns:
			(str): Action
		'''
		######################
		### YOUR CODE HERE ###
		######################
		action = random.choice(self.actions)

		return action


# Makes the cell game with 5 cells.
environment = ChainMDP(5)
actions = environment.get_actions()

my_agent = NewAgent("ais-agent", actions)
random_agent = RandomAgent(actions)

list_of_agents = [my_agent, random_agent]

run_agents_on_mdp(list_of_agents, environment)