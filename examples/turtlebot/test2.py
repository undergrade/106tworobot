#!/usr/bin/env python
import gym
import gym_gazebo
import time
import numpy
import random
import time
import pickle
from functools import reduce

import qlearn
import liveplot

#def qt_method()
#    id(qt_method) = 140292432748104

    

def render():
    render_skip = 0 #Skip first X episodes.
    render_interval = 50 #Show render Every Y episodes.
    render_episodes = 10 #Show Z episodes every rendering.

    if (x%render_interval == 0) and (x != 0) and (x > render_skip):
        env.render()
    elif ((x-render_episodes)%render_interval == 0) and (x != 0) and (x > render_skip) and (render_episodes < x):
        env.render(close=True)

if __name__ == '__main__':

#    env = gym.make('1')
    env = gym.make('GazeboCircuit2TurtlebotLidar-v0')
    outdir = '/tmp/gazebo_gym_experiments'
    env = gym.wrappers.Monitor(env, directory=outdir, force=True, write_upon_reset=True)
#    env = gym.wrappers.Monitor(env, outdir, force=True)
    plotter = liveplot.LivePlot(outdir)
    last_time_steps = numpy.ndarray(0)

    qlearn = qlearn.QLearn(actions=range(env.action_space.n),
                    alpha=0.8, gamma=0.8, epsilon=0.0011)

    initial_epsilon = qlearn.epsilon

    epsilon_discount = 0.999

    start_time = time.time()
    total_episodes = 10
    highest_reward = 0
#    print("------------------------------------------------------\n"+str(qlearn.q)+"\n-----------------------------------------------------------------")
#    print(type(qlearn.q))

    file = open("qtable.dat", "rb")
    qlearn.q = pickle.load(file)
    file.close()
#    print("------------------------------------------------------\n"+str(qlearn.q)+"\n-----------------------------------------------------------------")
#    print(type(qlearn.learn))
#    print(id(qlearn.learn))
   
#    print(qlearn.learn)
#    print(qlearn.learn[state,action])
 
        

    for x in range(total_episodes):
        done = False

        

    
        








        cumulated_reward = 0 #Should going forward give more reward then L/R ?
        
        observation = env.reset()
        
        if qlearn.epsilon > 0.001:
            qlearn.epsilon *= epsilon_discount

        #render() #defined above, not env.render()

        state = ''.join(map(str, observation))

        for i in range(10000):

            # Pick an action based on the current state
            action = qlearn.chooseAction(state)

            # Execute the action and get feedback
            observation, reward, done, info = env.step(action)
            cumulated_reward += reward
            
           
            
           
            if highest_reward < cumulated_reward:
                highest_reward = cumulated_reward

            nextState = ''.join(map(str, observation))


            

            qlearn.learn(state, action, reward, nextState)
            
            
            
             
            
            
            env._flush(force=True)

            if not(done):
                
                
                state = nextState
               
            else:
                last_time_steps = numpy.append(last_time_steps, [int(i + 1)])
                break

        if x%100==0:
            plotter.plot(env)
        
        m, s = divmod(int(time.time() - start_time), 60)
        h, m = divmod(m, 60)
        print ("EP: "+str(x+1)+" - [alpha: "+str(round(qlearn.alpha,2))+" - gamma: "+str(round(qlearn.gamma,2))+" - epsilon: "+str(round(qlearn.epsilon,2))+"] - Reward: "+str(cumulated_reward)+"     Time: %d:%02d:%02d" % (h, m, s))
    

    #Github table content
    print ("\n|"+str(total_episodes)+"|"+str(qlearn.alpha)+"|"+str(qlearn.gamma)+"|"+str(initial_epsilon)+"*"+str(epsilon_discount)+"|"+str(highest_reward)+"| PICTURE |")

    l = last_time_steps.tolist()
    l.sort()
    
    
   
    #print("Parameters: a="+str)
    print("Overall score: {:0.2f}".format(last_time_steps.mean()))
    print("Best 100 score: {:0.2f}".format(reduce(lambda x, y: x + y, l[-100:]) / len(l[-100:])))
    print (qlearn.learn)
    print(id(qlearn.learn))

#    print("------------------------------------------------------\n"+str(qlearn.q)+"\n-----------------------------------------------------------------")
#    file = open("qtable.dat", "wb")
                
#    pickle.dump(qlearn.q,file)

            
 #   file.close()

    env.close()
