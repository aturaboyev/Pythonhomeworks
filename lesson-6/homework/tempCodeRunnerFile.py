while True:
#     print(f"if you want to get top words count write a number between 1 and {len(ar)}, else write 0")
#     try:
#         x = int(input())
#         assert(x<len(ar))
#         assert(x>=0)
#     except:
#         print("You picked wrong number. Try again!")
#         continue
#     if x==0:
#         break
#     for i in range(x):
#         print(f"{i+1}. {ar[i][1]} - {ar[i][0]} times")