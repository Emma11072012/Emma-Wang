#!/usr/bin/env python
# coding: utf-8

# In[1]:


name=input('Hi, my name is BOB, what is your name?')


# In[2]:


print('Nice to meet you ', name)


# In[3]:


music = ["piano", "clarinet", "singing"]
art = ["drawing", "painting", "pottery"]
sport = ["artistic swimming", "tennis", "volley ball"]


# In[4]:


activity=input(' Hi Emma! What is your favorite activity? ')


# In[5]:


if activity in music:
    print('Wow! you are a muscian! I love ', activity)
elif activity in art:
    print('Wow! you are an artist! I love ', activity)
elif activity in sport:
    print('Wow! you are an athlete! I love ', activity)
else:
    print('I love ', activity)


# In[6]:


food=["ice cream","steak","noodles","salad","candy"]

print(name, ', I am a foodie, I love many food, for example, ')
for x in food:
    print (x)


# In[7]:


color=input( 'What is your favorite color?')


# In[8]:


print('ooooh!', color,'is such a pretty color!')


# In[9]:


activity=input('do you like coding?')


# In[10]:


print('I love coding')


# In[11]:


question=input('how can I help you?')


# In[12]:


if "joke" in question:
    print('why did the cow cross the road? Because he wanted to get to the moooovies! haha!')
elif "movie" in question:
    print('I cannot play movies, but you can find them on Netflix.')
elif "song" in question:
    print('I cannot play song, but you can find them on Spotify.')
else:
    print('Sorry! I do not understand your question!')


# In[ ]:




