
global the_namespace_global_value

class Logger:
    print('class 内の文をこれから実行する...')
    the_class_value ='class変数の値'
    print('クラス変数を設定した')

    def __init__(self, show_class_value: bool, show_global_value: bool):
        self.show_class_value = show_class_value
        self.show_global_value = show_global_value

    def get_global_value(self):
        return the_namespace_global_value

    @classmethod
    def get_class_value_with_class_function(cls):
        return cls.the_class_value

    def get_class_value_with_instance_function(self):
        return self.the_class_value

    def show(self):
        if self.show_global_value:
            print('グローバル変数を読み込む -> ' + self.get_global_value())
        if self.show_class_value:
            print('クラス変数をインスタンスメソッド経由で読み込む -> ' + self.get_class_value_with_instance_function())
            print('クラス変数をクラスメソッド経由で読み込む -> ' + self.get_class_value_with_class_function())
    print('class 内の文を実行した')

print('地の文をこれから実行する...')
try:
    print(the_namespace_global_value)
    print('グローバル変数が設定済みであることを確認した')
except NameError:
    the_namespace_global_value  = 'global変数の値'
    print('グローバル変数が未設定なので設定した')
print('地の文を実行した')
