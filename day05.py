from pathlib import Path
import json



class Contactsclass:
    def __init__(self,file_dir):
        self.file_dir=file_dir
        self.contacts={}

    def load_all(self):
        if not Path(self.file_dir).exists():
            print("文件不存在，使用空目录")
            return {}
        try:
            with open(self.file_dir,"r",encoding="utf-8") as f:
                self.contacts=json.load(f)
        except json.JSONDecodeError:
            print("")
            return {}
        except (OSError, UnicodeDecodeError) as e:
            print(f"")
            return {}
        if not isinstance(self.contacts,dict):
            print("")
            return {}
        for name,number in self.contacts.items():
            if not isinstance(name,str) or not isinstance(number,str):
                print("")
                return {}
        return self.contacts

    def save_contacts(self):
        try:
            with open(self.file_dir,"w",encoding="utf-8") as f:
                json.dump(self.contacts,f,ensure_ascii=False,indent=2)
                return True
        except (OSError, TypeError) as e:
            print(f"读取失败：{e}")
            return False

    def add_contacts(self,name,number):
        self.contacts[name]=number
        self.save_contacts()
        return True

    def search_contacts(self,keywords):
        keywords=keywords.lower()
        search_dict={}
        for name,number in self.contacts.items():
            key0=name.lower()
            if keywords in key0:
                search_dict[name]=number
            elif keywords in number:
                search_dict[name]=number
            else:
                continue
        return search_dict

    def list_all(self):
        return self.contacts

    def find(self,name_number):
        key=None
        for name,number in self.contacts.items():
            if name==name_number or number==name_number:
                key=name
        return key

    def delete(self,key):
        del self.contacts[key]
        self.save_contacts()
        return True
    
    def show_menu(self):
        return "菜单:增、删、查、列、0（退出）"

    def len(self):
        i=0
        for name in self.contacts.items():
            i+=1
        return i
def main():
    file_dir=Path(__file__).with_name("contacts.json")
    book=Contactsclass(file_dir)
    contacts=book.load_all()
    while True:
        print(book.show_menu())
        act=input("请输入需要的操作:")
        if act=='0':
            break
        elif act=='增':
            name=input("想要添加的姓名:")
            if name in contacts:
                print("联系人已存在")
                continue
            number=input("联系方式:")
            if len(number)!=11 or not number.isdigit():
                print("联系方式不合规")
                continue
            x=book.add_contacts(name,number)
            if x==True:
                print("成功添加")
            else:
                print("添加失败")
        elif act=='删':
            keywords=input("请输入想要删除的姓名或联系方式:")
            key=book.find(keywords)
            if key is None:
                print("联系人本身不存在")
            else:
                act0=input("确定删除吗？y/n")
                if act0=='y':
                    act1=book.delete(keywords)
                    if act1==True:
                        print("成功删除")
                    else:
                        print("删除失败")
                else:
                    print("已取消删除")
        elif act=='查':
            name_number=input("请输入要查找的联系人或联系方式:")
            found_dict=book.search_contacts(name_number)
            if found_dict=={}:
                print("通讯录为空")
            else:
                i=0
                for name,number in found_dict.items():
                   i+=1
                   print(f"第{i}个联系人 姓名:{name} 联系方式:{number}") 
        elif act=='列':
            search_dict=book.list_all()
            i=0
            for name,number in search_dict.items():
               i+=1
               print(f"第{i}个联系人 姓名:{name} 联系方式:{number}")
        else:
            print("不存在该功能")
            continue 


if __name__=="__main__":
    main()
