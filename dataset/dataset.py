import cv2
from torch.utils.data import DataLoader, Dataset
import albumentations #推荐的数据增强库，https://blog.csdn.net/qq_27039891/article/details/100795846

class MYdataloader(Dataset):
    def __init__(self, path,mode='train'):#定义训练/验证数据的相关信息，包括路径，数据增强等，形成数据的列表
        super(MYdataloader, self).__init__()
        pass

    def __getitem__(self, index):#分batch的读取数据，通过index指向获得__init__中得到的数据的位置
        return #返回的数据为numpy或者PIL的类型均可

    def __len__(self):#返回数据的长度
        return

if __name__ == '__main__':
    dataloader = DataLoader(MYdataloader(path='./'), batch_size=1, shuffle=True,num_workers=4)#这一步定义了dataloader，走到了__init__那步
    for step, data in enumerate(dataloader):#这一步开始在getitem中读取并处理数据
        print(data)
