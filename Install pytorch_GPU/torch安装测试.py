import torch

print(f"PyTorch版本: {torch.__version__}")
print(f"CUDA可用: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"CUDA版本: {torch.version.cuda}")
    print(f"GPU设备数量: {torch.cuda.device_count()}")
    print(f"当前设备: {torch.cuda.current_device()}")
    print(f"设备名称: {torch.cuda.get_device_name(0)}")
    print(f"设备内存: {torch.cuda.get_device_properties(0).total_memory/1024**3:.2f} GB")
else:
    print("当前安装的是CPU版PyTorch或CUDA不可用")

# 版本号没有+cuxx后缀，表示是CPU版本

