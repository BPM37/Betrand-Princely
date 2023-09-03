#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime

def digit_sum(num):
    return sum([int(char) for char in str(num)])

bnum_to_mm = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July',
             8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}




x = datetime.datetime.now()


class ExpressionFor:
    def __init__(self, names):
        self.names = names
        self.y_in_name_lst = []

        self.masters = [11, 22]
        self.num_behind = [13, 14, 16, 19]

        
    def last_char_in(self, name):
        #global y_in_name_lst
        last_char = len(name)-1 #princely ok = 11 -1 = 10
        
        #is last char in name y?
        if 'y' == name[last_char]:
          remain_name = name[:last_char]
          self.y_in_name_lst.append(7)
        else:
          remain_name = name
        
        return remain_name

    
    def forFirstNameResult(self, num):
        #is it master
        if num in self.masters:
            core = num
        else:
            core = digit_sum(digit_sum(num))
        
        #is it karmic
        if num in self.num_behind:
            karma_in_core = num
        else:
            karma_in_core = 0
            
        #return karma_in_core, core
        return {'karma':karma_in_core, 'core':core}
    

    def forFirstName(self):
        
        '''
        extract the individual names from str name list - first name
        '''

        '''get the first name'''
        
        self.first_name = self.last_char_in(self.names[0:self.names.index(" ")])
        self.name = names[0:names.index(" ")]
        
        #get vowels and consonants
        vowels = [ord(char.lower())-96 for char in self.first_name if char.lower() in 'aeiou']
        consonants = self.first_name.translate(str.maketrans('','','aeiouAEIOU'))
        
        #consonants to num
        cons_to_num = [ord(char.lower())-96 for char in self.first_name if char.lower() in consonants.lower()]
        
        sum_ind_cons = [digit_sum(digit_sum(abs(x))) for x in cons_to_num] #sum the elements in the consonants list
        
        sum_ind_vow = [digit_sum(digit_sum(x)) for x in vowels] #sum the elements in the vowels list
        
        #if there is any num b/c of y, add  it to vowel list
        sum_ind_vow.append(digit_sum(sum(self.y_in_name_lst)))
        self.y_in_name_lst.clear()
        
        #sum vowels and cons
        sum_vow = sum(sum_ind_vow)
        sum_cons = sum(sum_ind_cons)
        
        pre_exp = (sum_vow + sum_cons)
    
        #return {'expr':self.forr_result(pre_exp), 's_urg':self.forr_result(sum_vow), 'imager':self.forr_result(sum_cons)}
        
        return {'expr':self.forFirstNameResult(pre_exp),
                's_urg':self.forFirstNameResult(sum_vow),
                'imager':self.forFirstNameResult(sum_cons)
                }
        
        #return self.forFirstNameResult(pre_exp)
    
    
    def __str__(self):
        return f"This returns a dict like 'expr':(karma, Core), 's_urg':(karma, Core), 'imager':(karma, Core) from the first name"

'''    
exp = ExpressionFor('karen ')
what_is = exp.forFirstName()
print(what_is)
print()
print(what_is['expr']['karma']) #Princely Okwuego Emeka
'''


life_number = {
1:
"""
You are a person that works best when you are in control of
your own destiny. This can cause friction and worse in your early years but,
with perseverance, you can reap the rewards you earn.
""",
2:
"""
You need to learn to work with others. With your natural tact, you can shine
in a group and prosper in a strong relationship like a marriage.
""",
3:
"""
You have a great desire and latent ability to communicate with others.
Develop your ability (your learning skilles are also above average.
""",
4:
"""
You have the ability to be a good organizer but it may seem that you need to
expend more effort than others to get the rewards you earn.
""",
5:
"""
You will be enthusiastic and adaptable, able to succeed at almost anything if
you apply yourself.
""",
6:
"""
You are a borm homemaker, getting great satisfaction from that role and its
rewards.
""",
7:
"""
You can, and should, tap into your abundant intuition but be careful that you
inward focus does not cut you off from those close to you
""",
8:
"""
You are focused and capable but sometimes all your thoughts are dominated
by the need to acquire more and more material possessions to the exclusion
of almost everything else. This may change when you reach a point where
you feel your own needs are amply covered into the future.
""",
9:
"""
You have a generous disposition and energy to accomplish much. But, you
must remember to satisfy your own needs or other people’s demands may
drain all your resources.
"""
}


