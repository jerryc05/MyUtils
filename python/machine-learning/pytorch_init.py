#%% PyTorch self-check script by github.com/jerryc05.

__tab_w__ = 4


def __print_ljusted(s: str):
    print(end=s.ljust(40), flush=True)


def __print_rjusted(s: str):
    print(s.rjust(25))


print()
__print_ljusted('PyTorch:')
import torch
__print_rjusted(f'v{torch.version.__version__} ✅')

__print_ljusted(' ' * __tab_w__ + 'Neural Network:')
nn = torch.nn
F = nn.functional
__print_rjusted('Imported ✅')

__print_ljusted(' ' * __tab_w__ + 'Optimizer:')
optim = torch.optim
__print_rjusted('Imported ✅')

print()
print('Cuda:')
__print_ljusted(' ' * __tab_w__ + 'Availability:')
if not torch.cuda.is_available():
    device = torch.device('cpu')
    __print_rjusted(' ' * __tab_w__ + 'N/A ❌')
else:
    device = torch.device('cuda')
    __print_rjusted(' ' * __tab_w__ + 'Working ✅')

    __print_ljusted(' ' * __tab_w__ + 'Version:')
    __print_rjusted(f'v{torch.version.cuda} ✅')

    current_id = torch.cuda.current_device()
    print(' ' * __tab_w__ + 'Cuda devices:')
    for i in range(torch.cuda.device_count()):
        prop = torch.cuda.get_device_properties(i)
        if i == current_id:
            __print_ljusted(' ' * __tab_w__ + f'#{i} ✅  {prop.name.ljust(30)}')
        else:
            __print_ljusted(' ' * __tab_w__ + f'#{i} ✋  {prop.name.ljust(30)}')
        mem = prop.total_memory
        mem_units = ('B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z')
        mem_unit = 0
        while mem > 1024:
            mem_unit += 1
            mem /= 1024.
        __print_rjusted(
            f'{prop.multi_processor_count: 3} procs {mem:4.0f} {mem_units[mem_unit]}'
        )

print()
__print_ljusted('TorchVision:')
import warnings
warnings.filterwarnings("ignore")
import torchvision
warnings.filterwarnings("default")
__print_rjusted(f'v{torchvision.__version__} ✅')

__print_ljusted(' ' * __tab_w__ + 'TorchVision Transforms:')
import torchvision.transforms as transforms
__print_rjusted('Imported ✅')

print()
__print_ljusted('NumPy:')
import numpy as np
__print_rjusted(f'v{np.__version__} ✅')

print()
__print_ljusted('IPython display func:')
try:
    import IPython.display as display
    __print_rjusted('Imported ✅')
except Exception as e:
    __print_rjusted(f'{e} ❌')

print()
__print_ljusted('Matplotlib:')
try:
    import matplotlib
    import matplotlib.pyplot as plt
    __print_rjusted(f'v{matplotlib.__version__} ✅')
except Exception as e:
    __print_rjusted(f'{e} ❌')

print()
__print_ljusted('IPython Matplotlib Inline Magic:')
try:
    from IPython import get_ipython
    ipython = get_ipython()
    ipython.magic('matplotlib inline')
    __print_rjusted('Done ✅')
except:
    __print_rjusted('Not in IPython ❌')

print()
print('===== All Check Finished! ====='.center(60))
print()


#%%
