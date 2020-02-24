# This function calculates the profitability given an originalPrice and an suggestedPrice
# It returns a flag and the profitability percentage
def profitability(originalPrice, suggestedPrice):
    # It is a simple division to calculte the profitability percentage
    profitability = float(suggestedPrice)/float(originalPrice)
    # The flag 2 means the profitability is great, above 100%
    if (profitability > 1):
        return [2, profitability]
    # The flag 1 means the profitability is good, between 90-100%
    if (profitability >= 0.9):
        return [1, profitability]
    # The flag 0 menas the profitability is bad, less than 90%
    return [0, profitability]
