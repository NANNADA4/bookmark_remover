"""
입력받은 폴더를 순회하여 PDF파일 발견시 스크립트가 수행됩니다
"""


import os
from natsort import natsorted


from module.remove_bookmarks import remove_bookmarks


def processing_folder(folder_path, level_threshold, output_folder):
    """주어진 폴더 내의 모든 PDF 파일 처리"""
    for root, _, files in os.walk(folder_path):
        for file in natsorted(files):
            if not file.lower().endswith('.pdf'):
                continue
            pdf_path = os.path.join(root, file)
            remove_bookmarks(
                pdf_path, level_threshold, output_folder)
