class CRC:
    def __init__(self,data,crc_polynomial):
        self.data=data
        self.polynomial=[]
        self.bits=[]
        for i in data:
            self.bits.append(int(i))
        for i in crc_polynomial:
            self.polynomial.append(int(i))
        self.quotient,self.remainder=self.__implement_crc(self.bits,self.polynomial)

    def __repr__(self):
        return f"| Data= {self.data} | \nBit Representation: {self.bits} | \nCRC Polynomial: {self.polynomial} | \nQuotient= {self.quotient} | \nCRC Remainder= {self.remainder} | "

    def __str__(self):
        return f"| Data= {self.data} | \nBit Representation: {self.bits} | \nCRC Polynomial: {self.polynomial} | \nQuotient= {self.quotient} | \nCRC Remainder= {self.remainder} | "

    def __xor(self,x,y):
        if x!=y:
            return 1
        return 0

    def __XOR(self,x,y):
        res=[]
        if len(x)==len(y):
            for i in range(len(x)):
                res.append(self.__xor(x[i],y[i]))
        return res

    def __strip(self,bitarray):
        tmp=bitarray[::-1]
        for i in range(len(bitarray)):
            if bitarray[i]==0:
                tmp.pop()
            else:
                break
        return tmp[::-1]

    def __implement_crc(self,bits,poly):
        bits=self.__strip(bits)
        poly=self.__strip(poly)
        bit_length=len(poly)
        tmp=bits[0:bit_length]
        rem=[i for i in self.__XOR(tmp,poly)]
        quotient=[1]
        for i in range(bit_length,len(bits)):
            rem=self.__strip(rem)
            rem.append(bits[i])
            if(len(rem)<bit_length):
                quotient.append(0)
            else:
                quotient.append(1)
                rem=self.__XOR(rem,poly)
        return quotient,rem

if __name__=="__main__":
    data="100100000"
    polynomial="1101"
    crc=CRC(data,polynomial)
    print(crc)
