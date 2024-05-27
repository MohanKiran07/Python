import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


#sample data
data=pd.DataFrame({'date':pd.date_range(start='2024-01-01', periods=100,freq='D'),'calories_burn':np.random.randint(1500,3000,100),'steps':np.random.randint(3000,10000,100),'sleep_hours':np.random.randint(7,11,100),'heart_rate':np.random.randint(60,100,100) })


#plots
def plots():
    
    #calories burn
    plt.subplot(2,2,1)
    plt.plot(data['date'],data['calories_burn'],label='calories burn',c='orange')
    plt.xlabel('date')
    plt.ylabel('calories burn')
    plt.title('calories burn trend')
    plt.legend()
    
    # steps
    plt.subplot(2,2,2)
    plt.plot(data['date'],data['steps'],label='steps',c='b')
    plt.xlabel('date')
    plt.ylabel('steps')
    plt.title('steps trend')
    plt.legend()
    
    #sleep hours
    plt.subplot(2,2,3)
    plt.plot(data['date'],data['sleep_hours'],label='sleep_hours',c='y')
    plt.xlabel('date')
    plt.ylabel('sleep hours')
    plt.title('sleep hours trend')
    plt.legend()
    
    # heart rate
    plt.subplot(2,2,4)
    plt.plot(data['date'],data['heart_rate'],label='heart_rate',c='r')
    plt.xlabel('date')
    plt.ylabel('heart rate')
    plt.title('heart rate trend')
    plt.legend()
    
    #show
    plt.tight_layout()
    plt.suptitle('Fitness Tracker Analysis')
    plt.show()

if __name__=='__main__':
    plots()