class Car():
    color = None
    top_speed = None
    def get_info(self, x, y):
        self.color = x
        self.top_speed = y
        print("You have a", self.color, "car with a top speed", self.top_speed)
        
    def cal_avg_speed(self, km, t):
        speed = km / t
        print("Your speed is", speed)