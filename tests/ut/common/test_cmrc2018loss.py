# Copyright 2022 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Test CMRC2018Loss"""

import unittest
import numpy as np
import mindspore
from mindspore import Tensor
from mindtext.common.loss import CMRC2018Loss


class TestCMRC2018Loss(unittest.TestCase):
    r"""
    Test CMRC2018Loss
    """

    def setUp(self):
        self.input = None

    def test_loss(self):
        r"""
        Test CMRC2018Loss loss
        """

        cmrc_loss = CMRC2018Loss()
        tensor_a = Tensor(np.array([1, 2, 1]), mindspore.int32)
        tensor_b = Tensor(np.array([2, 1, 2]), mindspore.int32)
        my_context_len = Tensor(np.array([2., 1., 2.]), mindspore.float32)
        tensor_c = Tensor(np.array([
            [0.1, 0.2, 0.1],
            [0.1, 0.2, 0.1],
            [0.1, 0.2, 0.1]
        ]), mindspore.float32)
        tensor_d = Tensor(np.array([
            [0.2, 0.1, 0.2],
            [0.2, 0.1, 0.2],
            [0.2, 0.1, 0.2]
        ]), mindspore.float32)
        loss = cmrc_loss(tensor_a, tensor_b, my_context_len, tensor_c, tensor_d)
        assert loss.shape == ()
