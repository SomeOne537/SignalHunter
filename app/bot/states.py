from enum import Enum


class UserState(Enum):
    IDLE = "idle"
    SELECT_PAIR = "select_pair"
    SELECT_TIMEFRAME = "select_timeframe"
