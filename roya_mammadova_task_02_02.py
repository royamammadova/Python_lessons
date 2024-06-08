# -*- coding: utf-8 -*-
"""Roya Mammadova - Task_02_02.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12r7pRJre-k0oHEl5q-pGlHCrJzo9d5-q

**1)** Create a class with names of fruits and add a new fruit, "fig", to the end of the list and print the updated list.

**2)** Create a list with the ages of the children in the class and print the length of the list.

**3)** Insert a new fruit, "grape", at the second position in the list and print the updated list.

**4)** Remove a specific fruit, "fig", from the list using the remove method and print the updated list.

**5)** Print the last fruit in the list after sorting it in reverse alphabetical order using the sort method.

**6)** Create a copy of the list sorted in alphabetical order without modifying the original list, and print both lists.

**7)** Delete the values from the first element up to the fourth element in the list given below

zodiac_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Capricorn"]

**8)** Prompt the user to enter a name, then print the second letter of the entered name to the screen.

**9)** Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. For example,

What is your name? Khalid

How old are you? 23

Khalid will be 100 years old in the year 2101

**10)** Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Get Input from user. For example, 5 + 55 + 555 = 615
"""

#Task1
fruits=['banana','apple','orange']
fruits.append('fig')
print(fruits)

#Task2
ages=[15,12,17,9,14]
print(len(ages))

#Task3
fruits.insert(1,'grape')
print(fruits)

#Task4
fruits.remove('fig')
print(fruits)

#Task5
fruits.sort(reverse=True)
print(fruits)
last_fruit=fruits[-1]
print(last_fruit)

#Task6
fruits1=fruits.copy()
fruits1.sort()
print(fruits)
print(fruits1)

#Task7
zodiac_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Capricorn"]
del zodiac_signs[0:4]
print(zodiac_signs)

#Task8
name=input('Enter the name:')
print(name[1])

#Task9
name=input('What is your name? ')
age=int(input('How old are you? '))
print(f"{name} will be 100 years old in the year {2124-age}")

#Task10
n=input()
print(n,'+',n+n,'+',n+n+n,'=',int(n)+int(n+n)+int(n+n+n))