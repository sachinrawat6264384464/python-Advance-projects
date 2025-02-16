
def printboard(list1,list2):
   zero='X' if list1[0] else('O' if list2[0] else 0)
   one='X' if list1[1] else('O' if list2[1] else 1)
   two='X' if list1[2] else('O' if list2[2] else 2)
   three='X' if list1[3] else('O' if list2[3] else 3)
   four='X' if list1[4] else('O' if list2[4] else 4)
   five='X' if list1[5] else('O' if list2[5] else 5)
   six='X' if list1[6] else('O' if list2[6] else 6)
   seven='X' if list1[7] else('O' if list2[7] else 7)
   eight='X' if list1[8] else('O' if list2[8] else 8)

   print(f"  {zero}   |   {one}  |   {two} ")
   print(f"------|------|-----")
   print(f"  {three}   | {four}    |   {five} ")
   print(f"------|------|-----")
   print(f"  {six}   | {seven}    |   {eight} ")
    
   
if __name__ == "__main__":  
 list1=[0,0,0,0,0,0,0,0,0,0]
 list2=[0,0,0,0,0,0,0,0,0,0]
 chance = 1
 while True:
   printboard(list1,list2)
   if chance == 1:
      print(" X chance ")
      user = int(input("enter the number = "))
      list1[user] = "X"
      chance = 1 - chance
      print("")
   else:
     print(" O chance ")
     user=int(input("enter the number = "))
     list2[ user ] = "O"
     chance= 0 + 1
     print("")
     
     