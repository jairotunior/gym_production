from gym.envs.registration import register

register(
    id='FactoryEnv-v0',
    entry_point='gym_factory.envs:FactoryEnv',
)

"""
register(
    id='TradingEnv-v1',
    entry_point='gym_trading.envs:TradingEnv',
    kwargs = { 'use_settings': False }
)
"""