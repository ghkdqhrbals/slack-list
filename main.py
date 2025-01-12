import os
import json
import sys

def main():
    # GitHub Actions 입력값은 환경변수로 전달됨
    input_command = os.getenv('INPUT_COMMAND', '').strip()

    if input_command == "list":
        # 리스트 데이터
        result_list = ["apple", "banana", "cherry"]
        print(f"List: {json.dumps(result_list)}")

        # GitHub Action output 설정
        print(f"::set-output name=result::{json.dumps(result_list)}")
    else:
        print(f"Error: Unsupported command '{input_command}'")
        sys.exit(1)

if __name__ == "__main__":
    main()