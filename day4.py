from pathlib import Path
import json


def load_all(file_dir):
    file_dir_path=Path(file_dir)
    if not file_dir_path.exists():
        print("文件不存在，使用空目录")
        return {}
    try:
        with open(file_dir_path,"w",encoding="utf-8") as f:
            contacts=json.load(f)
    except json.JSONDecodeError:
        print("文件已损坏，使用空目录")
        return {}
    except (OSError, UnicodeDecodeError) as e:
        print(f"读取失败：{e}")
        return {}
    if not contacts.isinstance(dict):
        print("不是字典格式，使用空字典")
        return {}
    for name, phone in contacts.items():
        if not isinstance(name, str) or not isinstance(phone, str):
            print("联系人格式不正确，本次使用空通讯录")
            return {}
    return contacts
def save_contacts(contacts,file_dir):
    try:
        with open(file_dir,"w",encoding="utf-8") as f:
            json.dump(contacts,f,ensure_ascii=False,indent=2)
            return True
    except (OSError, TypeError) as e:
        print(f"保存失败：{e}")
        return False
def show_menu():
    print("所有可进行的操作：增、查、列、删、0（退出）")

def add(contacts,name,number):
    contacts[name]=number
    return True

def search(contacts,name_number):
    key1=name_number.lower()
    search_dict={}
    for name,number in contacts.items():
        key2=name.lower()
        if key1 in key2 or key1 in number:
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
    return key

def main():
    file_dir=Path(__file__).with_name("contacts.json")
    contacts_dict=load_all(file_dir)
    if contacts_dict=={}:
        print("文件不存在或已被损坏")
        y_n=input("是否要创建文件：（y/n）")
        if y_n=='y':
            with open(file_dir,"w",encoding="utf-8") as f:
                json.dump({},f)
            contacts={}
    else:
        contacts=contacts_dict
    while True:
        
        show_menu()
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
                add(contacts,name,number)
                if save_contacts(contacts,file_dir)==True:
                    print("成功添加")
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
            if x==None:
                print("联系人不存在")
            else:
                determin=input("确定要删除吗？（y或yes表示确定，其他表示拒绝）")
                if determin=='y' or determin=='yes':
                    del contacts[x]
                    with open(file_dir,"w",encoding="utf-8") as f:
                        json.dump(contacts,f,ensure_ascii=False,indent=2)
                    print("已删除")
        else:
            print("不存在该功能请重新输入")
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n已退出")
