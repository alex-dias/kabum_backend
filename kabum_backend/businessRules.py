def profitability(originalPrice, suggestedPrice):
    profitability = float(suggestedPrice)/float(originalPrice)
    if (profitability > 1):
        return 2
    if (profitability >= 0.9):
        return 1
    return 0
