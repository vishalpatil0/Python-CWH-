def gen(n):
    for i in n:
        yield i #yield method convert any normal function into generator


print(gen(3))   
# h="vishal"
# g=gen(h)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())