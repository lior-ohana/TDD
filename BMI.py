import math
def calculation_bmi(height,weight):
    """

    param height: the height
    param weight: the weight
    return: the bmi result
    """
    if height <= 0:
        return "The height is Illegal"
    if weight <= 0:
        return "The weight is Illegal"

    return weight/pow(height,2) # calculation the bmi

def analysis_bmi(bmi_num):
    """

    param bmi_num: the bmi calculation
    return: string of weight status
    """
    if bmi_num<18.5:
        return "Underweight"
    elif 18.5<=bmi_num<25:
        return "Normalweight"
    elif 25<=bmi_num<=29.9:
        return "Deadweight"
    elif 30.0 <= bmi_num <= 34.9:
        return "obesity level 1"
    elif 35.0 <= bmi_num <= 39.9:
        return "obesity level 2"
    else:
        return "obesity level 3"






