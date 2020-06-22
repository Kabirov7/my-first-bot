from ugc.views import Conclusion

class filmss(Conclusion):
    def change_const(self):
        self.table_name = 'film'

# d = films()
# d.output(d.init_random_value())