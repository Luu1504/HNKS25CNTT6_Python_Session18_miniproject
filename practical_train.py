students = [
    {
        "id": "SV001",
        "name": "Nguyen Van A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0,
        "average": 8.17,
        "rating": "Giỏi"
    },
]


def check_empty(text_input):
    return not text_input.strip()


def check_score(score_input):
    if not score_input.isdigit() or float(score_input) <= 0:
        return False


def check_id(student_list , id_input):
    if not student_list:
        return False
    
    for index , student in enumerate(student_list):
        if student['id'] == id_input:
            return index
    return -1


def calculate_student(math , physics , chemistry):
    total = (float(math) + float(physics) + float(chemistry)) / 3
    check_rating = ""

    if total < 5.0:
        check_rating = "Yếu"
    elif total >= 5.0 and total < 7.0:
        check_rating = "Trung bình"
    elif total >= 7.0 and total < 8.0:
        check_rating = "Giỏi"
    else:
        check_rating = "Giỏi"

    
    return total , check_rating


def display(student_list):
    if not student_list:
        print("Danh sách sinh viên hiện đang trống!")
        return
    
    print("-" * 80)
    print(f"{"MÃ SV":<7} | {"Tên":<20} | {"Toán":<4} | {"Lý":<4} | {"Hóa":<4} | {"ĐTB":<4} | {"Xếp loại học lực"}")
    print("-" * 80)
    for index , student in  enumerate(student_list):
        print("{id:<7} | {name:<20} | {math:<4} | {physics:<4} | {chemistry:<4} | {average:<4} | {rating}".format_map(student))
        print("-" * 80)


def create_new_student(student_list):
    new_student_id = input("Nhập mã sinh viên: ").strip().upper()
    if check_empty(new_student_id):
        print("Mã sinh viên không được bỏ trống!")
        return
    
    if check_id(student_list , new_student_id) != -1:
        print("Mã sinh viên đã tồn tại!")
        return
    
    new_student_name = input("Nhập tên của sinh viên: ").strip().title()
    if check_empty(new_student_name):
        print("Tên sinh viên không được để trống!")
        return


    new_student_math_score = input("Nhập Điểm toán: ").strip()
    if check_empty(new_student_math_score):
        print("Điểm toán không được bỏ trống!")
        return
    
    if check_score(new_student_math_score):
        print("Điểm không hợp lệ!")
        return
    
    new_student_physics_score = input("Nhập Điểm Lý: ").strip()
    if check_empty(new_student_physics_score):
        print("Điểm toán không được bỏ trống!")
        return
    
    if check_score(new_student_physics_score):
        print("Điểm không hợp lệ!")
        return
    
    new_student_chemistry_score = input("Nhập Điểm toán: ").strip()
    if check_empty(new_student_chemistry_score):
        print("Điểm toán không được bỏ trống!")
        return
    
    if check_score(new_student_chemistry_score):
        print("Điểm không hợp lệ!")
        return
    
    new_average , new_rating = calculate_student(float(new_student_math_score) , float(new_student_physics_score) , float(new_student_chemistry_score))

    new_student = {
        "id": new_student_id,
        "name": new_student_name,
        "math": float(new_student_math_score),
        "physics": float(new_student_physics_score),
        "chemistry": float(new_student_chemistry_score),
        "average": float(new_average),
        "rating": new_rating
    }

    student_list.append(new_student)
    print("Đã thêm sinh viên thành công!")


def update_student(student_list):
    update_student_id = input("Nhập mã sinh viên: ").strip().upper()
    if check_empty(update_student_id):
        print("Mã sinh viên không được bỏ trống!")
        return
    
    index = check_id(student_list , update_student_id)

    student = student_list[index]

    if index == -1:
        print("Mã sinh viên không tồn tại!")
        return
    
    update_student_math_score = input("Nhập Điểm toán: ").strip()
    if check_empty( update_student_math_score):
        print("Điểm toán không được bỏ trống!")
        return
    
    if check_score(update_student_math_score):
        print("Điểm không hợp lệ!")
        return
    
    update_student_physics_score = input("Nhập Điểm Lý: ").strip()
    if check_empty(update_student_physics_score):
        print("Điểm toán không được bỏ trống!")
        return
    
    if check_score(update_student_physics_score):
        print("Điểm không hợp lệ!")
        return
    
    update_student_chemistry_score = input("Nhập Điểm toán: ").strip()
    if check_empty(update_student_chemistry_score):
        print("Điểm toán không được bỏ trống!")
        return
    
    student['math'] = float(update_student_math_score)
    student['physics'] = float(update_student_physics_score)
    student['chemistry'] = float(update_student_chemistry_score)

    update_average , update_rating = calculate_student(float(update_student_math_score) , float(update_student_physics_score) , float(update_student_chemistry_score))

    student['average'] = update_average
    student['rating'] = update_rating

    print("Đã cập nhật thông tin sinh viên thành công!")


def delete_student(student_list):
    delete_student_id = input("Nhập mã sinh viên: ").strip().upper()
    if check_empty(delete_student_id):
        print("Mã sinh viên không được để trống!")
        return
    
    index = check_id(student_list , delete_student_id)
    if index == -1:
        print("Mã sinh viên không tồn tại!")
        return
    
    student = student_list[index]
    print(f"Tìm thấy sinh viên {student}")

    confirm_delete = input("Bạn có xác nhận muốn xóa? Y/N: ").strip().upper()

    if check_empty(confirm_delete):
        print("Không được để trống!")
        return
    
    if confirm_delete == "Y":
        student_list.pop(index)
        print("Đã xóa thành công!")
    else:
        print("Đã thoát!")
        return
    

def find_student(student_list):
    if not student_list:
        print("Danh sách hiên tại đang trống!")
        return
    
    keyword = input("Nhập từ khóa: ").strip().upper()
    if check_empty(keyword):
        print("Mã sinh viên không được để trống!")
        return
    

    result = []

    for student in student_list:
        if keyword == student['id'] or keyword in student['name']:
            result.append(student)
            print(f"Tìm thấy sinh viên {student}")

    
def static_score(student_list):
    count = 0
    stats = {"Giỏi": 0 , "Khá": 0 , "Trung bình": 0 , "Yếu": 0}

    for student in student_list:
        stats[student['rating']] += 1
    
    for rating , count in stats.items():
        print(f"Sinh viên đạt loại {rating:<13} có {count} em")


def main():
    check = True
    while check:
        menu = """
        1. Hiển thị danh sách 
        2. Tiếp nhận sinh viên
        3. Cập nhật kết quả
        4. Xóa sinh viên
        5. Tìm kiếm sinh viên
        6. Thống kê TB
        7. Phân loại học lực
        8. Thoát
        """

        print(menu)

        choice = input("Chọn chức năng (1-8): ").strip()
        if check_empty(choice):
            print("Lựa chọn chức năng không được để trống!")
            return
        
        match choice:
            case "1":
                display(students)
                print()
            case "2":
                create_new_student(students)
                print()
            case "3":
                update_student(students)
                print()
            case "4":
                delete_student(students)
                print()
            case "5":
                find_student(students)
                print()
            case "6":
                static_score(students)
                print()
            case "7":
                
                print()
            case "8":
                check = False
                print("Đã thoát chương trình!")
            case _:
                print("Không có lựa chọn hợp lệ!")

main()