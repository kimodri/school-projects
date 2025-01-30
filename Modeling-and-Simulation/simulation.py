import matplotlib.pyplot as plt
import numpy as np


daily_speed_growth_rate = 0.05  # 5% improvement per week
daily_comprehension_growth_rate = 0.03  # 3% improvement per week
sporadic_speed_growth_rate = 0.02  # 2% improvement per week
sporadic_comprehension_growth_rate = 0.01  # 1% improvement per week
weeks = list(range(11))

print("Please input scores in decimal representation of percentage.")
print("Please input speed between 25 and 250, inclusive.")


try:
    score = float(input("Please input the initial comprehension score: "))
    speed = float(input("Please input the reading speed (WPM): "))
except:
    print("Please enter the right format.")
    exit()

if (score < 0.1 and score > 1.0):
    print("Please enter the right values1.")
    exit()
if (speed < 25 and speed > 250):
    print("Please enter the right values2.")
    exit()

def simulate(score, speed):
   
    daily_comprehension = [min(score * (1 + daily_comprehension_growth_rate * i), 1) for i in range(11)] 
    daily_speed = [min(speed * (1 + daily_speed_growth_rate * i), 250) for i in range(11)]
    sporadic_comprehension = [min(score * (1 + sporadic_comprehension_growth_rate * i), 1) for i in range(11)] 
    sporadic_speed = [min(speed * (1 + sporadic_speed_growth_rate * i), 250) for i in range(11)]

    if score < 0.75:
            if speed < 31:
                note1 = "Frustration I"
            elif 31 <= speed < 61:
                note1 = "Frustration II"
            elif 61 <= speed < 91:
                note1 = "Frustration III"
            elif 91 <= speed < 111:
                note1 = "Frustration IV"
            elif 111 <= speed < 141:
                note1 = "Frustration V"
            else:  
                note1 = "Frustration VI"
    
    elif 0.75 <= score <= 0.89:  # Ensure coverage for this range
            note1 = np.random.choice([
                    "Instructional I", "Instructional II",
                    "Instructional III", "Instructional IV",
                    "Instructional V", "Instructional VI"
                ])
        
    else:  
            if 70 <= speed < 100:
                note1 = "Independent I"
            elif 100 <= speed < 120:
                note1 = "Independent II"
            elif 120 <= speed < 140:
                note1 = "Independent III"
            elif 140 <= speed < 170:
                note1 = "Independent IV"
            elif 170 <= speed < 190:
                note1 = "Independent V"
            else:  # modsimDf['final_wpm'][i]
                note1 = "Independent VI"

    if daily_comprehension[-1] < 0.75:
            if daily_speed[-1] < 31:
                note = "Frustration I"
            elif 31 <= daily_speed[-1] < 61:
                note = "Frustration II"
            elif 61 <= daily_speed[-1] < 91:
                note = "Frustration III"
            elif 91 <= daily_speed[-1] < 111:
                note = "Frustration IV"
            elif 111 <= daily_speed[-1] < 141:
                note = "Frustration V"
            else:  
                note = "Frustration VI"
    
    elif 0.75 <= daily_comprehension[-1] <= 0.89:  # Ensure coverage for this range
            note = np.random.choice([
                    "Instructional I", "Instructional II",
                    "Instructional III", "Instructional IV",
                    "Instructional V", "Instructional VI"
                ])
        
    else:  
            if 70 <= daily_speed[-1] < 100:
                note = "Independent I"
            elif 100 <= daily_speed[-1] < 120:
                note = "Independent II"
            elif 120 <= daily_speed[-1] < 140:
                note = "Independent III"
            elif 140 <= daily_speed[-1] < 170:
                note = "Independent IV"
            elif 170 <= daily_speed[-1] < 190:
                note = "Independent V"
            else:  # modsimDf['final_wpm'][i]
                note = "Independent VI"


    # plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Speed
    ax1.plot(weeks, daily_speed, label="Daily Readers Speed (WPM)", marker="o")
    ax1.plot(weeks, sporadic_speed, label="Sporadic Readers Speed (WPM)", marker="o", linestyle='--')
    ax1.set_title("Weekly Improvement in Reading Speed", fontsize=12, fontweight="bold")
    ax1.set_xlabel("Weeks", fontsize=12, fontweight="bold")
    ax1.set_ylabel("Reading Speed (WPM)", fontsize=12, fontweight="bold")
    ax1.set_xticks(np.arange(min(weeks), max(weeks) + 1, 1.0))
    ax1.legend()
    ax1.grid(True)

    # Comprehension
    ax2.plot(weeks, daily_comprehension, label="Daily Readers Comprehension", marker="o")
    ax2.plot(weeks, sporadic_comprehension, label="Sporadic Readers Comprehension", marker="o", linestyle='--')
    ax2.set_title("Weekly Improvement in Comprehension Score", fontsize=12, fontweight="bold")
    ax2.set_xlabel("Weeks", fontsize=12, fontweight="bold")
    ax2.set_ylabel("Comprehension Score", fontsize=12, fontweight="bold")
    ax2.set_xticks(np.arange(min(weeks), max(weeks) + 1, 1.0))
    ax2.legend()
    ax2.grid(True)

   
    fig.suptitle("With Daily Habit, \nyou can be: " +  note + " from " + note1, fontsize=16, fontweight="bold",y=1)


    # Show the plots
    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout to make room for the main title
    plt.show()


simulate(score, speed)
