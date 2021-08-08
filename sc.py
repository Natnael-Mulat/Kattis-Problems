import turtle

import random

"""
Homework 9- Recursion and Fractals
 
Authors: Abigail Santiago and Natnael Mulat
 
Time Spent: 4 hours
 
 """

def recursive_delete(str_, char):
    """
        This function deletes the character char in the parameter str_.
        
        Parameters:
            str_- A string of an arbitrary length. 
            
            char- A character 
            
        Returns:
            The string str_ without any character char in the string.  
    """
    
    #base case
    if str_ == '':
        
        return ''
    #recursive case
    letter = str_[0]
    
    if letter == char:
        
        return recursive_delete(str_[1:], char)
    
    else:
        
        return letter + recursive_delete(str_[1:], char)
    
def double_countdown(n):
    """
        This function returns the sequence n to 0 and then 0 to n.
        
        Parameters:
            n- The given integer.
            
        Returns:
            The seqeuence n to 0 and then 0 to n. 
    """
    
    #base case
    if n == 0:
        
        return '0'
    
    #recursive case
    
    return str(n) +' '+ double_countdown(n-1)+ ' ' + str(n)
    
    
def draw_koch_snowflake(length,level):
    """
        This function draws a koch snowflake of a given side length and level.
        
        Parameters:
            length- The given length of a side.
            
            level- The given level of the snowflake.
            
        Returns:
            The koch snowflake. 
    """
    SNOWFLAKE_ANGLE = 120
    
    turtle.speed('fastest') 
    
    draw_side(length, level)
    
    turtle.right(SNOWFLAKE_ANGLE) 
        
    draw_side(length, level)
    
    turtle.right(SNOWFLAKE_ANGLE)
    
    draw_side(length, level)
    
    turtle.done()
  
def draw_side(length, level):
    """
        This function draws a side of the koch snowflake.
        
        Parameters:
            length- The given length of a side.
            
            level- The given level of the snowflake.
            
        Returns:
            One side of the koch snowflake. 
    """
    TURNING_ANGLE = 60
    
    ROTATE_ANGLE = 120
    
    #base case
    if level == 1:
       turtle.forward(length)
       return
    #recursive case    
    
    draw_side(length / 3, level-1)
    
    turtle.left(TURNING_ANGLE)
    
    draw_side(length / 3, level-1)
    
    turtle.right(ROTATE_ANGLE)
    
    draw_side(length / 3, level-1)
    
    turtle.left(TURNING_ANGLE)
    
    draw_side(length / 3, level-1)
    

def draw_mondrian(x, y, height, width, direction):
    """
        This function draws a Mondrian artpiece.
        
        Parameters:
            x- X-coordinate of the top left corner of the box.
            
            y- Y-coordinate of the top left corner of the box.
            
            height- The height of the box.
            
            width- The width of the box.
            
            direction- If the direction is True the box will be split
            vertically, otherwise it will be split horizontally.
            
        Returns:
            The completed Mondiran artpiece. 
    """
    CORNER_ANGLE = 90
    
    turtle.speed("slowest")
    
    turtle.forward(width)
    
    turtle.right(CORNER_ANGLE)
    
    turtle.forward(height)
    
    turtle.right(CORNER_ANGLE)
    
    turtle.forward(width)
    
    turtle.right(CORNER_ANGLE)
    
    turtle.forward(height)
    
    turtle.right(CORNER_ANGLE)
    
    split_box(x, y, height, width, direction)
    
    turtle.done()
    
        
def split_box(x, y, height, width, direction):
    """
        This function splits a given box within a Mondrian artpiece.
        
        Parameters:
            x- X-coordinate of the top left corner of the box.
            
            y- Y-coordinate of the top left corner of the box.
            
            height- The height of the box.
            
            width- The width of the box.
            
            direction- If the direction is True the box will be split
            vertically, otherwise it will be split horizontally.
            
        Returns:
            The split box of the Mondrian artpiece. 
    """
    RE_ORIENTING_ANGEL = 90
    #base case
    if (width - x) * (height - y) < 30000:
        
        return
    
    #recursive case
    if direction == True:
        
        x_new = random.randrange(x + (width//4), x + (width//2))
        
        turtle.forward(x_new)
        
        turtle.right(RE_ORIENTING_ANGEL)
        
        turtle.forward(height)
        
        turtle.back(height)
    
        turtle.left(RE_ORIENTING_ANGEL)
        
        turtle.back(x_new)
        
        split_box(x, y, height, x_new, False)
        
        turtle.forward(x_new)
        
#         split_box(x, y, height, width-x_new, False)
#         
#         turtle.back(x_new)
        
        
    else:
        turtle.right(RE_ORIENTING_ANGEL)
        
        y_new = random.randrange(height // 4, height)
        
        turtle.forward(y_new)

        turtle.left(RE_ORIENTING_ANGEL)
        
        turtle.forward(width)
        
        turtle.back(width)
        
        turtle.left(RE_ORIENTING_ANGEL)
        
        turtle.forward(y_new)
        
        turtle.right(RE_ORIENTING_ANGEL)
        
        split_box(x, y, y_new, width, True)
        
        turtle.right(RE_ORIENTING_ANGEL)
        
        turtle.forward(y_new)
        
        turtle.left(RE_ORIENTING_ANGEL)
        
        split_box(x, y - y_new, height - y_new, width, True)
        
        turtle.left(RE_ORIENTING_ANGEL)
        
        turtle.forward(y_new)
        
        turtle.right(RE_ORIENTING_ANGEL)
      
        
         