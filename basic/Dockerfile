# 使用官方 Python 映像作為基礎映像
FROM python:3.9

# 設定工作目錄
WORKDIR /app

# 複製依賴項列表並安裝
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式源代碼
COPY . .

# 對外暴露應用程式埠
EXPOSE 5000

# 定義 Docker 容器啟動時執行的命令
CMD ["python", "app.py"]
