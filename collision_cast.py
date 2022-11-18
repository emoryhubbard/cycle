class collision:

    def is_close(self, x, otherx):
            is_close = False
            precision = 25
            lower_limit = otherx - precision
            upper_limit = otherx + precision
            
            