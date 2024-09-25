"""
main함수
"""


import os


from module.processing_folder import processing_folder


def main():
    """main함수"""
    print("\n>>>>>>북마크 레벨별 제거기<<<<<<\n")
    print("-"*24)
    input_path = input("PDF 파일이 있는 폴더 경로를 입력하세요(종료는 0을 입력) : ").strip()

    if input_path == '0':
        return 0

    level_input = int(input("제거를 원하는 레벨 수를 입력하세요 : "))
    output_path = input("수정된 PDF 파일을 저장할 폴더 경로를 입력하세요 : ").strip()

    if not os.path.isdir(input_path) and not os.path.isdir(output_path):
        print("폴더 경로를 다시 확인하세요")
        return main()

    output_path = os.path.join(output_path, os.path.basename(input_path))
    os.makedirs(output_path)

    print("-"*24)
    print("\n작업중입니다. 데이터가 손상될 수 있으니 데이터를 수정하지 마세요.\n")
    processing_folder(input_path, level_input, output_path)
    print("-"*24)
    print(f"{output_path}에 새로운 PDF가 저장되었습니다.")
    print("\n~~~모든 작업이 완료되었습니다~~~")

    return main()


if __name__ == "__main__":
    main()
