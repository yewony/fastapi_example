#!/bin/bash

# 여기는 코멘트이다.
# 코멘트처리된 구문은 실행되지 않는다.

echo "Hello, World!"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000