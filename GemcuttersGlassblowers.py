# works for Gemcutter's Prism and Glassblowers Bauble
def gemcutterRecipe(qualities, partial=[]):
    s = sum(partial)
    
    # return list that gives us currency
    if s == 40: 
        print("sum(%s)=%s" % (partial, 40))
    if s >= 40:
        return

    # iterate for every sublist
    for i in range(len(qualities)):
        n = qualities[i]
        remaining = qualities[i+1:]
        gemcutterRecipe(remaining, partial + [n]) 
        
# change gem/flask qualities to calculate
qualities = [3,6,8,2,15,18,4,19]
gemcutterRecipe(qualities)
