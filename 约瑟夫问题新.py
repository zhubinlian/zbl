#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_cell_magic('writefile', '约瑟夫问题.py', 'def qiuhe(x,y):\n    """\n    用于求和的函数\n    \n    input:\n    x:接收1个实数\n    y:接收1个实数\n    \n    output:\n    返回x+y的计算结果\n    """\n    print(x)\n    print(y)\n    z = x+y\n    return z\nresult = qiuhe(1,2) # 函数的调用\nqiuhe(y=1,x=2)\n\n\n#约瑟夫问题\n#39个人，数到3淘汰，剩余2个：10 25\n#50个人，数到4淘汰，剩余3个：1 30 47\n#100个人，数到9淘汰，剩余1个：82\n\ndef move(players,step):\n    # 移动step前的元素到列表末尾\n    num = step-1\n    while num>0:\n        tmp = players.pop(0)\n        players.append(tmp)\n        num = num-1\n        \n    return players # 根据step做了元素的移动\n\n\n\ndef play(players,step,alive):\n    """\n    模拟约瑟夫问题的函数：\n    \n    Input:\n    players:参加游戏的人数;\n    step:数到step数字的人数淘汰;\n    alive:幸存人数，即游戏结束。\n    \n    output:返回一个列表，列表中元素为幸存者编号。\n    """\n    \n    # 生成一个列表，从[1,2...,players]\n    list1 = [i for i in range(1,players+1)]\n    \n    # 进入游戏的循环，每次数到step淘汰，step之前的元素移动到列表末尾\n    #\u3000游戏结束的条件：列表剩余人数小于alive\n    \n    while len(list1) > alive:\n        # 移动step的元素到列表末尾\n        # 将如何step的元素从列表中删除\n#        num = step-1\n#        while num>0:\n#            tmp = list1.pop(0)\n#            list1.append(tmp)\n#            num = num-1\n        list1 = move(list1,step)\n        \n        list1.pop(0) # 此时的step的元素在列表的第一个位置，使用pop（0）从列表中删除\n    \n    return list1\n\nplayers_num = int(input("请输入参加游戏的人数"))\nstep_num = int(input("请输入淘汰的数字"))\nalive_num = int(input("请输入幸存人数"))\n\nalive_list = play(players_num,step_num,alive_num)\nprint(alive_list)')

