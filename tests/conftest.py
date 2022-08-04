import shutil
import sys
from os.path import abspath, dirname

import pytest

root_dir = dirname(dirname(abspath(__file__)))
sys.path.append(root_dir)


# pytest_plugins = [
#     'tests.fixtures.fixture_data',
#     'tests.fixtures.fixture_msg',
# ]

@pytest.fixture(autouse=True)
def copy_constants_file_to_test():
    shutil.copy(f'{root_dir}/src/cloudtipsadp/constants.py',
                f'{root_dir}/tests/constants_file.py')
