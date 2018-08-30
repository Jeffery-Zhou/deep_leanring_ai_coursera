"""
Hi, everyone, you can get these links by Xpath tool in Chrome called Xpath Helper.
"""
links = """
f17docs/lecture_1_introduction.pdf
f17docs/lecture_2_behavior_cloning.pdf
f17docs/hw1fall2017.pdf
f17docs/lecture_3_rl_intro.pdf
f17docs/lecture_4_policy_gradient.pdf
f17docs/tf_review_session.pdf
f17docs/lecture_5_actor_critic_pdf.pdf
f17docs/hw2_final.pdf
f17docs/lecture_6_value_functions.pdf
f17docs/lecture_7_advanced_q_learning.pdf
f17docs/lecture_8_model_based_planning.pdf
f17docs/hw3.pdf
f17docs/lecture_9_model_based_rl.pdf
f17docs/lecture_10_imitating_optimal_control.pdf
f17docs/advanced_model_learning.pdf
f17docs/lecture_11_control_and_inference.pdf
f17docs/hw4.pdf
f17docs/lecture_12_irl.pdf
f17docs/lecture_13_advanced_pg.pdf
f17docs/lecture_13_exploration.pdf
f17docs/lecture_14_transfer.pdf
f17docs/lecture_15_multi_task_learning.pdf
f17docs/lecture_16_meta_learning.pdf
f17docs/lecture_17_challenges.pdf
"""

link_lst = links.split()
print(link_lst)

print(len(set(link_lst)))

url = "http://rail.eecs.berkeley.edu/deeprlcourse-fa17/"
for i in link_lst:
    print(url+i)


"""
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_1_introduction.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_2_behavior_cloning.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/hw1fall2017.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_3_rl_intro.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_4_policy_gradient.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/tf_review_session.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_5_actor_critic_pdf.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/hw2_final.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_6_value_functions.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_7_advanced_q_learning.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_8_model_based_planning.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/hw3.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_9_model_based_rl.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_10_imitating_optimal_control.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/advanced_model_learning.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_11_control_and_inference.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/hw4.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_12_irl.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_13_advanced_pg.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_13_exploration.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_14_transfer.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_15_multi_task_learning.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_16_meta_learning.pdf
http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_17_challenges.pdf
"""