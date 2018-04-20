"""
Exam 2, problem 1.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and James (Bo) Geyer.  April 2018.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1()


###############################################################################
# Done: 2.  READ the code of the  Rect  class below.
#
#   Once you are confident that you understand the  Rect  class and its code,
#   change the TO-DO for this problem to DONE.
#
#   If you do NOT understand the  Rect  class and its code,
#   talk to your instructor to see how to proceed.
###############################################################################
class Rect(object):
    def __init__(self, width, height):
        self.w = width
        self.h = height


def run_test_problem1():
    """ Tests the   problem1   function. """
    # -------------------------------------------------------------------------
    # done: 3. Implement at least 2 tests of the  problem1  function.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1   function:')
    print('--------------------------------------------------')

    # Test 1:
    rect1 = [Rect(5, 5), Rect(10, 10)]
    expected = 25 + 100  # which is 125
    answer = problem1(rect1)
    print()
    print('Test 1 is: problem1')
    print('  Expected:', expected)
    print('  Actual:  ', answer)

    # Test 2:
    rect2 = [Rect(3, 5), Rect(5, 10), Rect(1,1), Rect(2,3)]
    expected = 15 + 50 + 1 + 6  # which is 72
    answer = problem1(rect2)
    print()
    print('Test 1 is: problem1')
    print('  Expected:', expected)
    print('  Actual:  ', answer)





def problem1(rectangles):
    tot = 0
    for k in range(len(rectangles)):
        tot = tot + (rectangles[k].w * rectangles[k].h)
    return tot

    """
    What comes in:  A sequence of  Rect  objects.
    What goes out:  Returns the sum of the areas of the given  Rect  objects.
    Side effects:   None.
    Example:
      problem1([Rect(5, 10),
                Rect(4, 3),
                Rect(100, 7)]
         returns 50 + 12 + 700, which is 762

    Type hints:
    :param rectangles: [Rect]
    :return: int
    """
    # -------------------------------------------------------------------------
    # Done: 4. Implement and test this function.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()