your_personal = {
1:
"""
You value your independence and have a strong desire to succeed.
At times, you need to realize that you need to listen more closely to the
views and desires of those around you.
""",
2:
"""
You need to develop your natural ability to get on well with other people. You
are a natural negotiator, able to see the other person’s point of view.
Try to remember to look after your own interests and not let other people’s
ideas take over your own thinking.
""",
3:
"""
You have a compulsion to express yourself, often creatively. You attract
attention because you are always positive.
Keep yourself focused on finishing what you start and give your best effort to
each task or you may waste much time and effort.
""",
4:
"""
You like things to be orderly and fair. This influences people to trust you.
You can be great at organizing the most complicated deals (MY ADVICE, REMEMBER)you may not
always get the rewards or recognition that you deserve.
""",
5:
"""
Your are naturally optimistic and good-natured. You like variety but you ten
to abandon projects or people sometimes.
""",
6:
"""
You have a strong attachment to your family and their needs.
Be careful that your own needs are met or you may find yourself worn down.
""",
7:
"""
You want to continue learning throughout your life and have the ability to
search beneath the surface of any topic.
Your strong focus makes you a great communicator.
But, you probably cannot be bothered with small talk and discussing things
outside your areas of interest. You must learn to control this.
Relax and give of yourself by discussing what is important to those close to
you, even though it is not of great interest to you.
""",
8:
"""
You have the qualities to achieve your personal targets, however large.
Give yourself some time in other areas or your strong focus may rob you of
many possible benefits of your material success.
""",
9:
"""
You may put helping others above achieving their own goals.
You have much to give but need to be wary of taking on too much.
You probably have strong creative abilities and should give yourself some
time to developing them just for the pleasure they give you and others.
"""
}

real = {1:
"""
You draw on leadership skills which you learned when you were younger.
""",
2:
"""
You could excel at helping others to find a way to get along with those
around them
""",
3:
"""
You may express long-repressed creative abilities and help others to develop
theirs.
""",
4:
"""
Your proven organizational skills can be used to help others achieve their
dreams. Be careful that you don't become domineering with the attitude that
your way is the only way.
""",
5:
"""
You seek change in travel or new pursuits which you may have been unable
to do earlier.
""",
6:
"""
You help improve the existence of people that are suffering financially,
physically or emotionally. Always be sure that the people want your help.
""",
7:
"""
You enjoy research and finding your own solutions.Be careful that this
does not cut you off from the social life you deserve and need.
""",
8:
"""
You have probably had to work harder than most to achieve but you
succeeded. Now you can enjoy the fruits of you struggle and may decide to
help others who are still struggling.
""",
9:
"""
Your central desire is to help others but you must ensure your own security
so that you are not completely drained by their demands especially if your
health is not 100%.
"""
}

hearts_d = {
1:
"""
You seek freedom to express yourself and achieve goals you set above those
which others may impose on you.
""",
2:
"""
Your central focus is to connect and work with others.
""",
3:"""
You seek to use your intuition which is probably more powerful than usual
and can become more fine-tuned as you become more experienced in
assessing the signals which you get from it.
""",
4:"""
You crave order in your life and cannot be comfortable until you achieve it.""",
5:"""
You will only be truly happy if you can express your ideas and desires without
restriction.""",
6:"""
You will be happiest if you can give expression to your strong creative
abilities. But, you must also ensure that you build a framework of financial
and personal support to support yourself and those close to you.""",
7:"""
You want to teach others from your knowledge and experience but you need
to remember that others may have information and ideas which you should
listen to.""",
8:"""
You want to achieve material success so that you can follow your own path.
Be careful that you do not lose the affection and support of others because of
your single-minded focus on your own goals.""",
9:"""
You want to help others. This can sometimes appear to be interference rather
than help in the eyes and minds if you come on too strongly.
"""
}

