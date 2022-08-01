import os 
commend = ipconfig\input(give me a commend)
res = os.popen(commend)
print(res.read)