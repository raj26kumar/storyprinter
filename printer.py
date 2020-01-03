import textwrap

story = """The Saint's wisdom :

Kandagupta was a famous saint. He lived in the outskirts of Maninagar which was the capital of Manipur Kingdom. There were very few who did not know about the wisdom of Kandagupta. He was also known for his fortune telling. 

Maniraj who was the king of Manipuri came to know of the feats of Kandagupta. He wanted to pay respect to this great saint. So, he invited Kandagupta to his palace.

When Kandagupta arrived, Maniraj welcomed him and offered him a seat. Then, the king asked the saint to tell something about his feature from his horoscope.

After a keen observation into the king’s horoscope, Kandagupta started telling the future boons to be blessed upon the king. The king was so happy. He kept on rewarding the saint with gold and silver for every boon told by Kandagupta. 

Now, came the time to say the future misfortunes. The whole outlook of Maniraj started to change. At one point he shouted, “Stop! You filthy soul! How dare you say such nonsense! I order you to say me the time of your death". 

Kandagupta replied in a small voice, "My lord! According to my calculations, my death will take place just an hour before thy death". 

The king was stunned. He felt his error. He begged pardon from Kandagupta and sent him off with furthermore wealth. 
               

MORAL : Wisdom is more able than power. """


wrapper = textwrap.TextWrapper(width=43)

string = wrapper.fill(text = story)
print(string)


