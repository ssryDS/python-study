
print("""企业发放的奖金根据利润提成。利润(I)低于或等于 10万元时，奖金可提 10%；
      利润高于 10万元，低于 20 万元时，低于10 万元的部分按 10%提成，高于 10万元的部分，可提成 7.5%；
      20 万到40 万之间时，高于 20 万元的部分，可提成5%；40万到 60 万之间时高于40 万元的部分，可提成 3%；
      60万到100万之间时，高于 60 万元的部分，可提成1.5%，高于100万元时，
      超过 100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？""")


n=int(input('请输入当月利润:'))
if(n<100000):
    print("%d"%(n*0.1))
elif(n<200000):
    print("%d" %((n-100000)*0.075+100000*0.1))
elif(n<400000):
    print("%d" %((n-200000)*0.05+100000*0.1+100000*0.075))
elif(n<600000):
    print("%d" %((n-400000)*0.03)+100000*0.1+100000*0.075+200000*0.05)
elif(n<1000000):
    print("%d" %((n-600000)*0.015+400000*0.03+100000*0.1+100000*0.075+200000*0.05))
elif(n>1000000):
    print("%d" %((n-1000000)*0.01+400000*0.01+400000*0.03+100000*0.1+100000*0.075+200000*0.05))
