# os
# 운영 체제와 관련된 기능을 제공하는 파이썬 내장 모듈
# 파일 경로 조작, 디렉토리 관리 등과 같은 작업을 수행할 때 유용

import os

# getcwd(): 현재 작업 디렉토리 경로 알려주는 함수
# print(os.getcwd())
# os.chcir('경로'): 디렉토리 변경
# prefix r: raw string을 그대로 가져다 쓰겠다.
os.chdir(r'C:\Users\KEI\Desktop\특허평가보고서')
# print(os.getcwd())
# listdir(): 디렉토리 파일 리스트 반환

file_names = os.listdir()

# os.path.splitext(filename): 파일명과 확장자 튜플 형태로 분리
# [0]: 파일명만 추출 / [1]: 확장자만 추출
# for filename in file_names:
#     print(os.path.splitext(filename)[0])

# 특정 확장자만 추출
for filename in file_names:
    if os.path.splitext(filename)[1] == '.pdf':
        print(filename)