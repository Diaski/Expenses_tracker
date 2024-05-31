from .models import Expense 
import io
from matplotlib import pyplot as plt
import base64
def charts(user_id:int):
    expenses=Expense.query.filter_by(user_id=user_id).all()
    #l={'type':['ammount']}
    l={}
    for expense in expenses:
        if expense.type in l:
            l[expense.type]+=expense.amount
        else:
            l[expense.type]=expense.amount
    sizes=[]
    labels=[]
    for key in l:
        labels.append(key)
        sizes.append(l[key])    

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=l, autopct='%1.1f%%', startangle=140)
    plt.title('Pie Chart of Types and Amounts')
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url