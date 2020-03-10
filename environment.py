import frame_runner as fr
import math
import random


n_x = 80
n_y = 50

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def random_spawn():
    return (random.randint(0,n_x), random.randint(0,n_y))



class City():

    def __init__(self):
        self.done = False
        self.reward = 0
        self.agent_pos = random_spawn()
        self.target_pos = random_spawn()
        self.timestep = 0
        self.target_done = 0
        self.target_mised = 0
        self.n_iteration = 1
        

    def move_right(self):
        x = self.agent_pos[0]
        if x < n_x-1:
            self.agent_pos = (x + 1, self.agent_pos[1])
        else:
            self.reward -= 1

    def move_left(self):
        x = self.agent_pos[0]
        if x > 0:
            self.agent_pos = (x - 1, self.agent_pos[1])
        else:
            self.reward -= 1

    def move_up(self):
        y = self.agent_pos[1]
        if y < n_y-1:
            self.agent_pos = (self.agent_pos[0], y + 1)
        else:
            self.reward -= 1
   
    def move_down(self):
        y = self.agent_pos[1]
        if y > 0:
            self.agent_pos = (self.agent_pos[0], y - 1)
        else:
            self.reward -= 1
            
            


    # ------------------------ AI control ------------------------

    # 0 do nothing
    # 1 move right
    # 2 move left
    # 3 move up
    # 4 move down 

    def reset(self):
        self.timestep = 0
        self.agent_pos = random_spawn()
        self.target_pos = random_spawn()
        return [self.agent_pos[0], self.agent_pos[1], self.target_pos[0], self.target_pos[1]]

    def step(self, action):
        self.timestep += 1
        self.done = False
        self.reward = 0
        distance_0 = distance(self.agent_pos, self.target_pos)
        
        if action == 0:
            pass
            
        if action == 1:
            self.move_right()
            self.reward -= .5

        if action == 2:
            self.move_left()
            self.reward -= .5
            
        if action == 3:
            self.move_up()
            self.reward -= .5

        if action == 4:
            self.move_down()
            self.reward -= .5

        distance_1 = distance(self.agent_pos, self.target_pos)
        
        delta_distance = distance_0 - distance_1
        self.reward += delta_distance
        if self.agent_pos == self.target_pos:
            self.reward += 20         
        
        state = [self.agent_pos[0], self.agent_pos[1], self.target_pos[0], self.target_pos[1]]
        
        self.run_frame()
        
        return self.reward, state, self.done
    

    def run_frame(self):
        if self.n_iteration % 250 == 0 :
            fast = False
        else:
            fast = True
        fr.runner(n_x, n_y, self.agent_pos, self.target_pos, self.timestep, fast)
        if self.agent_pos == self.target_pos or self.timestep == 100:
            self.done = True
        self.n_iteration += 1

# while True:
#
#      env.run_frame()