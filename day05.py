from pathlib import Path
import json



class Contactsclass:
    def __init__(self,file_dir):
        self.file_dir=file_dir
        self.contacts={}
        self.load_all()

    def load_all(self):
        self.contacts={}
        if not Path(self.file_dir).exists():
            print("文件不存在，使用空目录")
            return self.contacts
        try:
            with open(self.file_dir,"r",encoding="utf-8") as f:
                data=json.load(f)
        except json.JSONDecodeError:
            print("")
            return self.contacts
        except (OSError, UnicodeDecodeError) as e:
            print(f"")
            return self.contacts
        if not isinstance(self.contacts,dict):
            print("")
            return self.contacts
        for name,number in self.contacts.items():
            if not isinstance(name,str) or not isinstance(number,str):
                print("")
                return self.contacts
        self.contacts=data
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
        if name in self.contacts:
            return "联系人已存在"
        if name=='':
            return "联系人不可为空"
        if len(number)!=11 or not number.isdigit():
            return "联系方式不合规"
        self.contacts[name]=number
        if not self.save_contacts():
            del self.contacts[name]
            return "保存失败，已回滚"
        return "保存成功"

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
        if name_number in self.contacts:
            key=name_number
            return key
        for name,number in self.contacts.items():
            if name==name_number or number==name_number:
                key=name
                return key
        return None

    def delete(self,key):
        if key is None:
            return "联系人不存在"
        number=self.contacts[key]
        del self.contacts[key]
        if not self.save_contacts():
            self.contacts[key]=number
            return "保存失败，删除已撤销"
        return "删除成功"
    
    def show_menu(self):
        return "菜单:增、删、查、列、0（退出）"

    def __len__(self):
        return len(self.contacts)
def main():
    file_dir=Path(__file__).with_name("contacts.json")
    book=Contactsclass(file_dir)
    contacts=book.load_all()
    while True:
        print(book.show_menu())
        act=input("请输入需要的操作:").strip()
        if act=='0':
            break
        elif act=='增':
            name=input("想要添加的姓名:").strip()
            number=input("联系方式:").strip()
            print(book.add_contacts(name,number))
        elif act=='删':
            keywords=input("请输入想要删除的姓名或联系方式:").strip()
            key=book.find(keywords)
            print(book.delete(key))
        elif act=='查':
            name_number=input("请输入要查找的联系人或联系方式:").strip()
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
