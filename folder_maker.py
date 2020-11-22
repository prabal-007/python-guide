import os
class Folder_Maker(object):
    def __init__(self, work_area):
        os.chdir(work_area)

    def create_folder(self, amount=1):
        amount = amount
        while True:
            try:
                if amount == 1:
                    folder_name = input("Enter folder name :")
                    os.mkdir(folder_name)
                    break
                else:
                    for _ in range(amount):
                        folder_name = input("Enter folder name : ")
                        os.makedirs(folder_name)
                        amount -= 1
                    break
            except:
                print("Invalid Filename")
                continue
    
if __name__ == "__main__":
    work_area = os.path.join(os.path.expanduser("~"),"Downloads")
    folder = Folder_Maker(work_area)
    folder.create_folder(2)
