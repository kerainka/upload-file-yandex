import requests

TOKEN = ""
FILE_PATH = "upload_me.txt"

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        upload_target = self.get_upload_target(file_path)
        with open(file_path, "rb") as f:
            upload_response = requests.put(upload_target, files={"file": f})
            upload_response.raise_for_status()
        return 'Успешно загружено'

    def get_upload_target(self, file_path):
        headers = {"Authorization": f"OAuth {self.token}"}
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload",
                                params={"path": file_path}, headers=headers)
        response.raise_for_status()
        href = response.json()["href"]
        return href

if __name__ == '__main__':
    uploader = YaUploader(TOKEN)
    result = uploader.upload(FILE_PATH)
    print(result)
