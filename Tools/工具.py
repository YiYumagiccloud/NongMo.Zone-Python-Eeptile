import os

def 创建文件夹(主: str, 次: str, 默认位置=r'D:\图片\爬到的图片'):
    r"""

    主, 次 -> 传入文件夹名称

    如果没有将会创建 -> D:\图片\爬到的图片\ 主 \ 次

    """

    if not os.path.exists(f'{默认位置}\\{主}\\{次}'):

        print()
        print(fr' - 创建文件夹 - {主} - {次} - ')
        print()

        os.makedirs(f'{默认位置}\\{主}\\{次}')
