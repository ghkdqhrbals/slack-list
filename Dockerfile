FROM python:3.9-slim

WORKDIR /app

# Python 의존성 설치 (필요할 경우)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Python 스크립트 복사
COPY main.py .

# 기본 실행 명령 설정
CMD ["python", "/app/main.py"]