orders = [
    {'id': 'HD01', 'name': 'Dai ly Hoang Long', 'price': 45000000, 'status': 'Paid'},
    {'id': 'HD02', 'name': 'Tap hoa Minh Thu', 'price': 15000000, 'status': 'Unpaid'}
]


def check_empty(text_input):
    return not text_input.strip()


def display(order_list):
    if not order_list:
        print("Danh sách trống!")
        return
    
    print("------ DANH SÁCH ĐƠN HÀNG ĐẠI LÝ ------")
    print(f"{"MÃ ĐƠN":<8} | {"TÊN ĐẠI LÝ":<20} | {"GIÁ TRỊ (VND)":<15} | {"TRẠNG THÁI"}")
    print("-" * 70)
    for item in order_list:
        print("{id:<8} | {name:<20} | {price:<15} | {status}".format_map(item))
        print("-" * 70)


def check_id(order_list , id_input):
    if not order_list:
        print("Danh sách trống!")
        return

    for index , item in enumerate(order_list):
        if id_input == item['id']:
            return index
    return -1

def check_price(price_input):
    if check_empty(price_input):
        return
    
    if not price_input.isdigit() or int(price_input) <= 0:
        return False
    return True

def create_new_order(order_list):
    if not order_list:
        print("Danh sách trống!")
        return
    
    new_order_id = input("Nhập mã đơn hàng: ").strip().upper()
    if check_empty(new_order_id):
        print("Mã đơn hàng không được bỏ trống!")
        return
    
    if check_id(order_list , new_order_id) != -1:
        print("Mã đơn hàng đã tồn tại!")
        return
    
    new_order_store = input("Nhập tên đại lý: ").strip().title()
    if check_empty(new_order_store):
        print("Tên đại lý không được bỏ trống!")
        return
    
    new_order_price = input("Nhập giá trị đơn hàng (VND): ").strip()
    if check_empty(new_order_price):
        print("Giá đơn hàng không được bỏ trống!")
        return

    if check_price(new_order_price) == False:
        print    


def main():
    check = True
    while check:
        menu = """
        === QUẢN LÝ ĐƠN HÀNG - AGENT ORDER ===
        1. Xem danh sách đơn hàng hiện có
        2. Tạo mới đơn hàng đại lý
        3. Cập nhật trạng thái thanh toán
        4. Tính tổng doanh thu & Chiêt khâu
        5. Thoát chương trình
        """
        print(menu)

        choice = input("Chọn chức năng (1-5): ").strip()

        if check_empty(choice):
            print("Lựa chọn không được bỏ trống!")
            return
        
        match choice:
            case "1":
                display(orders)
                print()
            case "2":
                print()
            case "3":
                print()
            case "4":
                print()
            case "5":
                check = False
                print()
            case _:
                print()

main()