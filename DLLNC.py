from NodeMahasiswa import NodeMahasiswa
class DLLNC:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def isEmpty(self):
        self.size=0
    def __len__(self,ukuran):
        return ukuran
    
    def  addElementTail(self,_element,_ipk):
        baru=NodeMahasiswa(_element,_ipk)
        if self.size==0:
            self.head=baru
            self.tail=baru
        else:
            self.tail._next=baru
            baru._prev=self.tail
            self.tail=baru  
        print("data masuk ke tail")
        self.size=self.size + 1

    def deleteLast(self):
        if self.size==1:
            self.head=None
            self.tail= None
        else:
            hapus=self.head
            self.head=self.head._next
            hapus._next=None
            self.head._prev=None
            del hapus
        print("Data Terhapus")
        self.size=self.size-1

    def printDescending(self):
        print("=====PRINT DESCENDING=====")
        bantu=self.head
        while bantu != None:
            print("==========")
            print("Nama: ",bantu._element)
            print("IPK: ",bantu._ipk)
            bantu=bantu._next

    # def rataIpk(self,ipk):
    #     print("===Rata-Rata IPK===: ",len*ipk/)




#test case
DLLNC=DLLNC()
DLLNC.addElementTail('Shalom',3.9)
DLLNC.addElementTail('Nabilla',3.8)
DLLNC.addElementTail('Kurniadi',3.7)
DLLNC.addElementTail('Haris',3.6)
DLLNC.printDescending()

DLLNC.deleteLast()
DLLNC.printDescending()
# DLLNC.rataIpk()



