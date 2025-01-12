FROM python:3.9-slim

WORKDIR /app

# requirements.txt가 있다면 복사 후 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Python 스크립트 복사
COPY main.py .

# 컨테이너 실행 시 main.py 실행
CMD ["python", "main.py"]