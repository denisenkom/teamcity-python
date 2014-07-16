# coding=utf-8
__all__ = ['is_running_under_teamcity']

import os

teamcity_determinant_env_variable = "TEAMCITY_VERSION"


def is_running_under_teamcity():
    return os.getenv(teamcity_determinant_env_variable) is not None
