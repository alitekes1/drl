#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gym 
import numpy as np
env=gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False)
env.reset()

state_numbers=env.observation_space.n ## observation space boyutunu verir.
action_number=env.action_space.n ## action ların sayısını verir.

print(f"action numbers:{action_number}, state numbers:{state_numbers}")

q_table=np.zeros((state_numbers,action_number))## q değerlerini tutacak olan q table oluşturuldu.

episode=1000
learning_rate=0.5
discount_factor=0.9

outcomes=list()

for i in range(episode):
    state,_ = env.reset()# her episode da agent start state inden başlıyor.
    is_reach_to_goal=False# agent istenen goal a ulaşma durumu
    outcomes=list()
    
    outcomes.append("failure")
    
    while not is_reach_to_goal:# bir bolümde hedefe ulaşana kadar
        if np.max(q_table[state]>0):# ilgili state deki max q değerini 0 dan büüykse
            action=np.argmax(q_table[state])# action ımız bu q state deki max q value suna sahip olan action olarak seçiyoruz.
        else:# eğer o state deki tüm action value lar <=0 ise o state deki random bir action seçeceğiz
            action=env.action_space.sample()# random action
        
        new_state,reward,is_reach_to_goal,boundry_info,_=env.step(action)
        # seçilen action ı agent gerçekleştirdi ve bize bu değerleri döndürdü.
        # q table ı güncellememiz gerekiyor.
        
        q_table[state,action]+=learning_rate*(reward + discount_factor*np.argmax(q_table[new_state])-q_table[state,action])
        
        state=new_state
        
        if reward:
            outcomes[-1]="Success"

print(q_table)
            
    
    
    
    
    
    

