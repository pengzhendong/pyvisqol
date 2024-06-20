# Copyright (c) 2024, Zhendong Peng (pzd17@tsinghua.org.cn)
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

import click

from pyvisqol import Visqol


@click.command()
@click.argument("reference", type=click.Path(exists=True, file_okay=True))
@click.argument("defraded", type=click.Path(exists=True, file_okay=True))
def main(reference, defraded):
    moslqo = Visqol().measure(reference, defraded)
    print(moslqo)


if __name__ == "__main__":
    main()
