import numpy as np
import math

class trifasicos_estrella():
    def estrella_estrella(self,van,angulo,impedanciaA,impedanicaB,impedanciaC):
        self.valor=van*(math.cos(math.degrees(angulo)))+van*math.sin(math.degrees(angulo))
        self.valor=self.valor*(1.5+0.866025j)
        self.vb=self.valor*(-0.5-0.8660254j)
        self.vc=self.valor*(-0.5+0.8660254j)
        self.impA=impedanciaA
        self.impB=impedanicaB
        self.impC=impedanciaC
        self.voltaje_fase()


    

    def corriente_sin(self):
        A=np.matrix([[self.impA+self.impB,-self.impB],[-self.impB,self.impB+self.impC]])
        B=np.matrix([[self.valor],[self.vb]])
        x = (A**-1)*B
        ia=x[0][0]
        ic=x[0][1]
        ib=-ic-ia
        print('sus corrientes de linea y de fase son \n')
        print('Ia\n')
        print(ia)
        print('Ib\n')
        print(ib)
        print('Ic\n')
        print(ic)



    def voltaje_fase(self):
        self.van=self.valor*(0.5-0.28867513j)
        self.vbn=self.van*(-0.5-0.8660254j)
        self.vcn=self.van*(-0.5+0.8660254j)
        print('sus voltajes de fase son \n')
        print('Van\n')
        print(self.van)
        print('Vbn\n')
        print(self.vbn)
        print('Vcn\n')
        print(self.vcn)
        self.corrientes_neutro()


    def voltajes_linea(self):
        print('sus voltajes de linea son \n')
        print('Vab\n')
        print(self.valor)
        print('Vbc\n')
        print(self.vb)
        print('Vca\n')
        print(self.vc)
    
    def corrientes_neutro(self):
         ia=self.van/self.impA
         ib=self.vbn/self.impB
         ic=self.vcn/self.impC
         print('sus corrientes de linea y de fase son \n')
         print('Ia\n')
         print(ia)
         print('Ib\n')
         print(ib)
         print('Ic\n')
         print(ic)
         self.voltajes_linea()

class trifasicos_estre():
    def estrella_estrella(self,van,angulo,impedanciaA,impedanicaB,impedanciaC):
        self.valor=van*(math.cos(math.degrees(angulo)))+van*math.sin(math.degrees(angulo))
        self.valor=self.valor*(1.5+0.866025j)
        self.vb=self.valor*(-0.5-0.8660254j)
        self.vc=self.valor*(-0.5+0.8660254j)
        self.impA=impedanciaA
        self.impB=impedanicaB
        self.impC=impedanciaC
        self.voltajes_linea()


    

    def corriente_sin(self):
        A=np.matrix([[self.impA+self.impB,-self.impB],[-self.impB,self.impB+self.impC]])
        B=np.matrix([[self.valor],[self.vb]])
        x = (A**-1)*B
        ia=x[0][0]
        ic=x[1][0]
        ib=-ic-ia
        print('sus corrientes de linea y de fase son \n')
        print('Ia\n')
        print(ia)
        print('Ib\n')
        print(ib)
        print('Ic\n')
        print(ic)
        self.voltaje_fase()



    def voltaje_fase(self):
        self.van=self.valor*(0.5-0.28867513j)
        self.vbn=self.van*(-0.5-0.8660254j)
        self.vcn=self.van*(-0.5+0.8660254j)
        print('sus voltajes de fase son \n')
        print('Van\n')
        print(self.van)
        print('Vbn\n')
        print(self.vbn)
        print('Vcn\n')
        print(self.vcn)
     


    def voltajes_linea(self):
        print('sus voltajes de linea son \n')
        print('Vab\n')
        print(self.valor)
        print('Vbc\n')
        print(self.vb)
        print('Vca\n')
        print(self.vc)
        self.corriente_sin()
    
class trifasicos_delta():
    def estrella_estrella(self,van,angulo,impedanciaA,impedanicaB,impedanciaC):
        self.valor=van*(math.cos(math.degrees(angulo)))+van*math.sin(math.degrees(angulo))
        self.valor=self.valor*(1.5+0.866025j)
        self.vb=self.valor*(-0.5-0.8660254j)
        self.vc=self.valor*(-0.5+0.8660254j)
        self.impA=impedanciaA
        self.impB=impedanicaB
        self.impC=impedanciaC
        self.voltajes_linea()


    

    def corriente(self):
         ia=self.valor/self.impA
         ib=self.vb/self.impB
         ic=self.vc/self.impC
         print('sus corrientes de linea y de fase son \n')
         print('Ia\n')
         print(ia)
         print('Ib\n')
         print(ib)
         print('Ic\n')
         print(ic)
         self.voltaje_fase()



    def voltaje_fase(self):
        self.van=self.valor*(0.5-0.28867513j)
        self.vbn=self.van*(-0.5-0.8660254j)
        self.vcn=self.van*(-0.5+0.8660254j)
        print('sus voltajes de fase son \n')
        print('Van\n')
        print(self.van)
        print('Vbn\n')
        print(self.vbn)
        print('Vcn\n')
        print(self.vcn)
     


    def voltajes_linea(self):
        print('sus voltajes de linea son \n')
        print('Vab\n')
        print(self.valor)
        print('Vbc\n')
        print(self.vb)
        print('Vca\n')
        print(self.vc)
        self.corriente()
    
        
 




def nicolas(n,van,angulo,impedanciaA,impedanicaB,impedanciaC):
    if n ==1:
        a=trifasicos_estrella()
        a.estrella_estrella(van,angulo,impedanciaA,impedanicaB,impedanciaC)
    if n==2:
        a=trifasicos_estre()
        a.estrella_estrella(van,angulo,impedanciaA,impedanicaB,impedanciaC)
    if n==3:
        a=trifasicos_delta()
        a.estrella_estrella(van,angulo,impedanciaA,impedanicaB,impedanciaC)



if __name__=="__main__" :
    nicolas()