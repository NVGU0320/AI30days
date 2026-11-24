"命令行通讯录 v1：增/查/列/删，函数拆分 ≥ 4 个。"

contacts={}

def show_menu():
    print("所有可进行的操作：增、查、列、删、0（退出）")

def add(contacts,name,number):
    contacts[name]=number
    return "添加成功"

def search(contacts,name_number):
    found=False
    key1=name_number.lower()
    search_dict={}
    for name,number in contacts.items():
        key2=name.lower()
        if key1 in key2 or key1 in number:
            found=True
            search_dict[name]=number
    return search_dict
    

def show_all(contacts):
    if contacts=={}:
        print("通讯录为空")
    n=0
    for name,number in contacts.items():
        n=n+1
        print(f"第{n}个联系人：姓名：{name}，电话号码：{number}")

def delete(contacts,delete_name_number):
    key=None
    for name,number in contacts.items():
        if name==delete_name_number or number==delete_name_number:
            key=name
            break
    if key==None:
        return "联系人不存在"
    return key
def main():
    show_menu()
    while True:
        choice=input("想要进行的操作：").strip()
        if choice=='0':
            break
        elif choice=='增':
            name=input("请输入姓名：").strip()
            if name in contacts:
                print("联系人已存在")
                continue
            number=input("请输入手机号：").strip()
            if len(number)==11 and number.isdigit() and name!='':
                print(add(contacts,name,number))
            else:
                print("请重新输入")
                continue
        elif choice=='查':
            name_number=input("请输入要查询的姓名或手机号：").strip()
            x=search(contacts,name_number)
            if x!={}:
                for name,number in x.items():
                    print(f"找到联系人{name}：{number}")
            else:
                print("未找到联系人")
        elif choice=='列':
            show_all(contacts)
        elif choice=='删':
            delete_name_number=input("请输入要删除的姓名或号码：").strip()
            x=delete(contacts,delete_name_number)
            if x=='联系人不存在':
                print(x)
            else:
                determin=input("确定要删除吗？（y或yes表示确定，其他表示拒绝）")
                if determin=='y' or determin=='yes':
                    del contacts[x]
                    print("已删除")
        else:
            print("不存在该功能请重新输入")
if __name__ == "__main__":
    main()
