import gym

from griddly import GymWrapperFactory
from griddly.RenderTools import RenderToFile

if __name__ == '__main__':
    # A nice tool to save png images
    file_renderer = RenderToFile()

    # This is what to use if you want to use OpenAI gym environments
    wrapper = GymWrapperFactory()

    # There are two levels here
    level = 0
    wrapper.build_gym_from_yaml('GameOfLife', 'game-of-life.yaml', level=level)

    # Create the Environment
    env = gym.make(f'GDY-GameOfLife-v0')
    observation = env.reset()

    file_renderer.render(observation, f'sokoban-level-{level}.png')