image_num = {
1:"""
Your Image Number shows your independence and strong desire to succeed.
At times, you need to realize that you need to listen more closely to their
views and desires of those around you.""",
2:"""
Your Image Number shows you have a natural ability to get on well with
other people. They are drawn to you.""",
3:"""
Your Image Number shows you are compelled from within to express
yourself, often in some creative way. You attract attention because you are
always positive. If you do not keep yourself focused on finishing what you
start and giving your best effort to each task, you may waste much time
and effort with little to show for it.""",
4:"""
Your Image Number shows you value good order and fair dealing. This
influences people to trust your and to follow you.""",
5:"""
Your Image Number reflects your natural optimism and good humor; a
person that others like to be around.
""",
6:"""
Your Image Number shows your strong attachment to your family and their
needs. Many in the medical profession at all levels have this number.""",
7:"""
Your Image Number shows your desire to continue learning throughout your
life and the ability to search beneath the surface of any topic to get the best
information you can.""",
8:"""
Your Image Number shows you have the appearance of an achiever who
keeps going until your personal targets, usually large ones, are reached.""",
9:"""
Your Image Number shows you as someone who often may put helping
others above achieving their own goals."""
}

bddict = {1:"""
This is the Birthday Number of the individualist.
""",
2:"""
This is the Birthday Number of people that can work well
with other people and inspire them.
""",
3:"""
This Birthday Number indicates a person with a positive
and very active mind.
""",
4:"""
This is the Birthday Number of the Organiser. Provided
you allow yourself time for social activities and other
energy-rebuilding things, you have a good
chance of achieving whatever goals you set for yourself.
""",
5:"""
This is the Birthday Number of the Communicator.
You like to be active and always ready to pursue
some new interest. Ensure that you keep
commitments that you make to others even if you
have become less interested in the task or them.
""",
6:"""
This is the Birthday Number of the Homemaker,
forcus on nurturing and protecting their home and family.
You need to also develop intrests outside of the home;
sport or a hobbby that give your mind something external
to engage it from time to time.
""",
7:"""
This is the Birthday Number of the Tester who learns
best from personal experience. That is a way to
ensure the lessons are well-learned but it can
be expensive. In later life, many people like
you find great satisfaction in passing on the benefits
of their experimentation to younger people.
""",
8:"""
This is the Birthday Number of people who want to
achieve financial and personal freedom and will
work whatever hours to achieve that.
For some, the accumulation of material assets
become the focus instead of enjoying the benefits
of their hard work and sharing
them with the people closest to them.
""",
9:"""
This is the Birthday Number of the Humanitarian.
People like you are responsible for helping people
around our Planet raising their living standards and
future options without much thought for their own
benefit. But, sometimes, their goals are based on
their own beliefs which conflict with the beliefs and
aspirations of the people they are genuinely trying to help.
""",
11:"""
Because of the special number associated to it,
it is now making you the visionary.
You can inspire others and create much good for yourself
and those you care about. But, sometimes, you focus too
hard on your personal vision with little regard for the
views and desires of other people.
""",
22:"""
   Because of the special number associated to it,
   it is now making you an Action-taker.
   You may have a latent capacity to achieve great
   things. You must be careful to ensure that you
   accept some input from others and don’t become
   obsesse to the point where you are unwilling to
   share the fruits of your joint efforts appropriately.
"""
}


