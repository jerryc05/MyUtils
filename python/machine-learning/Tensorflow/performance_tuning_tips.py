# %%
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Warning and Error only

import tensorflow as tf
from tensorflow.python.client import device_lib
import re

print(f'Tensorflow v{tf.__version__}'.center(90, '·'))

tf_exp_config = tf.config.experimental

print('\nLocal Devices:')
gpu_name_re = re.compile('name: ?([A-Za-z0-9 ]+)(?=(?:,|$))')
cp_cap_re = re.compile('compute capability: ?([0-9.]+)(?=(?:,|$))')
unit = ('M', 'G', 'T', 'P''E',)
for i, x in enumerate(device_lib.list_local_devices()):
    print(f'\t{i}: name \t=[{x.name}]')
    try:
        _desc = x.physical_device_desc
        print(f'\t{i}: model\t=[{gpu_name_re.search(_desc).group(1)}]')
        print(f'\t{i}: capability\t=[{cp_cap_re.search(_desc).group(1)}]')
        del _desc
    except AttributeError:
        ...
    print(f'\t{i}: type \t=[{x.device_type}]')
    _mem = x.memory_limit / 1024 / 1024
    unit_i = 0
    while _mem > 1024 and unit_i < len(unit):
        _mem /= 1024
        unit_i += 1
    print(f'\t{i}: memory\t=[{_mem:.1f} {unit[unit_i]}]')
    print()
    del _mem, unit_i
del gpu_name_re

print('Visible Devices:')
for i, x in enumerate(tf_exp_config.get_visible_devices()): print(f'\t{i}: {x}')
print()

print(f'Device Policy: {tf_exp_config.get_device_policy()}')
print()

print(f'Visible GPU Configs:')
gpus = tf_exp_config.get_visible_devices('GPU')
for i, x in enumerate(gpus):
    print(f'\t{i}: {x}')
    tf_exp_config.set_memory_growth(x, True)
    print(f'\t{i}: Memory Growth: {tf_exp_config.get_memory_growth(x)}')
print()

del tf_exp_config, unit, i, x

# %%
from tensorflow.keras.mixed_precision import experimental as mixed_precision

for i, x in enumerate(device_lib.list_local_devices()):
    if x.device_type != 'GPU':
        continue
    _desc = x.physical_device_desc
    _capability = float(cp_cap_re.search(_desc).group(1))
    if _capability > 7:
        print('Enabling Mixed Precision...')
        float16_policy = mixed_precision.Policy('mixed_float16')
        mixed_precision.set_policy(float16_policy)
        print(f'\tCompute  dtype: {float16_policy.compute_dtype}')
        print(f'\tVariable dtype: {float16_policy.variable_dtype}')
        del float16_policy
    else:
        print(f'Skipping Mixed Precision due to compute capability [{_capability}] < 7')
    del cp_cap_re, _desc, _capability
    print()
    break

# %%
tf.config.optimizer.set_jit(True)
print('Enabled XLA for TensorFlow models')

# %%