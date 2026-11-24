from pathlib import Path
import json



class Contactsclass:
    def __init__(self,file_dir):
        self.file_dir=file_dir
        self.contacts={}

    def load_all(self):
        if Path(self.file_dir).exists():
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
                json.dump(self.contacts,self.file_dir,ensure_ascii=False,indent=2)
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
            key0=name.lower
            if keywords in key0:
                search_dict[name]=number
            elif keywords in number:
                search_dict[name]=number
            else:
                continue
        return search_dict

    def list_all(self):
        return self.contacts

    def delete(self,name_number):
        key=None
        for name,number in self.contacts.items():
            if name==name_number or number==name_number:
                key=name
        return key

    