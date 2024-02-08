""" Instructions
"""  """
"""  """I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
"""  """
"""  """Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
"""  """
"""  """It will take your current age as the input and output a message with our time left in this format:
"""  """
"""  """You have x weeks left.
 """

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

weeks = 52
weeks_until_death = 90 - int(age)
death = (weeks_until_death * weeks)
print(f"You have {death} weeks left.")