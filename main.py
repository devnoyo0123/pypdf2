# import os
# from PyPDF2 import PdfFileMerger
# import stat
#
# def set_directory_permissions(path, mode=stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH):
#     """디렉토리 권한을 설정하는 함수."""
#     try:
#         os.chmod(path, mode)
#         print(f"권한이 {oct(mode)}로 변경되었습니다: {path}")
#     except PermissionError as e:
#         print(f"권한 변경에 실패했습니다: {e}")
#
# # 타겟 디렉토리를 절대 경로로 지정
# pdf_dir = '/Users/nohys/Downloads/batch'
# pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
#
# # PDF 파일 경로를 절대 경로로 변환
# pdf_files = [os.path.join(pdf_dir, f) for f in pdf_files]
#
# # 파일 이름 순서대로 정렬 (필요에 따라 조정 가능)
# pdf_files.sort()
#
# merger = PdfFileMerger()
#
# for pdf in pdf_files:
#     merger.append(pdf)
#
# # 저장할 타겟 디렉토리 지정
# target_save_dir = '/Users/nohys/Documents/MergedPdfs'
# # 해당 디렉토리가 없으면 생성
# if not os.path.exists(target_save_dir):
#     os.makedirs(target_save_dir)
#     # 디렉토리 생성 후 권한 설정
#     set_directory_permissions(target_save_dir)
#
# # 타겟 디렉토리에 저장될 파일의 절대 경로 생성
# merged_file_path = os.path.join(target_save_dir, "fastcampus-spring-batch-example.pdf")
#
# merger.write(merged_file_path)
# merger.close()
import os
from PyPDF2 import PdfFileMerger
import stat

def set_directory_permissions(path, mode=stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH):
    """디렉토리 권한을 설정하는 함수."""
    try:
        os.chmod(path, mode)
        print(f"권한이 {oct(mode)}로 변경되었습니다: {path}")
    except PermissionError as e:
        print(f"권한 변경에 실패했습니다: {e}")

# 사용자 입력을 통해 디렉토리 경로 및 파일명 받기
pdf_dir = input("PDF 파일이 있는 디렉토리를 입력하세요: ")
target_save_dir = input("병합된 PDF를 저장할 디렉토리를 입력하세요: ")
merged_filename = input("병합된 PDF 파일의 이름을 입력하세요 (확장자 제외): ")

# 파일명이 .pdf로 끝나는지 확인하고, 아니라면 추가
if not merged_filename.endswith('.pdf'):
    merged_filename += '.pdf'

pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
pdf_files = [os.path.join(pdf_dir, f) for f in pdf_files]
pdf_files.sort()

merger = PdfFileMerger()

for pdf in pdf_files:
    merger.append(pdf)

if not os.path.exists(target_save_dir):
    os.makedirs(target_save_dir)
    set_directory_permissions(target_save_dir)

merged_file_path = os.path.join(target_save_dir, merged_filename)

merger.write(merged_file_path)
merger.close()

print("병합된 PDF 파일이 저장되었습니다: {merged_file_path}")
