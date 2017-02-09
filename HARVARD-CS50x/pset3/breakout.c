//
// breakout.c
//
// Computer Science 50
// Problem Set 3
//

// standard libraries
#define _XOPEN_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Stanford Portable Library
#include <spl/gevents.h>
#include <spl/gobjects.h>
#include <spl/gwindow.h>

// height and width of game's window in pixels
#define HEIGHT 600
#define WIDTH 400

// number of rows of bricks
#define ROWS 5

// number of columns of bricks
#define COLS 10

// radius of ball in pixels
#define RADIUS 10

// lives
#define LIVES 3

// height and width of paddle & constant y value in pixels
#define PADWID 60
#define PADHGT 10
#define PADY 540

// y of grid
#define GRIDY 60

// prototypes
void initBricks(GWindow window);
GOval initBall(GWindow window);
GRect initPaddle(GWindow window);
GLabel initScoreboard(GWindow window);
void updateScoreboard(GWindow window, GLabel label, int points);
GObject detectCollision(GWindow window, GOval ball);

int main(void)
{
    // seed pseudorandom number generator
    srand48(time(NULL));

    // instantiate window
    GWindow window = newGWindow(WIDTH, HEIGHT);

    // instantiate bricks
    initBricks(window);

    // instantiate ball, centered in middle of window
    GOval ball = initBall(window);

    // instantiate paddle, centered at bottom of window
    GRect paddle = initPaddle(window);

    // instantiate scoreboard, centered in middle of window, just above ball
    GLabel label = initScoreboard(window);

    // number of bricks initially
    int bricks = COLS * ROWS;

    // number of lives initially
    int lives = LIVES;

    // number of points initially
    int points = 0;

    // initialize velocity
    double xspeed = (4.0 * drand48()) + 1.5;
    double yspeed = xspeed;

    // wait for click to start?
    waitForClick();

    // keep playing until game over
    while (lives > 0 && bricks > 0)
    {
        // check for mouse evemt
        GEvent event = getNextEvent(MOUSE_EVENT);

        // if there is an event
        if (event != NULL)
        {
            
            // get paddle x coordinate from mouse
            double mousex = getX(event);
            double padx = mousex - (PADWID / 2);
            
            // set movement along x axis up to ends of window only
            if (mousex + (PADWID / 2) <= WIDTH && mousex - (PADWID / 2) > 0)
            { 
                setLocation(paddle, padx, PADY);   
            }             
        }  
        
        // move ball
        move(ball, xspeed, yspeed);    
    
        // bounce off right edge of window
        if (getX(ball) + getWidth(ball) >= getWidth(window))
        {
            xspeed = -xspeed;
        }
    
        // bounce off left edge of window
        else if (getX(ball) <= 0) 
        {
            xspeed = -xspeed;
        }
   
        // bounce off top edge of window
        else if (getY(ball) <= 0)
        {
            yspeed = -yspeed;
        }
    
        // if hits bottom edge of window
        else if (getY(ball) + getWidth(ball) >= getHeight(window))
        {
            waitForClick();
            setLocation(ball, (WIDTH / 2) - RADIUS, (HEIGHT / 2) - RADIUS);  
            lives--;
        }
    
        // detect collision with paddle or bricks
        GObject object = detectCollision(window, ball);
        if (object != NULL && strcmp(getType(object), "GRect") == 0)
        { 
            // reverse y velocity
            yspeed = -yspeed;
            
            // if the rectangle is a brick (ie not the paddle)
            if (object != paddle)
            {
                removeGWindow(window, object); 
                points++;
                bricks--;
                updateScoreboard(window, label, points);        
            }  
        }
    
        // linger before moving again
        pause(10);
        
    }
    
    if (lives == 0)
        setLabel(label, "you died :(");
    
    else if (points == 50)
        setLabel(label, "you won!");

    setLocation(label, (WIDTH - getWidth(label)) / 2, (HEIGHT - getHeight(label)) / 2);

    // wait for click before exiting
    waitForClick();

    // game over
    closeGWindow(window);
    return 0;
}

/**
 * Initializes window with a grid of bricks.
 */
