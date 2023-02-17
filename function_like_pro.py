def avg(par1,par2,par3):
    s = par1 + par2 + par3
    m = s / 3
    return m 

def printFormatted(par1, par2, par3, res):
    print (f'the average of {par1} {par2} {par3} ia {res}')


a = 10 
b = 20 
c = 30

res = avg(a,b,c)

printFormatted(a,b,c,res)

#HW:1 redraw the diagram for second function


'''
* SRP        Single Responsibility Principle
* FUNCTION 
* CONTEXT
* CALL
* CONTROL
* PARAMETERS
* GLOBAL
* LOCAL
* RETURN
'''

'''
+-------------------------------------------------------------------------------+
|     a = 10    b = 20  c = 30                                                  |                                                           
|                                                                               |
|                    a     b     c                                              |
|          call      |     |     |                                              |
|             \\     v     v     v                                              |
|          +---avg(par1, par2, par3)----------+                                 |
|          |                                  |                                 |
|          |     s = par1 + par2 + par3       |                                 |
|          |     m = s / 3                    |                                 |
|          |                                  |                                 |
|          +------return m -------------------+                                 |
|                        |         >----------------------v                     |
|                        v         |    a     b     c     |                     |
|                       res >------^    |     |     |     |                     |
|                                       v     v     v     v                     |
|      +----------------printFormatted(par1, par2, par3, res)----------+        |
|      |                                                               |        |
|      |         print(f'the average of (par1)(par2)(par3) is (res)')  |        |
|      |                                                               |        |
|      +-------- output -----------------------------------------------+        |
|                   |                                                           |
|                   v                                                           |
|    print(f'the average of (par1)(par2)(par3) is (res)')                       |
|                                                                               |
|                                                                               |
|                                                                               |
+-------------------------------------------------------------------------------+
'''




