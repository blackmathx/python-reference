# eimbo 9/15/23
# Python Language Reference - Packages


# see reference at: https://www.programiz.com/python-programming/package

########## packages
# earlier than Python 3.3 package folders required an empty __init__.py file
# __init__.py can initialize code, set package variables, and provide namespaces.see  https://sparkbyexamples.com/python/what-is-python-__init__-py-for/
# use modules unless you need to organize large amount of code. 

def do():
    print('using package..')
    fun.fun()


if __name__ == '__main__':
    
	from mypackage import run
	from mypackage.fffmodule import fun
    # OR # import mypackage.fffmodule.fun as fff
    #OR # from mypackage.fffmodule import fun

	do()
	print('doing more')
	run.runny()


fun.fun() # does stuff outside of __main__

