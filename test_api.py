import os
from fastapi.testclient import TestClient
from WhisperOnFastAPI import app

client = TestClient(app)


# Тест для загрузки файла
def test_upload_file():
    files = {'file': ('test_file.txt', 'test content')}
    response = client.post("/uploadfile/", files=files)
    assert response.status_code == 200
    assert "filename" in response.json()


# Тест для списка файлов (просто проверим успешный статус)
def test_list_files():
    response = client.get("/listfiles")
    assert response.status_code == 200


# Тест для удаления файла (просто проверим успешный статус)
def test_delete_file():
    filename = "test_delete.txt"
    # Создадим файл для последующего удаления
    with open(os.path.join("uploads/", filename), 'w') as test_file:
        test_file.write("test content")

    response = client.delete(f"/deletefile/{filename}")
    assert response.status_code == 200