void initBricks(GWindow window)
{   
    // initialize printy to GRIDY
    double printy = GRIDY;

    // define size of bricks and gap for printing before loop
    double colsize = WIDTH / COLS;
    double gap = colsize / 8;
    double bkwidth = colsize - gap;
    double bkheight = gap * 2;

    // set up row printing loop
    for (int r = 0; r < ROWS; r++)
    {
        double startx = 0;
        
        // set up column printing loop
        for (int c = 0; c < COLS; c++)
        {
            double printx = startx; 
            
            // use switch statement to define color
            char* bkcolor;
            switch (r)
            {
                case 0:
                    bkcolor = "#003333";
                    break;
                
                case 1: 
                    bkcolor = "#0b5e56";
                    break;
                
                case 2:
                    bkcolor = "#1aa3a3";
                    break;

                case 3:
                    bkcolor = "#86becb";
                    break;

                case 4:
                    bkcolor = "#b2e5e5";
                    break;

                default:
                    bkcolor = "PINK";
                    break;
            }

            // print rectangles
            GRect brick = newGRect(printx, printy, bkwidth, bkheight);
            setFilled(brick, true);
            setColor(brick, bkcolor);

            // add to brick to grid
            add(window, brick);

            // update startx
            startx = startx + colsize;
         }
    
        // update printy after each row is printed
        printy = printy + bkheight + gap;
    }  
}

/**
 * Instantiates ball in center of window.  Returns ball.
 */
GOval initBall(GWindow window)
{ 
    // draw ball
    GOval ball = newGOval((WIDTH / 2) - RADIUS, (HEIGHT / 2) - RADIUS,  RADIUS * 2, RADIUS * 2);
    setColor(ball, "#800035");
    setFilled(ball, true);
    
    // add ball to window
    add(window, ball);
    return ball;   
}

/**
 * Instantiates paddle in bottom-middle of window.
 */
GRect initPaddle(GWindow window)
{
    // draw paddle
    GRect paddle = newGRect((WIDTH - PADWID) / 2, PADY, PADWID, PADHGT);
    setColor(paddle, "#800035");
    setFilled(paddle, true);
     
    // add paddle to window
    add(window, paddle);
    return paddle;
         
}

/**
 * Instantiates, configures, and returns label for scoreboard.
 */
GLabel initScoreboard(GWindow window)
{
    // draw label
    GLabel label = newGLabel("");
    setFont(label, "SansSerif-36");
    setLabel(label, "0");
    
    // center label in window (taken from below so appears before updateScoreboard called
    double x = (getWidth(window) - getWidth(label)) / 2;
    double y = (getHeight(window) - getHeight(label)) / 2;
    setLocation(label, x, y);
    
    // add label to window
    add(window, label);
    return label;
}

/**
 * Updates scoreboard's label, keeping it centered in window.
 */
void updateScoreboard(GWindow window, GLabel label, int points)
{
    // update label
    char s[12];
    sprintf(s, "%i", points);
    setLabel(label, s);

    // center label in window
    double x = (getWidth(window) - getWidth(label)) / 2;
    double y = (getHeight(window) - getHeight(label)) / 2;
    setLocation(label, x, y);
}

/**
 * Detects whether ball has collided with some object in window
 * by checking the four corners of its bounding box (which are
 * outside the ball's GOval, and so the ball can't collide with
 * itself).  Returns object if so, else NULL.
 */
GObject detectCollision(GWindow window, GOval ball)
{
    // ball's location
    double x = getX(ball);
    double y = getY(ball);

    // for checking for collisions
    GObject object;

    // check for collision at ball's top-left corner
    object = getGObjectAt(window, x, y);
    if (object != NULL)
    {
        return object;
    }

    // check for collision at ball's top-right corner
    object = getGObjectAt(window, x + 2 * RADIUS, y);
    if (object != NULL)
    {
        return object;
    }

    // check for collision at ball's bottom-left corner
    object = getGObjectAt(window, x, y + 2 * RADIUS);
    if (object != NULL)
    {
        return object;
    }

    // check for collision at ball's bottom-right corner
    object = getGObjectAt(window, x + 2 * RADIUS, y + 2 * RADIUS);
    if (object != NULL)
    {
        return object;
    }

    // no collision
    return NULL;
}
