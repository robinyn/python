import graphics as g

class agent():
    def __init__(self, pos, color=[0, 0, 0]):
        self.pos = pos
        self.drawn = False
        self.color = color
        self.generation = 1

    def print_agent(self, win):
        if self.drawn:
            return
        self.pos.draw(win)
        self.drawn = True

def check_condition(curX, curY, agent_dict, check_mode):
    sur_count = 0

    for x in range(-10,10,step=10):
        for y in range(-10,10,step=10):
            if curX+x < 0 or curY+y <0:
                break
            if (curX+x, curY+y) in list(agent_dict.keys()):
                sur_count += 1
    
    if check_mode == 0:
        if sur_count < 2:
            return False
        elif sur_count >=2 and sur_count < 4:
            return True
    else:
        if sur_count == 3:
            return True
        else:
            return False

def propagate_life(agent_dict, win):
    for agent in agent_dict.values():
        if not check_condition(agent.pos.getP1().getX(), agent.pos.getP1().getY(), 0):
            return False 

    for x in range(win.getWidth(), step=10):
        for y in range(win.getHeight(), step=10):
            return check_condition(x, y, agent_dict, 1)
                

def print_map(agent_dict, win):
    for agent in agent_dict.values():
        agent.print_agent(win)

def main():
    win = g.GraphWin(title='Game of Life', width=500, height=500)
    agent_dict = dict()
    user_in = ''
    while user_in != 'exit':
        p1 = win.getMouse()
        p1 = g.Point((p1.getX()//10)*10,(p1.getY()//10)*10)
        p2 = g.Point(p1.getX()+10, p1.getY()+10)
        rect = g.Rectangle(p1, p2)
        agent_dict[(p1.getX(), p1.getY())] = agent(rect)
        print_map(agent_dict, win)
        #print(agent_dict[len(agent_dict)-1].pos.getP1())


        #rect.draw(win)

if __name__ == '__main__':
    main()