year_num = {1:
"""
This represents a year for a new project, hobby or even a relationship. Your
energy level is likely to be higher than usual so that you can handle the extra
load that the additional activity will cause.""",
2:
"""
This represents a year for consolidation, to improve your current projects etc.
Give some time to examining and strengthening your current activities and
commitments rather than taking on even more.""",
3:
"""
This represents a year where you should devote some time to enjoying the
fruits of your hard work in the previous years. Make sure that you share what
you have gained with those who continue to help and encourage you.""",
4:
"""
This represents a year where your energy level and other reserves may be
lower after you took some time off last year. Don’t become depressed or
regretful; focus on learning how to improve the results you get from your
hard work and decide whether perhaps you are dissipating your energy and
other resources between too many projects.""",
5:
"""
This represents a year for change, perhaps in the form of enhancements to
your working methods and your social options rather than new projects. Take
any reasonable chane to travel and expend your knowledge of other ways to
do things.""",
6:
"""
This represents a year where you probably will need to put more effort into
nurturing your family and improving your home environment. That means
more work but you will probably also find yourself enjoying it more as you
get more support from those around you as the year progresses.""",
7:
"""
This represents a year where you can become more productive by putting
some time into improving your mental agility and your peace of mind. Many
people use this year to re-evaluate and strengthen their spiritual focus,
whatever it may be.""",
8:
"""
This represents the main financial year in your cycle. This may be a good
year to profit fro selling goods which you no longer use or value as much as
you did, perhaps with a view to getting things which will help or amuse you
more. But, be careful that you get value for your goods and the money you spend.
Don’t just look at getting the best price – remember that you may have more
space, money and time which used to be spent maintaining the old, outdated
gear.""",
9:
"""
This represents the year for evaluating the previous years of the cycle,
learning lessons which will help you in the next one and abandoning regrets
and other negatives which are holding you back.
"""
}

lesson = {1:
"""For Lesson 1, represented by an absence of 1's in the name you are given
at birth, you may find yourself letting others direct you too much. Look for
ways to build up your for strength of purpose and take the initiative more
often.""",
2:"""
For Lesson 2, represented by an absence of 2's, you may be more
successful in business or personal areas when you learn to listen to and
cooperate with other people instead of thinking you are always right.""",

3:""" For Lesson 3, you should not devalue your own ability or knowledge. If,
like many people with this Lesson represented in their Birth Name, you find it
difficult to communicate with other people in all kinds of personal and
business situations, get more practise - join a speaking club or even a drama
group.""",
4:""" For Lesson 4, you may show a lack of focus and direction. You can change
this in small steps. The best time to start is now.""",
5:""" For Lesson 5, you may be unsure of yourself and continue to miss out on
marvellous opportunities and experiences unless you start to rely on your
own judgement and develop some confidence in yourself and your future
success.""",
6:""" For Lesson 6, you may need to become more willing to reach out and trust
those around you to a greater extent than you have been comfortable with.""",
7:""" For Lesson 7, you could possibly reach greater levels of success than you
can imagine right now if you develop and use your natural abilities rather
than just doing enough to coast along.""",
8:""" For Lesson 8, you may need to concentrate on overcoming a tendency to
spend whatever you earn, without regard to how you will provide for your
future before circumstances change and it becomes more difficult to
replenish your reserves.""",
9:""" For Lesson 9, your challenge may be to accept, understand and cooperate
with those around you, whatever your differences in background,
beliefs or goals."""
}


