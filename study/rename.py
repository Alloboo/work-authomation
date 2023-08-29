import os

file_path = r'C:\Users\KEI\Desktop\특허평가보고서'


# 1. os 모듈의 경로와 확장자를 보여주는 splitext 함수 활용하기 
# -> 근데 실제 변경하려면 다른 거 필요(rename)
# pat: 파일명 전까지의 경로 / ext: 확장자명
# file_name_list = os.listdir(file_path)
# new_file_name_list = []
# i = 1

# for n in file_name_list:
#     pat, ext = os.path.splitext(n)
#     new_file_name_list.append(os.path.join(file_path, "보고서당" + f'{i}' + ext))
# print(new_file_name_list)

# 2. os 모듈의 rename 함수 활용하기
# 리스트 순서는 임의
file_names = os.listdir(file_path)

i = 1
for f in file_names:
    # 현재 파일의 경로, file_path와 현재 파일의 이름으르 결합
    # os.path.join(): 여러 개의 경로 세그먼트를 하나로 결합하여 새로운 경로 반환
    src = os.path.join(file_path, f)

    # 이름 생성하여 할당: '변경할 이름' + 번호 + 확장자명
    dst = '보고서임'+str(i)+'.pdf'
    # 새로운 경로 생성하여 재할당
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1
