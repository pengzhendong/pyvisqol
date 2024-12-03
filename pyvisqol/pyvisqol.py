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

import os
import platform
import sys

import librosa
import numpy as np
from modelscope.hub.file_download import model_file_download

visqol_lib = os.path.join(os.path.dirname(__file__), "visqol_lib_py.so")
if not os.path.exists(visqol_lib):
    python_version = f"{sys.version_info.major}{sys.version_info.minor}"
    src = model_file_download(
        "pengzhendong/visqol",
        f"visqol_lib_py_{platform.system().lower()}_py{python_version}.so",
    )
    os.symlink(src, visqol_lib)

from . import visqol_lib_py
from .pb2 import similarity_result_pb2, visqol_config_pb2


class Visqol:
    def __init__(self, mode="speech"):
        config = visqol_config_pb2.VisqolConfig()
        if mode == "audio":
            self.sample_rate = 48000
            config.audio.sample_rate = self.sample_rate
            self.config.options.use_speech_scoring = False
            svr_model_path = "libsvm_nu_svr_model.txt"
        elif mode == "speech":
            self.sample_rate = 16000
            config.audio.sample_rate = self.sample_rate
            config.options.use_speech_scoring = True
            svr_model_path = "lattice_tcditugenmeetpackhref_ls2_nl60_lr12_bs2048_learn.005_ep2400_train1_7_raw.tflite"
        else:
            raise ValueError(f"Unrecognized mode: {mode}")
        config.options.svr_model_path = os.path.join(os.path.dirname(visqol_lib_py.__file__), "model", svr_model_path)

        self.api = visqol_lib_py.VisqolApi()
        self.api.Create(config)

    def measure(self, reference, defraded):
        reference, _ = librosa.load(reference, sr=self.sample_rate)
        defraded, _ = librosa.load(defraded, sr=self.sample_rate)
        reference = reference.astype(np.float64)
        defraded = defraded.astype(np.float64)
        similarity_result = self.api.Measure(reference, defraded)
        return similarity_result.moslqo