debt = {13:"""
A 13 Debt indicates that you may find it hard to focus on what is most
important for achieving your goals and to keep yourself organized.
When you realize that being organized can be a great help to be better able
to cope with the obstacles or challenges which we all inevitably meet, your
enthusiasm to improve in this area will rapidly increase.
I know many people that have this pressure upon them and most of them
have used it as a spur to success rather than an excuse for giving up.""",
14:"""
If you have a 14 Debt, your challenge may seek to exploit any area of
financial, personal or professional weakness and it is likely to occur without
warning. The best way to deal with this obstacle is to be prepared to the
best of your ability, maintain the highest standards of commitment and
resist those who want to draw you into risky or unhealthy areas or activities.
""",
16:"""
When you have a 16 Debt you may, at some time, have severe
disappointment when something you have planned for and counted on fails
unexpectedly. This can crush some people but, because you are now
forewarned, you can find the inner strength and, often, external help to turn
the event into a new and greater adventure.""",
19:"""
If you find a 19 Debt when you draw up your Chart, it indicates that you
may need to draw on your inner strength to overcome a major challenge at
some time without much external help being available to you.
You should look for and treasure sincere friends that you can depend on. To
get the best from any project for yourself, you should share your plans and
the fruits of success with them."""
}

peak = {1:"""
The number 1 is related, in numerology, to self-reliance and desire to take
the lead. This is an admirable quality but, when you find this on the first peak
in your numerological life, expect that all may not go smoothly.
Where it appears on any of the peaks except the highest, (which represents
your reaching full maturity in numerological terms), it can be a sign that
everything will not be smooth sailing but the journey to your next peak is a
time when you will be able to accomplish something important for your own
development.
Patience is a quality that you will need to get the best from the period after
reaching a #1 Peak.""",
2:"""
This period is one where you will want to make progress on your personal
and business goals. It’s a period where you should also try to develop and
improve your relationships in both areas.
You may find you are more attuned to subtle indications in your relationships
and your environment generally. You will be more likely to notice and be able
to make full use of any opportunities to cooperate and collaborate that
appear during this period.
You are more likely to hear opportunity knocking. When that happens, don’t
hesitate too long if you decide to take advantage of it or it will be gone to
knock on someone else’s door.""",
3:"""
This can be a time when you find it less difficult than usual to clearly express
your inner feelings.
It is also probably a good time to invest some time and energy in any artistic
activity that you have wanted to do “some day”.
But, you may suffer regrets later if you do not maintain the level of effort you
need to keep improving your business activities.""",
4:"""
The Type 4 Peak indicates a period where serious tasks may be performed.
At the same time, some effort should be applied to helping other people.
That can have great benefits because many successful people only really
started to be successful when they made service to other people a priority.""",
5:"""
You will feel more less bound by restrictions during the period after you reach
a #5 Peak. I’m told that’s a wonderful feeling.
But, you should exercise some care because there are potential risks if you
don’t think before you leap.
If this is your first Peak, you may pay less attention than you should to your
future needs, because you feel that it will always be as easy as it is during
this period to get the money or other resources you need to gratify your
desires.""",
6:"""
The #6 Peak is an indication that support and obligation to your family will be
particularly important during that phase of your life as you head toward your
next Peak.This will not always be easy to maintain and you will get little
satisfaction if you cannot fulfil the demands that might be put on you.
But, it can be a time of great happiness and rewards (not always material) if
you succeed.""",
7:"""
As you start on the period after reaching a #7 Peak, you should take up any
opportunities to learn skills which will help you in future years.
You may have disappointments because you lack the resources or support to
make the best use of these opportunities.
Where 7 is the number on the ultimate Peak in your life, it suggests that you
will be able to learn more about those things that most interest you and also
to pass on that knowledge to younger people that it could greatly benefit.""",
8:"""
The #8 Peak heralds a period when you can absorb and develop new ideas
and put those you already have into practice, especially where they relate to
your business or vocation.
While you might find ideas and opportunities to expand your business
horizons, you must exercise some care about financial matters so that you do
not expand so fast that your progress becomes too risky.""",
9:"""
The #9 Peak indicates the beginning of a period where you can benefit from
greater exposure to new experiences and feelings.
Travel and new relationships can be especially fruitful during this period.
If your first Peak is a #9, then you may experience a distinct change in your
type of business or develop a serious relationship with someone that has not
been a major part of your life before.
"""
}