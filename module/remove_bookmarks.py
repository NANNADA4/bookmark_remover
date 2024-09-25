"""
입력받은 북마크보다 높은 레벨의 북마크를 모두 제거합니다
"""


import os
import fitz


def remove_bookmarks(pdf_path, level_threshold, output_folder):
    """주어진 PDF에서 레벨이 level_threshold보다 높은 북마크 제거"""
    document = fitz.open(pdf_path)
    bookmarks = document.get_toc()

    new_bookmark_list = []

    for bookmark in bookmarks:
        level = bookmark[0]
        if level < level_threshold:
            new_bookmark_list.append(bookmark)

    output_path = os.path.join(output_folder, os.path.basename(pdf_path))

    document.set_toc(new_bookmark_list)
    document.save(output_path)
    document.close()
