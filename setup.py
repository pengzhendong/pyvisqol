# Copyright (c) 2024 Zhendong Peng (pzd17@tsinghua.org.cn)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup


with open("requirements.txt", encoding="utf8") as f:
    requirements = f.readlines()

setup(
    name="pyvisqol",
    version=open("VERSION", encoding="utf8").read(),
    url="https://github.com/pengzhendong/pyvisqol",
    description="An objective, full-reference metric for perceived audio quality.",
    entry_points={
        "console_scripts": [
            "pyvisqol = pyvisqol.cli:main",
        ]
    },
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
    ],
)
