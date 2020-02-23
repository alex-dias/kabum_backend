def profitability(originalPrice, suggestedPrice):
    profitability = float(suggestedPrice)/float(originalPrice)
    if (profitability > 1):
        return [2, profitability]
    if (profitability >= 0.9):
        return [1, profitability]
    return [0, profitability]
