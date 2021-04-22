#!/usr/bin/python

class MyClass:

      def __init__( self ):
	  print ( "MyClass constructor ..." )
          self.x = 0
          self.y = 0

      def getValues( self, val1, val2 ):
          self.x = val1
          self.y = val2 
         
      def printValues( self ):
          print ( "X = " , self.x )
          print ( "Y = " , self.y )

def main():
    obj1 = MyClass()
    obj1.printValues()
    obj1.getValues( 100, 200 )
    print ( "Object 1 values ..." )
    obj1.printValues()

    obj2 = MyClass()
    obj2.printValues()
    obj2.getValues (400, 500)
    print ( "Object 2 values ..." )
    obj2.printValues()
