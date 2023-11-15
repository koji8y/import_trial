print('util.logger をこれからインポートする...')
if True:
    from util.logger import Logger
else:
    from util.logger import *
print('util.logger をインポートした')

def test_run():
    print('test_run()の実行を始めた')
    logger = Logger(show_class_value=True, show_global_value=True)
    print('logger.show() をこれから実行する...')
    logger.show()
    print('test_run()の実行を終わる')

if __name__ == '__main__':
    print('test_run() をこれから実行する...')
    test_run()
