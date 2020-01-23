from dollarpy import Recognizer, Template, Point

# Define 'Template' gestures, each consisting of a name and a list of 'Point' elements.
# These 'Point' elements have 'x' and 'y' coordinates and optionally the stroke index a point belongs to.
tmpl_1 = Template('X', [
    Point(0, 0),
    Point(1, 1),
    Point(0, 1),
    Point(1, 0)])
tmpl_2 = Template('line', [
    Point(0, 0),
    Point(1, 0)])
tmpl_3 = Template('line', [
    Point(0, 0),
    Point(1, 1)])
tmpl_4 = Template('line', [
    Point(0, 0),
    Point(0, 1)])
tmpl_5 = Template('square', [
    Point(0, 0),
    Point(0, 1),
    Point(1, 1),
    Point(1, 0)])

# Create a 'Recognizer' object and pass the created 'Template' objects as a list.
recognizer = Recognizer([tmpl_1, tmpl_2])

# Call 'recognize(...)' to match a list of 'Point' elements to the previously defined templates.
result = recognizer.recognize([
    Point( 31, 141, 1),
    Point(109, 222, 1),
    Point( 22, 219, 2),
    Point(113, 146, 2)])
print(result)  # Output: ('X', 0.733770116545184)
