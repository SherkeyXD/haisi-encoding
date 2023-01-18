from dict import getdict
import re
import sys


def encode(text: str, seed: int) -> str:
    dic = getdict(seed)
    result = ''
    for i in text:
        result += dic[i]
    return result


def decode(text: str, seed: int) -> str:
    redic = {v: k for k, v in getdict(seed).items()}
    result = ''
    ma = r"（[\u4e00-\u9fa5]*）（[\u4e00-\u9fa5]*）（[\u4e00-\u9fa5]*）（[\u4e00-\u9fa5]*）"
    words = re.findall(ma, text)
    for i in words:
        result += redic[i]
    return result


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('使用方法：')
        print('    python3 main.py decode 要解码的文字 密码（可选）')
        print('    python3 main.py encode 要编码的文字 密码（可选）')
        print('提示：需要的话将文字用引号括起来')
    elif sys.argv[1] == 'encode':
        seed = sys.argv[3] if len(sys.argv) >= 4 else 114514
        print(encode(sys.argv[2], seed))
    elif sys.argv[1] == 'decode':
        seed = sys.argv[3] if len(sys.argv) >= 4 else 114514
        print(decode(sys.argv[2], seed))
    else:
        print('使用方法：')
        print('    python3 decode 要解码的文字 密码（可选）')
        print('    python3 encode 要编码的文字 密码（可选）')
        print('提示：需要的话将文字用引号括起来')
