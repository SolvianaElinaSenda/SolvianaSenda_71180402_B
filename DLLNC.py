from NodeMahasiswa import NodeMahasiswa
class DLLNC:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self.size == 0
    
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
        if self.isEmpty() == False:
            d = None
            bantu = self.head
            if(self.head != self.tail):
                while bantu._next != self.tail:
                    bantu = bantu._next
                hapus = self.tail
                self._tail = bantu
                d = hapus._element
                del hapus
                self._tail._next = None
            else:
                d = self._tail._element
                self.head=tail=None
            self.size -= 1
            print(d, " terhapus!")
        else:
         print("Kosong!")

    def printDescending(self):
        print("=====PRINT DESCENDING=====")
        bantu=self.head
        while bantu != None:
            print("==========")
            print("Nama: ",bantu._element)
            print("IPK: ",bantu._ipk)
            bantu=bantu._next

    def rataIpk(self):
        print("Rata-rata tidak sempat, waktu kurang")


#test case
DLLNC=DLLNC()
DLLNC.addElementTail('Shalom',3.9)
DLLNC.addElementTail('Nabilla',3.8)
DLLNC.addElementTail('Kurniadi',3.7)
DLLNC.addElementTail('Haris',3.6)
DLLNC.printDescending()

DLLNC.deleteLast()
DLLNC.printDescending()
DLLNC.rataIpk()



